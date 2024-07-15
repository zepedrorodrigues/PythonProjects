import random
square_initial = [[random.choice(range(1,10)) for x in range(9)] for y in range(9)]

def find_square(row,column):
    a = range(3);b=range(3,6);c=range(6,9)
    if row in a:
        if column in a:
            return 1
        if column in b:
            return 2
        if column in c:
            return 3
    elif row in b:
        if column in a:
            return 4
        elif column in b:
            return 5
        elif column in c:
            return 6
    elif row in c:
        if column in a:
            return 7
        elif column in b:
            return 8
        elif column in c:
            return 9

def check_row(value,row,whole_square):
    line = whole_square[row]
    check = [item for item in line if item == value]
    if len(check)>1:
        return False
    else:
        return True
    
def check_column(value,column,whole_square):
    column = [item[column] for item in whole_square]
    check = [item for item in column if item==value]
    if len(check)>1:
        return False
    else:
        return True

def all_checks(value,row,column,square,whole_square):
    if check_column(value,column,whole_square)==True and check_row(value,row,whole_square)==True:
        return True
    else:
        return False


    
 