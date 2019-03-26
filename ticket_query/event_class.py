# -*- coding: utf-8 -*-

#   2019/3/22 0022 上午 11:21     

__author__ = 'RollingBear'

import time

from PyQt5.QtWidgets import QTableWidgetItem

from ticket_query.train_service import train_service


class event_class(object):

    def __init__(self):

        self.train_service = train_service()
        pass

    def search(self, table, From='北京', To='上海', Date=time.strftime('%Y-%m-%d', time.localtime())):

        print('【{}】 from {} to {}'.format(Date, From, To))

        train_list = self.train_service.crawl_train_mess(From, To, Date)
        print(table)
        table.setRowCount(len(train_list))

        for row, item in enumerate(train_list):
            for col, i in enumerate(item):
                if i is '':
                    i = '0'
                table.setItem(row, col, QTableWidgetItem(i))

        pass
