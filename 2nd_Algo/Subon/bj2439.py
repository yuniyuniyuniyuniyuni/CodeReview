N = int(input())

for a in range(N):
    b = a+1
    print(' '*(N-b), end='')
    print('*'*b)
