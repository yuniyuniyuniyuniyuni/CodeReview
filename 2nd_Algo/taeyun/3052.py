remainder_set = set()

for _ in range(10):
    num = int(input())
    remainder_set.add(num % 42)

print(len(remainder_set))
