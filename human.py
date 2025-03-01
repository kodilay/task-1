
class Human:
    name = "Ali"

    def __init__(self,name):
        self.name = name 
        print("Bir insan örneği üretildi.")
    def talk(self,sentence):
        print(f"{self.name}:{sentence}")
    def walk(self):
        print(f"{self.name} is walking..")

human1=Human("Veli")

human1.talk("Merhaba")
human1.walk()

            
human2=Human("Mahumut")

human2.talk("Selam")
human2.walk()
print(human2)

Human("Ayşe").talk("Merhaba")
