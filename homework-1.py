import copy
import random

#--task 1--#
def hello(arg):
    print("Hello " + arg)
#--task 2--#
def sum(arr):
    res = 0
    for item in arr:
        res += item

def multiply(arr):
    res = 1
    for item in arr:
        res *= item
#--task 3--#
def reverse(string):
    res = ""
    for i in range (len(string) - 1, -1, -1):
        res += string[i]
    return res

#--task 4--#
def isPalindrome(string):
    return (string == ''.join(reversed(string)))

#--task 5--#
def histogram(a):
    for i in a:
        print("*" * i)
        
#--task 6--#
def caesarCipher(string, number):
    res = ""
    max_num = 90
    for i in range(len(string)):
        res += str ( chr ( ( ord ( string[i] ))  + number ) )
    return res

#--task 7--#
def diagonalReverse(a):
    res = copy.deepcopy(a)
    for i in range(len(a)):
        for j in range(len(a)):
            res[i][j] = a[j][i]

    return res

#--task 8--#
def game(begin, end):
    num = random.randint(begin, end)
    a = int(input())
    while (a != num):
        print("Please, try again!")
        a = int(input())
    print("Congratulations, you've won!")

#--task 9--#
def check_par_correctness(s):
    res = []
    for i in s:
        if (i == "["):
            res.append(i)
        else:
            res.pop()

    return len(res) == 0    

#--task 10--#
def charFreq(s):
    res = {}
    for char in s:
        if char in res:
            res[char] += 1
        else:
            res[char] = 1
    return res

#--task 11--#
def decToBin(a):
    res = ""
    while a >= 1:
        res += str(int(a%2))
        a = int(a)
        a/=2
    return ''.join(reversed(res))

#--task 12--#
import random

def initializeShipGame():
    print("Please enter enter the order of matrix you wanna play: ")
    order = int(input())
    if (order == "exit"):
        return
    
    fieldAI = []
    fieldUser = []
    isFiredAI = []
    isFiredUser = []

    for i in range(order):
        fieldUser.append([None]*order)
        fieldAI.append([None]*order)
        isFiredAI.append([None]*order)
        isFiredUser.append([None]*order)

    print(len(fieldUser))
    print(len(fieldUser[0]))

    for i in range(order):
        for j in range (order):
            fieldAI[i][j] = False
            fieldUser[i][j] = False
            isFiredAI[i][j] = False
            isFiredUser[i][j] = False


    shipsAI = []
    shipsUser = []

    for i in range(order + int(order/2)):
        shipsAI.append(random.randint(0, order**2 - 1))
        shipsUser.append(random.randint(0,order**2 - 1))

    for pos in shipsAI:
        fieldAI[int(pos/order)][pos%order] = True

    for pos in shipsUser:
        fieldUser[int(pos/order)][pos%order] = True
        
    visualize(fieldUser, fieldAI, order, isFiredUser, isFiredAI)

    shipGame(fieldUser, fieldAI, order, isFiredUser, isFiredAI)


def visualize(fieldUser, fieldAI, order, isFiredUser, isFiredAI):
    print ("your field\n")
    for i in range(order):
        for j in range(order):
            if (not fieldUser[i][j] and not isFiredUser[i][j]):
                print('~', end = "")
            if (not fieldUser[i][j] and isFiredUser[i][j]):
                print ('O', end = "")
            if (fieldUser[i][j] and not isFiredUser[i][j]):
                print('|', end = "")
            if (fieldUser[i][j] and isFiredUser[i][j]):
                print('X', end = "")
        print("\n")
    print ("opponents field\n")
    for i in range(order):
        for j in range (order):
            if (not isFiredAI[i][j]):
                print('~', end = "")
            if (not fieldAI[i][j] and isFiredAI[i][j]):
                print ('O', end = "")
            if (fieldAI[i][j] and isFiredAI[i][j]):
                print('X', end = "")
        print("\n")


def shipGame(fieldUser, fieldAI, order, isFiredUser, isFiredAI):
    while True:
        print ("Please, tell me where you want to shoot. Type \"exit\" to leave")
        x = input()
        if (x == "exit"):
            break
        x = int(x)
        y = input()
        if (y == "exit"):
            break
        y = int(y)

        while(isFiredAI[x][y]):
            print("Sorry, you've already fired there. Please type in new coordinates:")
            x  = int(input())
            y = int(input())

        isFiredAI[x][y] = True
        if (fieldAI[x][y]):
            fieldAI[x][y] = False

        AIx = random.randint(0, order - 1)
        AIy = random.randint(0, order - 1)

        while(isFiredUser[AIx][AIy]):
            AIx = random.randint(0, order - 1)
            AIy = random.randint(0, order - 1)

        isFiredUser[AIx][AIy] = True

        if (fieldUser[AIx][AIy]):
            fieldUser[AIx][AIy] = False

        visualize(fieldUser, fieldAI, order, isFiredUser, isFiredAI)

        if (checkAIWinner(fieldUser)):
            print("AI is winner")
            break
        
        if (checkUserWinner(fieldAI)):
            print("User of winner")
            break
        

        

def checkAIWinner(fieldUser):
    for i in range(len(fieldUser)):
        for j in range(len(fieldUser)):
             if (fieldUser[i][j] == True):
                 return False
    return True

def checkUserWinner(fieldAI):
    for i in range(len(fieldAI)):
        for j in range(len(fieldAI)):
             if (fieldAI[i][j] == True):
                 return False
    return True
