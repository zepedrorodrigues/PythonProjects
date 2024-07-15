number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

number_grid1 = []

for row in number_grid:
    for x in row:
        number_grid1.append(x)
number_grid1.sort()
print(number_grid1)




