'''lst = list(map(int, input().split()))
n = int(input())

min_index = lst.index(min(lst))
lst1 = lst[min_index:] + lst[:min_index]

i = 0
j = len(lst1) - 1
while i <= j:
    if lst1[i] + lst1[j] == n:
        print(True)
        break
    elif lst1[i] + lst1[j] < n:
        i += 1
    else:
        j -= 1
else:
    print(False)'''


'''lst = list(map(int, input().split()))
n = int(input())

min_idx  = 0
for i in range(len(lst) - 1):
    if lst[i] > lst[i + 1]:
        min_idx = i
        break'''

