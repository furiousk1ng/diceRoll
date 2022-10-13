import random
min = 1
max = 6
kol_cube = int(input("Количество кубиков: "))
roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    i=0
    print ("Бросаем кубики...")
    while i < kol_cube:
        print( "Выпало....")
        print (random.randint(min, max))
        i+=1

    roll_again = input("Бросаем еще раз? ")
    kol_cube = int(input("Количество кубиков: "))