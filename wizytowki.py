# niestety mam totalnie urwanie głowy w pracy więc mogę zrobić zadania tylko po łebkach i wersja minimum

import random
#import Faker

#faker.Faker()
from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self, name, surname, phone, email):
       self.name = name
       self.surname = surname
       self.email = email
       self.phone = phone
    def __str__(self):
        return f'{self.name} {self.surname} {self.email} {self.phone}'
    def contact(self):
        return f'Kontaktujesz się z {self.name} {self.surname} {self.phone}'
    
    @property
    def label_lenght(self):
        return len(self.name) + len(self.surname) + 1


class BusinessContact(BaseContact):
    def __init__(self, company, bphone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.bphone = bphone
    def __str__(self):
        return f'{self.name} {self.surname} {self.email} {self.bphone}'
    def contact(self):
        return f'Kontaktujesz się z {self.name} {self.surname} {self.bphone}'


def new_contact(x):
    for i in range(0,x):
        contact_type = random.randint(1,2) 
        if contact_type == 1:
            new_contact_name_x = fake.name()  
            position = new_contact_name_x.find(" ")
            new_contact_name = new_contact_name_x[0:position]
            new_contact_surname = new_contact_name_x[position+1:]
            new_contact_phone = random.randint(600000000,699999999)
            new_contact_email = new_contact_name + "." + new_contact_surname + "@gmail.com" 
            new_contact_data = BaseContact(name = new_contact_name, surname = new_contact_surname, phone = new_contact_phone, email= new_contact_email)
        else:
            new_contact_name_x = fake.name()  
            position = new_contact_name_x.find(" ")
            new_contact_name = new_contact_name_x[0:position]
            new_contact_surname = new_contact_name_x[position+1:]
            new_contact_phone = random.randint(600000000,699999999)
            new_contact_company = fake.text()[0:10]
            new_contact_email = new_contact_name + "." + new_contact_surname + "@" + new_contact_company.replace(" ", "")  + ".com" 
            new_contact_data = BusinessContact(name = new_contact_name, surname = new_contact_surname, bphone = new_contact_phone, phone = None, email= new_contact_email, company = new_contact_company)
        contact_list.append(new_contact_data)
    i = i + 1




#typ1 = BaseContact(name = "Jan", surname = "Kowalski", firma = firma"JTI", stanowisko= "CFO", email= "j@jti.com")
#typ2 = BaseContact(name = "Anna", surname = "Woźniak", firma = "Zoetis", stanowisko= "Marketing Manager", email= "a@zoetis.com")
#typ3 = BaseContact(name = "Waldemar", surname = "Szczecki", firma = "Bakalland", stanowisko= "MA", email= "j@bakalland.pl")
#typ4 = BaseContact(name = "Iza", surname = "Nowak", firma = "Ipsen", stanowisko= "Programista", email= "j@ipsen.com")
#typ5 = BaseContact(name = "Leszek", surname = "LaLa", firma = "Polski Fundusz Rozwoju", stanowisko= "Stażysta", email= "j@pfr.pl")

contact_list = []

new_contact(5)

#for typki in contact_list:
#    print(f"{typki.name} {typki.surname} {typki.email}")

for typki in contact_list:
    #print(typki)
    print(typki.contact())
    print(typki.label_lenght)

#print(BaseContact.contact(typ2))
#print(typ1.contact())
#print(typ1.label_lentht)