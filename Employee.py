from Person import Person

class Employee(Person):

    def __init__(self, full_name=" ", year_birth=1990, position=' ', experience=0, salary=1000):
        Person.__init__(self,full_name,year_birth)
        self.position = position
        self.experience  = experience
        self.salary = salary

    def get_name_position(self):
        if 0<self.experience<=3:
            degree = "Junior"
        elif 3<self.experience<=6:
            degree = "Middle"
        else:
            degree = "Senior"
        return "{} {}".format(degree,self.position)

    def raise_salary(self, summ):
        self.salary +=summ

if __name__=="__main__":
    emp1 = Employee("Vika_Ivanova",1990,"QA",10,1500)
    #print(emp1.get_surname())
    print(emp1.get_name_position())
    emp1.raise_salary(400)
    print(emp1.salary)
