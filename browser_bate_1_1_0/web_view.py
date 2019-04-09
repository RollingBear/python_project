# -*- coding: utf-8 -*-

#   2019/4/4 0004 上午 10:59     

__author__ = 'RollingBear'

import sys

from PyQt5.QtCore import pyqtSlot, QUrl, QEvent, Qt, QObject
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTabWidget, QMessageBox, QWidget, QVBoxLayout, QCompleter

from browser_bate_1_1_0.ui import ui


class new_web_view(QWebEngineView):

    def __init__(self, tab_widget):
        super().__init__()

        self.tab_widget = tab_widget

    def createWindow(self, QWebEnginePage_WebWindowType):
        created_web = new_web_view(self.tab_widget)
        self.tab_widget.newTab(created_web)
        return created_web


class web_view(QMainWindow, ui):

    def __init__(self, parent=None):

        super(web_view, self).__init__(parent)

        self.ui(self)
        self.init_ui()

    def init_ui(self):

        self.progress_bar.hide()

        # set the window full window when open the program
        # self.showMaximized()

        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        self.tab_widget.currentChanged.connect(self.tab_change)

        self.view = new_web_view(self)
        self.view.load(QUrl('https://www.baidu.com'))

        self.new_tab(self.view)

        self.url_line_edit.installEventFilter(self)
        self.url_line_edit.setMouseTracking(True)

        settings = QWebEngineSettings.defaultSettings()
        settings.setAttribute(QWebEngineSettings.PluginsEnabled, True)

        self.get_model()

    def get_model(self):

        self.m_model = QStandardItemModel(0, 1, self)
        m_completer = QCompleter(self.m_model, self)
        self.url_line_edit.setCompleter(m_completer)
        m_completer.activated[str].connect(self.onUrlChoosed)

    def new_tab(self, view):

        self.forward_btn.setEnabled(False)
        self.back_btn.setEnabled(False)
        view.titleChanged.connect(self.web_title)
        view.iconChanged.connect(self.web_icon)
        view.loadProgress.connect(self.web_progress)
        view.loadFinished.connect(self.web_progress_end)
        view.urlChanged.connect(self.web_history)
        view.page().linkHovered.connect(self.show_url)
        current_url = self.get_url(view)

        self.url_line_edit.setText(current_url)
        self.tab_widget.addTab(view, 'New Tab Page')
        self.tab_widget.setCurrentWidget(view)

    def get_url(self, web_view):

        url = web_view.url().toString()
        return url

    def close_tab(self, index):

        if self.tab_widget.count() > 1:
            self.tab_widget.widget(index).deleteLater()
            self.tab_widget.removeTab(index)
        elif self.tab_widget.count() == 1:
            self.tab_widget.removeTab(0)
            self.onNewButtonClicked()

    def tab_changed(self, index):

        current_view = self.tab_widget.widget(index)
        if current_view:
            current_view_url = self.get_url(current_view)
            self.url_line_edit.setText(current_view_url)

    def closeEvent(self, event):
        tab_num = self.tab_widget.count()
        close_info = 'You have open {} pages, are you sure to close this pages?'.format(tab_num)

        if tab_num > 1:
            result = QMessageBox.question(self, 'Close browser', close_info, QMessageBox.Ok | QMessageBox.Cancel,
                                          QMessageBox.Cancel)

            if result == QMessageBox.Ok:
                event.accept()
            elif result == QMessageBox.Cancel:
                event.ignore()
        else:
            event.accept()

    def eventFilter(self, object, event):

        if object == self.url_line_edit:
            if event.type() == QEvent.MouseButtonRelease:
                self.url_line_edit.selectAll()
            elif event.type() == QEvent.KeyPress:
                if event.key() == Qt.Key_Return:
                    self.onGoButtonClicked()
        return QObject.eventFilter(self, object, event)

    def web_title(self, title):

        index = self.tab_widget.currentIndex()

        if len(title) > 16:
            title = title[0: 17]
        self.tab_widget.setTabText(index, title)

    def web_icon(self, icon):

        index = self.tab_widget.currentIndex()
        self.tab_widget.setTabIcon(index, icon)

    def web_progress(self, progress):

        self.progress_bar.show()
        self.progress_bar.setValue(progress)

    def web_progress_end(self, is_finished):

        if is_finished:
            self.progress_bar.setValue(100)
            self.progress_bar.hide()
            self.progress_bar.setValue(0)

    def web_history(self, url):
        self.url_line_edit.setText(url.toString())
        index = self.tab_widget.currentIndex()
        current_view = self.tab_widget.currentWidget()
        history = current_view.history()

        if history.count() > 1:
            if history.currentItemIndex() == history.count() - 1:
                self.back_btn.setEnabled(True)
                self.forward_btn.setEnabled(False)
            elif history.currentItemIndex() == 0:
                self.back_btn.setEnabled(False)
                self.forward_btn.setEnabled(True)
            else:
                self.back_btn.setEnabled(True)
                self.forward_btn.setEnabled(True)

    def show_url(self, url):

        self.status_bar.showMessage(url)

    def onUrlChoosed(self, url):

        self.url_line_edit.setText(url)

    @pyqtSlot(str)
    def on_lineEdit_textChanged(self, text):

        url_group = text.split('.')

        if len(url_group) == 3 and url_group[-1]:
            return
        elif len(url_group) == 3 and not (url_group[-1]):
            www_list = ['com', 'cn', 'net', 'org', 'gov', 'cc']
            self.m_model.removeRows(0, self.m_model.rowCount())

            for i in range(0, len(www_list)):
                self.m_model.insertRow(0)
                self.m_model.setData(self.m_model.index(0, 0), text + www_list[i])

    @pyqtSlot()
    def onNewButtonClicked(self):

        new_view = new_web_view(self)
        self.new_tab(new_view)
        new_view.load(QUrl(''))

    @pyqtSlot()
    def onForwardButtonClicked(self):

        self.tab_widget.currentWidget().forward()

    @pyqtSlot()
    def onBackButtonClicked(self):

        self.tab_widget.currentWidget().back()

    @pyqtSlot()
    def onRefreshButtonClicked(self):

        self.tab_widget.currentWidget().reload()

    @pyqtSlot()
    def onStopButtonClicked(self):

        self.tab_widget.currentWidget().stop()

    @pyqtSlot()
    def onGoButtonClicked(self):
        url = self.url_line_edit.text()

        if url[0:7] == 'http://' or url[0:8] == 'https://':
            qurl = QUrl(url)
        else:
            qurl = QUrl('http://' + url)
        self.tab_widget.currentWidget().load(qurl)

    @pyqtSlot()
    def onHomeButtonClicked(self):

        home_url = QUrl('https://www.baidu.com')

        if self.tab_widget.currentWidget().title() == 'about:blank':
            self.tab_widget.currentWidget().load(home_url)
        else:
            new_view = new_web_view(self)
            self.new_tab(new_view)
            new_view.load(home_url)

    def __del__(self):
        self.view.deleteLater()
