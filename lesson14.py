#ООП - обьекто-ориентированое программирование

# класс - синтаксическая единица, чтобы описать объект
# атрибут класса - составляющая класса
# атрибут экземпляра класса -
# метод экземпляра класса -

class Person:
    def __init__(self, name, surname, age, sex):  # __***__магические функции пайтона
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.switch_sex()

    def __str__(self):
        return f'{self.name}_{self.surname},{self.age},{self.sex}'

    def __repr__(self):
        return f'{self.name}_{self.surname}'

    def increase_age(self):  # это метод экземпляра - может самопоменять значение какого-либо атрибута
        self.age += 1

    def switch_sex(self):
        sex_dict = {'male': "female", "female": "male"}
        self.sex = sex_dict[self.sex]


person_1 = Person('John', 'Wick', 23, 'male')
person_2 = Person('Violeta', 'Makarenko', 68, 'female')
list_persons = [person_1, person_2]
print(person_1)
print(person_2)
print(list_persons)


# class MyFirstClass:
#     some_string = 'TEST' #это атрибут класса
#     value = 0   #это атрибут класса
#
#
# MyFirstClass.some_string = 'new test'
# test_value = MyFirstClass.some_string
# new_value = MyFirstClass.value
# print(test_value, new_value)
#
#
# class Person:
#     name = 'John'
#     sorname = 'Wick'
#     age = 23
#     sex = 'Male'
#
#
# if Person.age < 50:
#     print(f'Ты молодой человек, {Person.name} {Person.sorname}')
#
# person_1 = Person()  # экземпляр класса =объект который рожден с помощью класса можем добавлять новые атрибуты  некоторым экзмпл
# person_2 = Person()
# print(person_1.name)
# print(person_2.name)
# print('----------------')
# person_1.name = "Vova" #персональное действие с экземпляром являетс главнее, чем общая команда по атрибутам класса
# print(person_1.name)
# print(person_2.name)
# print('----------------')
# Person.name = "jack"
# print(person_1.name)
# print(person_2.name)
#
