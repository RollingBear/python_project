# -*- coding: utf-8 -*-

#   2019/3/22 0022 上午 11:23     

__author__ = 'RollingBear'

import requests
import json


class train_service(object):

    def __init__(self):

        with open('code.json', 'r') as file:
            code = eval(file.read())

        self.code = code
        self.code_url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9002'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36'}

    def crawl_train_mess(self, from_station, to_station, train_date):

        self.url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
            train_date, self.code[from_station], self.code[to_station])

        response = requests.get(self.url, headers=self.headers)
        train_json = json.loads(response.text)
        results = train_json['data']['result']
        train_list = []

        for i in results:
            temp = i.split('|')
            train_list.append([temp[3], temp[8], temp[9], temp[25], temp[26]])

        return train_list

    def crawl_code_mess(self):

        response = requests.get(self.code_url, headers=self.headers)
        station_list = response.text.split('@')[1:]
        code = {}

        for i in station_list:
            temp = i.split('|')
            code[temp[1]] = temp[2]

        with open('code.json', 'w') as file:
            file.write(str(code))


if __name__ == '__main__':
    ts = train_service()
    ts.crawl_code_mess()
