print("1.")
a="ali"
b="veli"
c="hasan"
d="ayşe"
print(a,b,c,d)
print(a,b,c,d, sep="")
print(a,b,c,d, sep=" ")
print("2.")
gun=16
ay=12
yıl=2019
print(gun,ay,yıl)
print(gun,ay,yıl, sep=".")
print("3.")
print("bir","iki","üç","dört", sep=" mumdur ")
print("bir","iki","üç","dört", sep=" mumdur ", end=" mumdur ")
print("4.")
print("birinci satır","ikinci satır","üçüncü satır", sep="\n")
print("5.")
print(1,2,3,4,5, sep="-")
print(1,2,3,4,5,sep="0")#integer değer "sep" e gelmez.
print("6.")
print("su 100 derecede kaynar", end=".") #end="\n"
print("merhaba")
print("7.")
print(*"galatasaray", sep=".")
print("g","a","l","a","t","a","s","a","r","a","y")
print("8. virgül yerine .format kullanmak")
a=10
b=90
print("a'nın değeri",a,"b'nin değeri",b,"dir")

print("a'nın değeri {}dir. b'nin değeri {}dir".format(a,b))


