faiz = 1.59
vade = 36
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade)+12)

faiz = str(faiz)
print(type(faiz))

vade = int(input("Lütfen istediğiniz vade sayısnı girniz:"))
print(type(vade))
vade = vade + 12


print("Seçtiğiniz vade sonucu ortaya çıkan vade: "+ str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade:{vadeSayisi}".format(vadeSayisi=vade))

isim = "Azra"
metin = "Merhaba {name}".format(name=isim)
print(metin)


metin = f"Hosgeldiniz {1+1}"
print(metin)
 
#listeler
#dongüler
#fonksiyonlar

krediler = ["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler)) 

krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)

krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend(["Y kredisi","Z kredisi"])
print(krediler)


for i in range(10):
    print("xx")
    print(i)
print("************")
for i in range(5,11):
    print(i)
print("************")   

for i in range(0,51,10):
    print(i)
print("************")  

krediler=["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
for kredi in krediler:
    print(kredi)
print("************")  
for i in range(len(krediler)):
    print(krediler[i])

# infinite loop
i=0
while i<10:
    print("a")
    i+=1
print("b")

print("****************")

while True:
    print("A")
    break
print("*************** Son Döngü **************")

krediler=["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
i=0
while i< len(krediler):
    i+=1
    print(i)
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break


fiyat=100
indirim=20

def calculate():
    print(100-20)
    
def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)
    
def sayHello(name):
    print(f"Merhaba {name}")
    
calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)

sayHello("Ali")
sayHello("Veli")
sayHello("Mehmet")

def calculateAndReturn(fiyat,indirim):
    return fiyat-indirim

yeniFiyat=calculateAndReturn(300,200)
print(yeniFiyat+10)
#void
def calculatePrice(price,discount):
    print(price-discount)

def calculatePriceAndReturn(price,discount):
    return price-discount

print("**************")
fonk1 = calculatePrice(100,50)
fonk2 = calculatePriceAndReturn(300,100)

print(f"159.satır:{fonk1}")
print(f"160.satır:{fonk2}")

print("*****************")
