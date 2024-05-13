N = int(input())
subj = list(map(int, input().split()))
m = max(subj)

for i in range(N):
    subj[i] = subj[i]/m*100

print(sum(subj)/N)
