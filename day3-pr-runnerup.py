# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

# user_list = []
#
# limit = int(input("Enter the total number of scores:"))
#
# for x in range(0,limit):
#     user_list.append(int(input("Enter the score:")))
#
# print(user_list)
#
# highest_score = user_list[1]
# second_highest_score = user_list[1]
#
# for x in range(0, limit):
#     if user_list[x] > highest_score:
#         second_highest_score = highest_score
#         highest_score = user_list[x]
#     elif user_list[x] > second_highest_score:
#         second_highest_score = user_list[x]
#
# print(user_list)
# print(second_highest_score)


n = int(input())

scores = list(input().split(" "))

for i in range(n):
    scores[i] = int(scores[i])
scores.sort();
local = n-2;
while local >= 0:
    if scores[local] < scores[local+1] :
        print(scores[local])
        break;
    else:
        local = local - 1;
