'''
Seating Arrangement
https://goo.gl/S2Z7ab
'''

all_seats = list(range(1, 109))
left = [1, 2, 3]
right = []

var = 1
pos = 3

while len(left) + len(right) != len(all_seats):
    if var == 0:
        left += all_seats[pos:pos+6]
        var = 1
        pos += 6

    elif var == 1:
        right += all_seats[pos:pos+6]

        var = 0
        pos += 6

ws_left = []
ws_right = []

ms_left = []
ms_right = []

as_left = []
as_right = []

l = 0
r = 0

while (len(ws_left) + len(ms_left) + len(as_left)) != len(left):

    if l % 2 == 0:
        ws_left.append(left[l])
        ms_left.append(left[l + 1])
        as_left.append(left[l + 2])

    else:
        ws_left.append(left[l + 2])
        ms_left.append(left[l + 1])
        as_left.append(left[l])

    l += 3

while (len(ws_right) + len(ms_right) + len(as_right)) != len(right):

    if r % 2 == 0:
        as_right.append(right[r])
        ms_right.append(right[r + 1])
        ws_right.append(right[r + 2])

    else:
        as_right.append(right[r + 2])
        ms_right.append(right[r + 1])
        ws_right.append(right[r])

    r += 3

inp = int(input())

for i in range(inp):

    number = int(input())

    if number in left:

        if number in ws_left:
            num_pos = [x for x, y in enumerate(ws_left) if ws_left[x] == number][0]

            if number % 2 != 0:
                print(ws_left[num_pos+1], 'WS')

            else:
                print(ws_left[num_pos - 1], 'WS')

        elif number in ms_left:
            num_pos = [x for x, y in enumerate(ms_left) if ms_left[x] == number][0]

            if number % 2 == 0:
                print(ms_left[num_pos + 1], 'MS')

            else:
                print(ms_left[num_pos - 1], 'MS')

        elif number in as_left:
            num_pos = [x for x, y in enumerate(as_left) if as_left[x] == number][0]

            if number % 2 != 0:
                print(as_left[num_pos + 1], 'AS')

            else:
                print(as_left[num_pos - 1], 'AS')

    elif number in right:
        if number in ws_right:

            num_pos = [x for x, y in enumerate(ws_right) if ws_right[x] == number][0]

            if number % 2 == 0:
                print(ws_right[num_pos+1], 'WS')

            else:
                print(ws_right[num_pos - 1], 'WS')

        elif number in ms_right:
            num_pos = [x for x, y in enumerate(ms_right) if ms_right[x] == number][0]

            if number % 2 != 0:
                print(ms_right[num_pos + 1], 'MS')

            else:
                print(ms_right[num_pos - 1], 'MS')

        elif number in as_right:
            num_pos = [x for x, y in enumerate(as_right) if as_right[x] == number][0]

            if number % 2 == 0:
                print(as_right[num_pos + 1], 'AS')

            else:
                print(as_right[num_pos - 1], 'AS')
