# -*- coding: utf-8 -*-

#   2019/10/25 0025 下午 1:25     

__author__ = 'RollingBear'

import numpy
import random

maxTime = 10

with open('nameList.txt', encoding='utf8') as f:
    nameList = [[line.replace('\n', ''), 0] for line in f.readlines()]

while nameList[0][1] == nameList[1][1]:
    for i in range(len(nameList)):
        nameList[i][1] = numpy.mean([random.random() for i in range(maxTime)])
    nameList.sort(reverse=True, key=lambda mark: mark[1])
    print(nameList)

print(nameList[0][0])
