from  random import randint
def ugaday_izi_znachenii():
    value = "0123456789"#value - значение
    q = 4#количество чисел в пароле
    x = len(value)#
    i = 0#это у нас что?

    #while True:
    while i < 1000000000:
        result = ""
        temp = i#temp -
        while temp > 0:
            r = temp % x# % - остаток от деления
            result = value[r] + result#
            temp = temp // x # целочислиное деление 
        while len(result) < q:
            result = "0" + result
        print(result)
        i = i + 1


    print(result)

def ugaday():
    lap = ""
    poputka = 0
    while lap != pin:
        for i in range(4):
            lap = lap + str(randint(0, 9))
        if lap != pin:
            poputka = poputka + 1
            lap = ""
    print(poputka)

pin = ""
for i in range(4):
    pin = pin + str(randint(0,9))

print(pin)

with open("pin.txt","w") as file_txt:
    file_txt.write(pin)
ugaday()
ugaday_izi_znachenii()