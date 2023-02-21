
from datetime import datetime

class Create_Person:
    def __init__(self, name, birthDate, stature):
        self._name = name
        self._birthDate = birthDate
        self._stature = stature
        
    def Current_Year_Calculator(self):
        self.current_year = datetime.today().year
        
    def Age_Calculator(self):
        self.birthDate = self.current_year - int(""*(len(self.birthDate)-4) + self.birthDate[-4:])
    
    def Print_Person(self):
        print ("Nome:", self.name, "\nIdade:", self.birthDate,"Anos", "\nAltura:", self.stature,"m")
        
    @property
    def name(self):
        return self._name.title()
    
    @name.setter
    def name(self, value):
        self._name = value
    
        

new_person = Create_Person("GODI", "08/01/2003", 1.80)
new_person.Current_Year_Calculator()
new_person.Age_Calculator()
new_person.Print_Person()

        