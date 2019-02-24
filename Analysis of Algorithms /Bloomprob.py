# # import sys
# #
# # data = sys.stdin.read().splitlines()
# # count = 0
# # rowcount = 0
# # rows = list()
# # for line in data:
# #     if count == 0:
# #         test = line.split(" ")
# #         rowcount = test[0]
# #         cols = test[1]
# #         iters = test[2]
# #         count = count + 1
# #     else:
# #         rows.append(line.split(" "))
# # print(rows)
#
# # Problem        : Tile Adventure
# # Language       : Python 3
# # Compiled Using : py_compile
# # Version        : Python 3.4.3
# # Input for your program will be provided from STDIN
# # Print out all output from your program to STDOUT
# def whereTo(rows, hops):
#
#
#
# def possibleHops(current_row, current_col, rowcount, cols):
#     hops = []
#     if current_row - 1 < 0:
#         if current_col - 1 < 0:
#             hops = [(current_row, current_col + 1), (current_row + 1, current_col)]
#         elif current_col + 1 < cols:
#             hops = [(current_row, current_col + 1), (current_row + 1, current_col), (current_row, current_col - 1)]
#         if current_col + 1 >= cols:
#             hops = [(current_row, current_col - 1), (current_row + 1, current_col)]
#     elif current_row + 1 < rowcount:
#         hops = [(current_row, current_col + 1), (current_row + 1, current_col), (current_row, current_col - 1), (current_row - 1, current_col)]
#
#     elif current_row + 1 == rowcount:
#         if current_col - 1 < 0:
#             hops = [(current_row, current_col + 1), (current_row - 1, current_col)]
#         elif current_col + 1 < cols:
#             hops = [(current_row, current_col + 1), (current_row - 1, current_col), (current_row, current_col - 1)]
#         if current_col + 1 >= cols:
#             hops = [(current_row, current_col - 1), (current_row - 1, current_col)]
#     return hops
#
#
# import sys
#
# data = sys.stdin.read().splitlines()
# count = 0
# rowcount = 0
# rows = list()
# for line in data:
#     if count == 0;
#         test = line.split(" ")
#         rowcount = test[0]
#         cols = test[1]
#         iters = test[2]
#         count = count + 1
#     else:
#         rows.append(line.split(" "))
# cur_row = 0
# cur_column = 0
#
# for i in range(0, iter):
#     print(rows[cur_row][cur_column])
#     hops = possibleHops(cur_row, cur_column, rowcount, cols)
#     cur_row, cur_column = whereTo(rows, cur_row, cur_column)
#
#
