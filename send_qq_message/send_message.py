# -*- coding: utf-8 -*-

#   2019/3/28 0028 下午 5:29

__author__ = 'RollingBear'

import win32clipboard as w32cb

from win32gui import SendMessage, FindWindow
from win32con import CF_UNICODETEXT, WM_KEYDOWN, VK_RETURN

from time import sleep
from random import randint
from logging import info
from traceback import format_exc
from os import system

from send_qq_message.config import config


class send_msg():

    def __init__(self, target=None):
        super().__init__()

        self.conf = config('/config.ini')

        self.target = target
        self.interval = int(self.conf.get('basic').basic_interval)
        self.message = self.conf.get('basic').basic_message
        self.max_count = int(self.conf.get('basic').max_count)
        self.running_flag = True

        if target != None:
            self.rand_msg_list = self.loading_msg(self.conf.get('address').random_mes_address)
            self.sequ_msg_list = self.loading_msg(self.conf.get('address').sequential_mes_address)

    def running_state_change(self, boolean):
        self.running_flag = boolean

    def interval_modify(self, new_interval):
        self.interval = new_interval

    def message_modify(self, new_message):
        self.message = new_message

    def msg_list_modify(self, type):
        if type == 'rand':
            address = self.conf.get('address').random_mes_address
            self.open_file(address)
            self.rand_msg_list = self.loading_msg(address)
        elif type == 'sequ':
            address = self.conf.get('address').sequential_mes_address
            self.open_file(address)
            self.sequ_msg_list = self.loading_msg(address)

    def loading_msg(self, mes_address):
        with open(mes_address, 'r', encoding="utf-8-sig") as f:
            message_list = []
            result = f.readlines()
            for count in range(len(result)):
                message_list.append(result[count].replace('\n', ''))
        return message_list

    def open_file(self, file_address):
        try:
            system('notepad ' + file_address)
            return None
        except Exception:
            info(format_exc())

    def send_simple(self):
        w32cb.OpenClipboard()
        w32cb.EmptyClipboard()
        w32cb.SetClipboardData(CF_UNICODETEXT, self.message)
        w32cb.CloseClipboard()

        handle = FindWindow(None, self.target)

        count = 0

        while count <= self.max_count:
            sleep(self.interval)

            SendMessage(handle, 770, 0, 0)
            SendMessage(handle, WM_KEYDOWN, VK_RETURN, 0)

            count += 1
            print('Message Sent Count: {count}'.format(count=count))

            if self.running_flag == False:
                break

    def send_random(self):
        count = 0

        while count <= self.max_count:
            sleep(self.interval)

            rand = randint(0, len(self.rand_msg_list))

            w32cb.OpenClipboard()
            w32cb.EmptyClipboard()
            w32cb.SetClipboardData(CF_UNICODETEXT, self.rand_msg_list[rand])
            w32cb.CloseClipboard()
            handle = FindWindow(None, self.target)

            SendMessage(handle, 770, 0, 0)
            SendMessage(handle, WM_KEYDOWN, VK_RETURN, 0)

            count += 1
            print('Message Sent Count: {count}'.format(count=count))

            if self.running_flag == False:
                break

    def send_sequential(self):

        for num in range(len(self.sequ_msg_list)):
            sleep(self.interval)

            w32cb.OpenClipboard()
            w32cb.EmptyClipboard()
            w32cb.SetClipboardData(CF_UNICODETEXT, self.sequ_msg_list[num])
            w32cb.CloseClipboard()
            handle = FindWindow(None, self.target)

            SendMessage(handle, 770, 0, 0)
            SendMessage(handle, WM_KEYDOWN, VK_RETURN, 0)

            print('Message Sent Count: {count}'.format(count=num))

            if self.running_flag == False:
                break


if __name__ == '__main__':
    send = send_msg()

    print(send.rand_msg_list)
    send.msg_list_modify('rand')
    print(send.rand_msg_list)
