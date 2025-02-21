faiz = 1.59
vade = "36"
krediAdi = "ihtiyac kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade)+12) # basina int koyarak onu metinsel ifadeden integere ceviriyoruz.
#print(int(krediAdi)) hata verir.
faiz = str(faiz)
print(type(faiz))

#vade = int(input("Lutfen istediginiz vade sayisini girin : ")) # 14. satirda int koyarak ve 17. satirda print(int(vade)+12) yapmak aynı islem
vade = 36 
print(vade)
print(type(vade))
print((vade)+12)
vade = vade + 12

# string interpolation
# sectiginiz vade sonucu ortaya cikan vade
print("sectiginiz vade sonucu ortaya cikan vade : " + str(vade))
print("sectiginiz vade sonucu ortaya cikan vade: {vadeSayisi}".format(vadeSayisi=vade))

isim = "Mine"
metin ="merhaba {name}".format(name= isim)
print(metin)

# f-string
metin = f"Hosgeldiniz {1+1}"
print(metin)

#listeler
#döngüler
# fonksiyonlar

krediler = [ "ihtiyac kredisi ", "Tasit kredisi", "Konut kredisi"]
print(type(krediler))

print(krediler)
print(krediler[0]) #0 a denk gelen 'ihtiyac kredisi' yazdırır
#print(krediler[3])  hata verir =>> lengt-1

dizi = ["ihtiyac kredisi", 10,5.2, True]
print(dizi)

#tanimlandiktan sonra eleman eklemek istedigimizde son elemana ekler
krediler.append("özel kredi")
print(krediler)

krediler.pop() #icine index yazmazsan en son elemanı siler
print(krediler) 

krediler.pop(0) # 0. indexdeki  elemanı siler
print(krediler) 

krediler.remove("Tasit kredisi") #ilk gördügü tasit kredisini siler
print(krediler)

krediler.extend(["Y kredisi","Z kredisi"]) # ikiside diziye eklendi
print(krediler) 

#for
# i = 0 i<10

for i in range(10) :
   print("xx")
   print(i) 
for i in range(5,10): #döngüyü 5 ile baslatmıs olduk
   print(i)

print("************")
for i in range(0,10):
   print(i)

print("*************")
for i in range(0,51,10): #0 ile 51 arasında 10 artırarak döndür
  print(i) 

krediler = ["ihtiyac kredisi", "Tasit kredisi","Konut kredisi"]
for kredi in krediler:
   print(kredi)
print("**************")
for i in range(len(krediler)):
   print(krediler[i])


#sonsuz  döngü olmaması icin
i = 0
while i <10 :
   print("x")
   i+=1
print("y")

print("***********")
krediler = ["İhtiyac kredisi","tasit kredisi", "konut kredisi"]
i=0
while i< len(krediler):
   i+=1 
   print(i)
   print(krediler[i])
   if krediler[i]=="konut kredisi":
    break

# fonksiyonlar
fiyat = 100
indirim = 20

#yeniFiyat = fiyat - indirim buradaki islemi fonksiyon hale getiricez
#defination define
def calculate():
   print(100-20)

def calculateWithParams(fiyat,indirim):
   print(fiyat-indirim)
def sayHello(name):
   print(f"Merhaba {name}")
calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Mine")

#void
def calculateAndReturn(price, discount):
   return price-indirim

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat +10)


print("*****************************")







