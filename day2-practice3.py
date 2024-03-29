
# There are N dinosaurs (enumerated 1 through N) placed in a line.
# The i-th dinosaur has a height of i meters.
#
# Ada is training The dinosaurs in the following tactic:
#
# Initially the leftmost dinosaur has the ball.
# The dinosaur that has the ball passes the ball to the nearest dinosaur to the right that is tallest
# than him.
# The previous step continues until the ball reaches the tallest dinosaur, then he throws the ball
# and scores a goal!
# Help Ada reordering the dinosaurs in such a way that the ball is passed from dinosaur
# to dinosaur exactly K times.
#
# For example, if there are 5 dinosaurs ordered as [2,3,1,5,4], then the ball
# goes 2→3→5→goal, and the ball was passed two times.
#
# Input:
# First line will contain T, number of testcases.
# Each test case consist of a line with two space separated integers N,K.
# Output:
# For each testcase, output in a single line conaining N integers representing
# one possible ordering in which the dinosaurs can be placed.
#
# Constraints
# 1≤T≤28
# 2≤N≤20
# 0≤K≤N−1
# Sample Input:
# 1
# 5 2
# Sample Output:
# 2 3 1 5 4

n = int(input("N:"))
# k = int(input("K:"))
#
team_list = []
# for i in range(0,n):
#     team_list = i+1
#
# team_list[]
points = 0
for i in range(0,n):
    team_list.append(int(input("number:")))

bigger = team_list[0]
for i in range(1,n):
    if bigger < team_list[i]:
        bigger = team_list[i]
    else:
        points += 1

print(points)