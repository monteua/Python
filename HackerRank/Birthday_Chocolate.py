
# my submission: https://www.hackerrank.com/challenges/the-birthday-bar/submissions/code/63509914
bar_count = input()
square_numbers = list(map(int, input().split(" ")))
d, m = input().split(" ")
'''
bar_count = 5
square_numbers = [1, 2, 1, 3, 2]
d, m = 3, 2
'''
posible_results = list()
for i in range(bar_count-m+1):
    posible_results.append(sum(square_numbers[i:i+m]))

print(posible_results.count(d))


