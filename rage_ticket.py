import random

oran = 0
for e in range(1, 100):
    won = 0
    for a in range(1,100):
        for i in range(1,301):
            a = random.randint(1,6001)
            if (a == 1979 or a == 1980):
                won = won + 1
                break
    print("kazanma oranı: %", won)
    oran = oran + won
print("ortalama oran", oran/100)