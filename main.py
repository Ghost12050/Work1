import random

max_lines = 3 
max_bet =100
min_bet =1

ROWS = 3
COLS = 3

syms_count = {
    "A":10,
    "B":10,
    "C":10,
    "D":10
}

sys_value = {
    "A":6,
    "B":4,
    "C":3,
    "D":2
}

def checkwin(columns, lines, bet, values):
    win = 0
    winlines = {}
    for line in range(lines):
        sym = columns[0][line]
        for col in columns:
            symcheck = col[line]
            if sym != symcheck:
                break
        else:
            win += values[sym]*bet
            
            (line + 1)
    return win, winlines


def slotspin(rows,cols,symbols):
    allsyms=[]
    for sym,syms_count in symbols.items():
        for _ in range(syms_count):
            allsyms.append(sym)
    
    columns = []
    for _ in range(cols):
        colum = []
        cursym = allsyms[:]
        for _ in range(rows):
            value = random.choice(cursym)
            cursym.remove(value)
            colum.append(value)

        columns.append(colum)

    return columns

def printslot(colums):
    for row in range(len(colums[0])):
        for i,colum in enumerate(colums):
            if i != len(colums) -1:
                print(colum[row], end=" | ")
            else:
                print(colum[row],end="")
        print()

def deposit():
    while True:
        amount = input("ใส่เงินทั้งหมดของคุณ :")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("ตัวเลขต้องมากกว่า0")
        else:
            print("ใส่เงินของคุณใหม่0")
    return amount

def getlines():    
    while True:
        lines = input("ใส่แถวที่อยากพนัน (1-" + str(max_lines) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines<=max_lines:
                break
            else:
                print("ตัวเลขต้องมากกว่า0")
        else:
            print("เลือกใหม่")
    return lines

def getbet():    
    while True:
        amount = input("ใส่เงินที่คุณอยากพนันในแต่ล่ะแถว :")
        if amount.isdigit():
            amount = int(amount)
            if min_bet<= amount<=max_bet:
                break
            else:
                a=str(min_bet)
                b=str(max_bet)
                print("ตัวเลขต้องอยู่ระหว่าง"+a+"-"+b)
        else:
            print("ใส่เงินของคุณใหม่20")
    return amount

def game(balance):
    lines=getlines()
    while True:
        bet = getbet()
        allbet = bet*lines

        if allbet>balance:
            print(f"เงินของคุณมีไม่พอ ตอนนี้คุณมี {balance}")
        else:
            break
     
    print (f"คุณกำลังพนัน{lines}กับแถว จำนวนเงินทั้งหมด :{allbet}")

    slots = slotspin(ROWS,COLS,syms_count)
    printslot(slots)
    win, winlines = checkwin(slots, lines, bet , sys_value)
    print(f"คุณได้{win}")
    print(f"คุณชนะกับแถว :",*winlines)
    a=int(allbet)
    return win - allbet

def main():
    balance = deposit()
    while True:
        print(f"ตอนนี้คุณมีเงิน{balance}")
        spin = input("กดEnterเพื่อเล่น(กดqเพื่อออกจากเกม)")
        if spin == "q":
            break
        balance+=game(balance)
    print(f"เงินทั้งหมดของคุณคือ{balance}")\
    
main()