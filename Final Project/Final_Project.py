#GlobalAIHub Final Project
"""
Managers: Vahap Onur YILDIRIM 23 Turkish English German
                  Alaattin Ahmet DİRİ 25 Turkish
                  İrem Eylül GÖBEL 22 Turkish Spanish
Employees: Ayşe İÇÖZ 25 Turkish Spanish
                    John DUGGAN 30 English
                    Hideo KOJIMA 45 English Japanese
                    Marcin Przybylowicz 35 Polish
"""
                    
#employee class written and languages of a person taken as a list         
class employees():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.languages=[]
    def entlang(self,lang):
        self.languages.append(lang)
    def printl(self):
        return(self.languages)
liste=[] #langua list of employees,managers will be added below
Ayse=employees("Ayse ICOZ",25)
Ayse.entlang("Turkish")
Ayse.entlang("English")
a=Ayse.printl()
for i in a:
    if i not in liste:
        liste.append(i)
    else:
        continue
John=employees("John DUGGAN",30)
John.entlang("English")
b=John.printl()
for i in b:
    if i not in liste:
        liste.append(i)
    else:
        continue
Hideo=employees("Hideo KOJIMA",25)
Hideo.entlang("Japanese")
Hideo.entlang("English")
c=Hideo.printl()
for i in c:
    if i not in liste:
        liste.append(i)
    else:
        continue
Marcin=employees("Marcin PRZYBYLOWICZ",35)
Marcin.entlang("Polish")
d=Marcin.printl()
for i in d:
    if i not in liste:
        liste.append(i)
    else:
        continue
    
class managers():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.languages=[]
    def entlang(self,lang):
        self.languages.append(lang)
    def printl(self):
        return(self.languages)
Vahap=managers("Vahap Onur YILDIRIM",25)
Vahap.entlang("Turkish")
Vahap.entlang("English")
Vahap.entlang("German")
a=Vahap.printl()
for i in a:
    if i not in liste:
        liste.append(i)
    else:
        continue
alaattin=managers("Alaattin Ahmet DIRI",25)
alaattin.entlang("Turkish")
b=alaattin.printl()
for i in b:
    if i not in liste:
        liste.append(i)
    else:
        continue
eylul=managers("Irem Eylul GOBEL",25)
eylul.entlang("Turkish")
eylul.entlang("Spanish")
c=eylul.printl()
for i in c:
    if i not in liste:
        liste.append(i)
    else:
        continue
for i in liste:
    print(i)

    

