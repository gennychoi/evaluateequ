sum = 0
start = int(input('Please input the starting number: '))
end = int(input('Please input the ending number: '))
for i in range(start, end + 1):
    sum += 1.0 / i
    print('{:2d} {:6.4f}'.format(i, sum))