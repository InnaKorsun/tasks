class Person(object):

    def __init__(self, full_name=' ', year_birth=1990):
        self.full_name = full_name
        self.year_birth=year_birth

        if year_birth not in range(1900, 2019):
            self.year_birth=1990
            raise Exception("Year of birth more than 2018 or less than 1900. /"
                            "Now year of birth set as default 1990")
        ## check that full name parametr contains 2 words
        if len(full_name.split()) != 2:
            raise Exception ("Full name does not contain 2 words")

        ## check that year of birth contain only numbers
        if not str(year_birth).isdigit():
                raise Exception ("Year of birth is not a number")

    def get_year(self):
        return self.year_birth

    def get_name(self):
        name = self.full_name.split()[0]
        return name

    def get_surname(self):
        surname = self.full_name.split()[1]
        return surname

    def age_in(self,year=2018):
        age = year - self.year_birth
        return age


if __name__ == "__main__":
    per1 = Person("Lola",1990)
    print(per1.get_name())
    print(per1.get_surname())
    print(per1.age_in(2019))


