'''
Description: List.md的实验代码
version: 1.0
Author: Yuan Yitong
Date: 2021-11-28 21:51:53
LastEditors: Yuan Yitong
LastEditTime: 2021-11-28 21:54:28
'''
l = [[1, "c"], [2, "b"], [3, "a"]]
sortByFirstCol = sorted(l, key=lambda l: l[0], reverse=True);print(sortByFirstCol)
sortBySecondCol = sorted(l, key=lambda l: l[1], reverse=True);print(sortBySecondCol)
