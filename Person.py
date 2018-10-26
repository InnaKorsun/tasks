import datetime
class Person(object):

    def __init__(self, full_name='', year_birth=None):
        self.full_name = full_name
        self.year_birth=year_birth

        if year_birth not in range(1900, 2019):
            '''
            check that year_birth more than 1900 and less than 2019, instead - generate a ValueError
            '''
            raise ValueError("Year of birth more than 2018 or less than 1900")

        if len(full_name.split())!=2:
            '''
            check that full name contains a 2 words,instead - set as default "Dafault name and generate a ValueError"
            '''
            self.full_name = "Default Name"
            raise ValueError ("Full name does not contain 2 words")

    def get_name(self):
        name = self.full_name.split()[0]
        return name

    def get_surname(self):
        surname = self.full_name.split()[1]
        return surname

    def age_in(self,year=datetime.datetime.now().year):
        age = year - self.year_birth
        return age


if __name__ == "__main__":
    per1 = Person("Lola Ivanova",1990)
    print(per1.get_name())
    print(per1.get_surname())
    print(per1.age_in())
    


