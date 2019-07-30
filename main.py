import random

havingMoney = 10000
bet = 1000
probability = 0.5
applyRate = 2
maxLoop = 100

loopCt = 0
result = 0

nowBetting = bet

f = open('result.txt', 'w')

f.write('ゲーム数,bet数,勝ち負け,持っているお金\n')

while loopCt < maxLoop and havingMoney > 0:

    loopCt += 1

    winGame = True

    if random.random() < probability:
        winGame = False

    if winGame:
        havingMoney = havingMoney + nowBetting
    else:
        havingMoney = havingMoney - nowBetting

    f.write(str(loopCt))
    f.write(',')
    f.write(str(nowBetting))
    f.write(',')
    if winGame:
        f.write('◯')
        nowBetting = bet
    else:
        f.write('×')
        nowBetting = nowBetting * applyRate
    f.write(',')
    f.write(str(havingMoney))
    f.write('\n')

    if havingMoney <= 0:
        f.write('破産しました\n')


f.close()



