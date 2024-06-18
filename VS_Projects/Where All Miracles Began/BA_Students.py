
from tkinter.messagebox import QUESTION


class Student:
    def __init__ (self, name, age, birthday, school, year, club, gun, description, opinion, would):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.school = school
        self.year = year
        self.club = club
        self.gun = gun
        self.description = description
        self.opinion = opinion
        self.all = f"\n{name}\n{age}\n{birthday}\n{school}\n{year}\n{club}\n{gun}\n{description}\n{opinion}"
        self.would = would


class Sensei_Standards:
    def __init__ (self, ask, would):
        self.ask = ask
        self.would = would

