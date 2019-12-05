# Lucy had recently learned the game, called Natural Numbers.
# The rules of the game are really simple. There are N players. At the same time, every player says one natural number.
# Let's call the number said by the i-th player Ai. The person with the smallest unique number
# (that is, the smallest number that was not said by anybody else) wins.
# Sometimes, there is a case when there are no unique numbers at all. Then the game is obviously a draw, so nobody wins it.
# Sometimes, it's hard to determine the winner, especially, when the number of players is enormous.
# So in this problem, your assignment will be: given the names of the players and the numbers every of them have said.
# Please, tell the name of the winner, or determine that nobody wins.
# Input
# The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
# The first line of every test case consists of a single integer N - the number of players.
# Then, N lines will follow. Each of these N lines will consist of the player's name and the number Ai said by her,
# separated by a single space.
# Output
# For each test case, output a single line containing an answer to the corresponding test case - the name of the winner,
# or a string "Nobody wins.", if nobody wins the game.
# Example
# Input:
# 2
# 5
# Kouta 1
# Yuka 1
# Mayu 3
# Lucy 2
# Nana 5
# 2
# Lucy 2
# Nana 2
# Output:
# Lucy
# Nobody wins.

test = int(input())
for t in range(0,test):
    # print("\ntest ", test)
    no_of_inputs = int(input())
    # print("No of inputs:", no_of_inputs)
    score_list = [[]]
    score_list_dup = []
    lowest_unique_number = 0
    unique_numbers = []
    for i in range(no_of_inputs):
        string = input()
        string_list = []
        string = string.split(" ")
        string_list.append(string[0])
        string_list.append(int(string[1]))
        # print("String list :", string_list)
        score_list.append(string_list)
    score_list.pop(0)
    # print("Score list : ", score_list)
    score_list_dup = score_list
    for i in range(no_of_inputs):
        flag = 0
        if score_list_dup[i][1] == 'a':
            continue
        for j in range(i + 1, no_of_inputs):
            if score_list_dup[j][1] == 'a':
                continue
            if score_list_dup[i][1] == score_list_dup[j][1]:
                flag = 1
                score_list_dup[j][1] = 'a'

        if flag == 0:
            unique_numbers.append(score_list_dup[i][1])
        else:
            score_list_dup[i][1] = 'a'

    # print("Uniqye : ", unique_numbers)
    if unique_numbers.__len__() == 0:
        print("Nobody wins.")
        continue
    smallest_unique_number = min(unique_numbers)
    for i in range(no_of_inputs):
        if score_list[i][1] == smallest_unique_number:
            print(score_list[i][0])




