from Employee import Employee
from Person import Person

class ITEmployee(Employee):

    def __init__(self, *args,**kwargs):
        Employee.__init__(self, *args,**kwargs)
        self.skills = []

    def add_skill(self,new_skill):
        self.skills.append(new_skill)

    def add_skills(self,new_skills):
        self.skills.extend(new_skills)

if __name__=="__main__":
    it = ITEmployee("Vova Petrov",1990,"Lead",10,1000)
    it.raise_salary(2000)
    print(it.salary)
    it.add_skill("SQL")
    print(it.skills)
    it.add_skill("Networking")
    print(it.skills)
    it.add_skills(["Linux","MacOs"])
    print(it.skills)
    print(it.year_birth)


