import random
sayi=random.randint(1,10)
tahmin=int(input("1 ile 10 arasında tahmin et: "))
if(tahmin==sayi):
    print("tebrikler bildiniz.")
else:
    print("maalesef bilemediniz.",sayi)
