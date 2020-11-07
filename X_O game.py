
def insert (array,rows=int(),cols=int(),XO_choose = str()):

    rows = int(rows)
    cols = int(cols)
    rows= rows - 1
    cols-=1
    if array[rows][cols] == ' ':
        array[rows][cols] =XO_choose
    else:
        print(" This place is taken !! ")

def isWining (array):
    ad_kseb = False
    kolo_tmm = False
    for x in range(3):
        if array[x][0] == array[x][1] and array[x][1] == array[x][2] and array[x][2] !=' ':
            print(" The Winner is " + array[x][0])
            ad_kseb = True
            exit()
    for y in range(3):
        if array[0][y] == array[1][y] and array[1][y] == array[2][y] and array[2][y] !=' ':
            print(" The Winner is " + array[1][y])
            ad_kseb = True
            exit()
    if array[0][0] == array[1][1] and array[1][1] == array[2][2] and array[2][2] !=' ':
        ad_kseb = True
        print(" The Winner is " + array[1][1])
        exit()
    elif array[0][2] == array[1][1] and array[1][1] == array[2][0] and array[2][0] !=' ':
        ad_kseb = True
        print(" The Winner is " + array[1][1])
        exit()
    for g in range(3):
        for h in range(3):
            if array[g][h] == ' ':
                kolo_tmm= True
                break
    if ad_kseb == False and kolo_tmm == False:
        print(" Tie !! No One Wins !!! ")



index_X = int()
index_y = int()
x_ = True
array = [[' ',' ',' '],[' ', ' ', ' '],[' ',' ',' ']]
for j in range (9):
    index_X = input("Enter Row Number That you want to play in ")
    index_y = input("Enter colums Number That you want to play in ")
    if x_:
        insert(array,index_X,index_y,"X")
        x_ = False
    else:
        insert(array, index_X, index_y, "O")
        x_ = True
    isWining(array)
