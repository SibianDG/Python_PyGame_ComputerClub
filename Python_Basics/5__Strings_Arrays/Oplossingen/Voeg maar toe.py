arr = []
number = input()
while number != "stop":
    arr.append(int(number))
    number = input()
for index in range(len(arr)):
    if index == 0:
        print(index, ":", arr[index], end='')
    else:
        print(",", index, ":", arr[index], end='')

