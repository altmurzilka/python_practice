a = int(input())
count = 0
for i in range(1, a):
  if a%i == 0:
    count = count + i
print(count+a)
