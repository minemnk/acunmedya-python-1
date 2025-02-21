
# sınıflar =>> classlar
# modules
# paket yönetimi
# self=>> this  zorunlu degil ama bir parametre alınmalı.

def sayHello():
    print("Hello!")
class Human : 

   # built-in
   #constructor
   
   def __init__(self,name):
      self.name = name
      print("Bir Human instance'i üretildi")
  
   def __str__(self):
      return f"STR Fonksiyonundan dönen deger : {self.name}"
   
    
   def talk(self,sentence): 
      #print(f"Human: {sentence}")
      print(f"{self.name}: {sentence}")
   def walk(self) :
      #print("Human is walking..")
      print(f"{self.name} is walking")

# instance = >> örnek 

human1 = Human("Enes")
#human1.name = ("Enes")
human1.talk("Merhaba")
human1.walk()



human2 = Human("cem")
#human2.name="Cem"
human2.talk("Selam")
human2.walk()




#packages

