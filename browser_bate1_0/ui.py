# -*- coding: utf-8 -*-

#   2019/3/26 0026 上午 10:14     

__author__ = 'RollingBear'

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QToolBar, QAction, QLineEdit, QTabWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView


class main_window(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt Browser bate1.0')
        self.setWindowIcon(QIcon('icons/penguin.png'))

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)

        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        self.add_new_tab(QUrl('https://www.baidu.com'), 'HomePage')

        self.setCentralWidget(self.tabs)

        new_tab_action = QAction(QIcon('icons/add_page.png'), 'New Page', self)
        new_tab_action.triggered.connect(self.add_new_tab)

        navigation_bar = QToolBar('Navigation')
        navigation_bar.setIconSize(QSize(16, 16))
        self.addToolBar(navigation_bar)

        back_btn = QAction(QIcon('icons/back.png'), 'Back', self)
        next_btn = QAction(QIcon('icons/next.png'), 'Forward', self)
        stop_btn = QAction(QIcon('icons/cross.png'), 'Stop', self)
        reload_btn = QAction(QIcon('icons/renew.png'), 'reload', self)

        back_btn.triggered.connect(self.tabs.currentWidget().back)
        next_btn.triggered.connect(self.tabs.currentWidget().forward)
        stop_btn.triggered.connect(self.tabs.currentWidget().stop)
        reload_btn.triggered.connect(self.tabs.currentWidget().reload)

        navigation_bar.addAction(back_btn)
        navigation_bar.addAction(next_btn)
        navigation_bar.addAction(stop_btn)
        navigation_bar.addAction(reload_btn)

        navigation_bar.addSeparator()
        navigation_bar.addWidget(self.url_bar)

        self.center()

    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == '':
            q.setScheme('http')
        self.tabs.currentWidget().setUrl(q)

    def renew_urlbar(self, q, browser=None):
        if browser != self.tabs.currentWidget():
            return

        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)

    def add_new_tab(self, qurl=QUrl(''), label='Blank'):

        browser = QWebEngineView()
        browser.setUrl(qurl)

        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        browser.urlChanged.connect(lambda qurl, browser=browser: self.renew_urlbar(qurl, browser))
        # browser.loadFinished.connect(
        #     lambda i=i, browser=browser: self.tabs.setTabText(i, browser.page().mainFrame().title()))

    def tab_open_doubleclick(self, i):

        if i == -1:
            self.add_new_tab()

    def current_tab_changed(self, i):
        qurl = self.tabs.currentWidget().url()
        self.renew_urlbar(qurl, self.tabs.currentWidget())

    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(i)

    def center(self):
        '''
        Set the window center of screen
        :return: None
        '''

        geomotry = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        geomotry.moveCenter(center_point)
        self.move(geomotry.topLeft())
