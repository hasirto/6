for i in range(3):
    print("bir sayi giriniz")
    sayi=int(input())
    if sayi==0:
        pass
    elif sayi%2==0:
        print("girdiğin sayi pozitiftir")
    elif sayi<0:
        break