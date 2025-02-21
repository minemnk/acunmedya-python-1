print("mine")
baslik = "Tasit kredisi"
print(baslik)
print("Tasit kredisi")
#string metinsel ifade
#int, integer => tam sayı
vade = 36
ekVade = 15
vade2 ="36"
#float ,decimal ,double
aylikOdeme = 200.50
#bool, boolean =>> True, false 

#matematiksel operatorler

print( vade + 12)
print(vade + ekVade)
print(5-5)
print(vade-10)
#*
print(5*5)
print(vade*5)

#/
print(10/2)
print(vade/2)
print(vade/ekVade)

yeniVade = vade / 2
fiyat = 100
yeniFiyat = fiyat - 20
print(yeniVade)
print(yeniFiyat)

# mod operator =>> % kalanı verir
print(10%2) 
print(vade %5)
print(vade % yeniVade)
print (vade% ekVade)
print(30%10)

# mantıksal operatorler
print(1==1) #true
print(1==2) #false

print(1>2)
print(3>1)
print(1>1)
print(1>=1)

print(1<2)
print(3<1)
print(1<1)
print(1<=1)

print(1!=1)
print(1!=2)

# or=>> veya
print(1>2 or 5>2)
#and=>> ve
print(1>2 and 5>2)
print(1>2 or 5>2 and 3>2) # 0 yada 1 >> 1   1 ve 1 =>> 1 true

print(1>2 and 5>2 and 3>2) # 0 ve 1 >> 0     0ve 1 >> 0 false

print(2>1 or 1>2 and 3>2) # 1 veya 0 >> 1    1 ve 1 >> 1 true

#karar yapıları
# if else if else yapıları

sayi1=15
sayi2= 15
# sayi1 sayi2 den büyükse ekrana sayi1 büyük yazdır
#condition

#indent
if sayi1 > sayi2 :
    print("sayi 1 sayi 2'den buyuktur") # boşluk ile if blogu içine alıyoruz
    print("Hala if bloğunun içerisindeyim" )
print("Burasi if bloğunun dişidir.") #bosluk ile if blogundan kopardık 

if sayi1 < sayi2 :
    print("sayi 1 sayi 2'den buyuktur") # boşluk ile if blogu içine alıyoruz
    print("Hala if bloğunun içerisindeyim" )
print("Burasi if bloğunun dişidir.") #true ve false durumuna bakmadan ifden ciktigi anda calistigi icin ekrana yazilacak.

#eger 
if sayi1 > sayi2 :
    print("sayi 1 sayi 2'den buyuktur")
    print("Hala if bloğunun içerisindeyim" )
#eger if bloguna girmez ise calissin istersek:
elif sayi1 == sayi2 :
    print("iki sayi esittir.")
# eger 2 durumada girmez ise
else :
   print("sayi1 sayi2den kücüktür.")

print("Burasi if bloğunun dişidir.") 






