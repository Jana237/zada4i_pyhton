# задача 1
a = input().split()
for i in range(0, len(a), 2):
    print(a[i])
   
# Задача 2
s=input()
a=[int(s) for s in s.split()]
for i in a:
    if int(i)%2 == 0:
       print(i, end=' ')

#Задача 3
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])
       
# Задача 4
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break

# Задача 5
a = [int(i) for i in input().split()]
counter = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        counter += 1
print(counter)

# Задача 6
index_of_max = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
print(a[index_of_max], index_of_max)

# Задача 7
a = [int(i) for i in input().split()]
x = int(input())
pos = 0
while pos < len(a) and a[pos] >= x:
    pos += 1
print(pos + 1)

# Задача 8
a = input().split()
sum_index = 0
for i in range(0, len(a) - 1):
    if int(a[i]) != int(a[i + 1]):
        sum_index += 1
print(sum_index + 1)

# Задача 9
a = [int(i) for i in input().split()]
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))

# Задача 10
a = [int(i) for i in input().split()]
min_index = a.index(min(a))
max_index = a.index(max(a))
[a[max_index], a[min_index]] = [a[min_index], a[max_index]]
print(' '.join([str(i) for i in a]))

# Задача 11
a = [int(s) for s in input().split()]
k = int(input())
for i in range(k + 1, len(a)):
    a[i - 1] = a[i]
a.pop()
print(' '.join([str(i) for i in a]))

# Задача 12
a = [int(s) for s in input().split()]
k, C = [int(s) for s in input().split()]
a.append(0)
for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k] = C
print(' '.join([str(i) for i in a]))

# Задача 13
a = [int(s) for s in input().split()]
counter = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            counter += 1
print(counter)

# Задача 14
a = [int(s) for s in input().split()]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end=' ')

# Задача 15
n, k = [int(s) for s in input().split()]
bahn = ['I'] * n
for i in range(k):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        bahn[j] = '.'
print(''.join(bahn))

#Задача 16
n = 8
x = []
y = []
for i in range(n):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)
 
correct = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False
 
if correct:
    print('NO')
else:
    print('YES')
