from time import *
from rygg.classes import *
from rygg.dynamic import *
from rygg.heuristic import *


capacity = int(input())
itemsNum = int(input())

itemsLib = []


for i in range(itemsNum):
    itemsLib.append(
        Item(*input().split(' '), _id=i)
    )


if __name__ == '__main__':
    # heuristic(capacity, itemsLib)
    dynamic(capacity, itemsNum, itemsLib)