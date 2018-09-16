# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
# # Complete the minimumLoss function below.
# def minimumLoss(price):
#     loss_min = 0
#     for i in range(0,len(price)):
#         for j in range(i+1,len(price)):
#             price_diff = price[i] - price[j]
#             if price_diff >0 and loss_min >= price_diff:
#                 loss_min = price_diff
#     return loss_min
#
#
# if __name__ == '__main__':
#
#     n = 3
#     price = [5, 10, 3]
#
#     result = minimumLoss(price)
#
#     print(result)
#
# # !/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
#
# # Complete the stockmax function below.
# def stockmax(prices):
#     price_max = 0
#     prices_unsorted = prices
#     prices_sorted = prices.sort(reversed=True)
#     prices_dict = dict()
#     for i in range(0, n):
#         if prices_unsorted[i] not in prices_dict:
#             prices_dict[prices_unsorted[i]] = i
#         else:
#             if prices_dict[prices_unsorted[i]] < i:
#                 prices_dict[prices_unsorted[i]] = i
#
#     for price in prices_sorted:
#
#
# def compute_profit(price, prices_unsorted, prices_dict):
#     index_price = prices_dict[price]
#     for i in range(index_price, )
#
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     t = int(input())
#
#     for t_itr in range(t):
#         n = int(input())
#
#         prices = list(map(int, input().rstrip().split()))
#
#         result = stockmax(prices)
#
#         fptr.write(str(result) + '\n')
#
#     fptr.close()
