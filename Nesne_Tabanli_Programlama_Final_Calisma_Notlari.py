from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    
    def Walk():
        pass
    
    @abstractmethod
    def Run():
        pass

    
class Bird(Animal):
    
    def __init__(self):
        
        print("Bird Sinifinin Yapici methodu Calisti.")

    def Walk(self):
        
        print("walk")
    
    def Run(self):
        
        print("run")
    

a1 = Bird()

a1.Run()

a1.Walk()


#%%

class Personel:
    
    def Walk(self):
        
        print("walk from Personel")
    
    def Run(self):
        
        print("run from Personel")
        
class Ogretim_Gorevlisi(Personel):
    
    def Walk(self):
        
        print("walk from Ogretim Gorevlisi")
    
    def Run(self):
        
        print("run from Ogretim Gorevlisi")
        
        
        
b1 = Personel()

b1.Walk()

c1 = Ogretim_Gorevlisi()

c1.Walk()

#%%

print(isinstance(5,int))

print(isinstance(5.0,int))

print(isinstance(True,object)) # True degeri bir objemidir diye soruyoruz

print(isinstance(False,object)) # False degeri bir objemidir diye soruyoruz

#%%

class A():
    
    def __init__(self):
        
        print("A constructor")
        
        
    def metot1(self):
        print("E metot 1")


class B(A):
    
    def __init__(self):
        
        super().__init__()
        
        print("B constructor")
        
        
    def metot1(self):
        print("E metot 1")


class C(B):
    
    def __init__(self):
        
        super().__init__()
        
        print("C constructor")
        
        
    def metot1(self):
        print("E metot 1")


class D(C):
    
    def __init__(self):
        
        super().__init__()
        
        print("D constructor")
        
# init metodu otomatik olarak çalışır

    def metot1(self):
        
        print("D metot 1")
        
        
    def metot2(self):
        
        print("D metot 2")
        
        
class E(D):
    
    def __init__(self):
        
        super().__init__()
        print("E constructor")
        
        
    def metot1(self):
        print("E metot 1")


objE = E()































