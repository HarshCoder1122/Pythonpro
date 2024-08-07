from datetime import date
class person:
    def __init__(self,Name,Country,Date_of_Birth):
        self.Name=Name
        self.Country=Country
        self.Date_of_Birth=Date_of_Birth

    def Age(self):
        today= date.today()
        age=today.year-self.Date_of_Birth.year
        if today< date(today.year,self.Date_of_Birth.month,self.Date_of_Birth.day):
            age-=1
        return age


person1=person("Harsh","India",date(2005,12,11))
print(person1.Name)
print(person1.Country)
print(person1.Date_of_Birth)
print(person1.Age())