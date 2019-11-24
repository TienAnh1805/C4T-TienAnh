# for i in range(5):
#     for j in range(5):
#         print(" * ", end="")
#     print()






# player = {
#     'i' : 2,
#     'j' : 0
# }
PlayerX = 3
PlayerY = 3
def printMap(side):
    for i in range(side):
        for j in range(side):
            # if i==player['i'] and j==player['j']:
            #     print(" P ", end = "")
            # else:
                # print(" * ", end = "")
            if i==PlayerY and j==PlayerX:
                print(" p ",end = "")
            else:
                print(" * ", end = "")
        print("")
printMap(7)

def run():
    global PlayerX,PlayerY
    move = input("Your move: ")
    print(move)
    if move == 'w':
        if PlayerY > 0:
            PlayerY -= 1
    if move == 's':
        if PlayerY < 6:
            PlayerY += 1
    if move == 'd':
        if PlayerX < 6:
            PlayerX += 1
    if move == 'a':
        if PlayerX > 0:
            PlayerX -= 1

while(True):
    printMap(7)
    run()



