first_col = []
second_col = []
with open("./day1/input.txt", "r") as file:
   for line in file:
        num1, num2 = map(int, line.split())

        first_col.append(num1)
        second_col.append(num2)
    
first_col.sort()
second_col.sort()


anothertemp = 0
for i in range(len(first_col)):
    anothertemp += abs(first_col[i] - second_col[i])

print(anothertemp)

count_map = {}

for num in second_col:
    count_map[num] = count_map.get(num, 0) + 1


result = [num * count_map.get(num, 0) for num in first_col]

total = sum(result)

print(total)