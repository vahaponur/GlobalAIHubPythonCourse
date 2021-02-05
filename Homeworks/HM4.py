#GlobalAIHub HM4
#Defining animals and defining functions inherit
class Animals():
    def __init__(self,name,familia,rep_type):
        self.name=name
        self.familia=familia
        self.rep_type=rep_type
    def define_animal(self):
        print(self.name+" belongs to "+self.familia+" family.")
    def reproductiontype (self):
        print(self.name+"'s reproduction type is "+self.rep_type)
animal=Animals("Snakes","Typhlopidae","Eggs")
animal.define_animal()

class Dogs():
    def __init__(self,name,typeof,color,lifetime):
        self.name=name
        self.typeof=typeof
        self.color=color
        self.lifetime=lifetime
    def infodog(self):
     print(self.name+"''s color:  "+self.color)
     print(self.name+"'s lifetime:  "+self.lifetime)
     print(self.name+"''s type is:  "+self.typeof)

dogs=Dogs("Palpatine","Siberian Husky","Black and White","11 Year")
dogs.infodog()

class Cats():
    def __init__(self,name,typeof,color,lifetime):
        self.name=name
        self.typeof=typeof
        self.color=color
        self.lifetime=lifetime
    def infocat(self):
     print(self.name+"''s color:  "+self.color)
     print(self.name+"'s lifetime:  "+self.lifetime)
     print(self.name+"''s type is:  "+self.typeof)

cats=Cats("Nisan","Turkish Agnora","White","5 Year")
cats.infocat()
    
    
