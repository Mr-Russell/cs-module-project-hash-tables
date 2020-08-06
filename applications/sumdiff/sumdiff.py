"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

q1 = set(range(1, 10))
q2 = set(range(1, 200))
q3 = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

def sumdiff(l):
    f_of_x = {}
    addition = {}
    subtraction = {}
    output = []

    def f(x):
        return x * 4 + 6

    for a in l:
        for b in l:
            if a not in f_of_x:
                f_of_x[a] = f(a)

            if b not in f_of_x:
                f_of_x[b] = f(b)
            
            plus = f_of_x[a] + f_of_x[b]
            minus = f_of_x[a] - f_of_x[b]
            
            if plus not in addition:
                addition[plus] = []
            
            addition[plus].append((f'f({a}) + f({b})', f'{f_of_x[a]} + {f_of_x[b]}')) 
            
            if minus not in subtraction:
                subtraction[minus] = []

            subtraction[minus].append((f'f({a}) - f({b})', f'{f_of_x[a]} - {f_of_x[b]}'))


    for c in addition:
        for d in subtraction:
            
            if c == d:
                for e in addition[c]:
                    for f in subtraction[d]:
                        output.append((f'{e[0]} = {f[0]}', f'{e[1]} = {f[1]}'))

    
    for i in output:
        print(f'{i[0]}\t{i[1]}')


    # print("===== f_of_x =====")
    # for i in f_of_x:
    #     print(f'{i:3}: {f_of_x[i]}')
    # print()
    # print("===== addition =====")
    # for i in addition:
    #     print(f'{i:4}: {addition[i]}')
    # print()
    # print("===== subtraction =====")
    # for i in subtraction:
    #     print(f'{i:4}: {subtraction[i]}')

# print("========== q1 ==========")
# sumdiff(q1)
# print()
# print()
# print("========== q2 ==========")
# sumdiff(q2)
# print()
# print()
print("========== q3 ==========")
sumdiff(q3)
