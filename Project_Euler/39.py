'''
Integer right triangles
Problem 39
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions
for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

# pretty slow solution, but it works.
p_max = 0
solutions = 0

# starting from 500
for i in range(1000//4*2, 1001, 2):
    count = 0
    for a in range(2, int(i)+1):
        for b in range(2, a + 1):
            c = i - a - b
            if c > 0:
                if a**2 + b**2 == c **2:
                    count += 1
    if count > solutions:
        p_max = i
        solutions = count
print(solutions)
print("P:",p_max)
