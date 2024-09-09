class User:
    def __init__(self, name, age):
        if type(name) is str and name.isalpha() and len(name) > 0:
            self._name = name
        else:
            raise ValueError('Некорректное имя')
        if isinstance(age, int) and 110 >= age >= 0:
            self._age = age
        else:
            raise ValueError('Некорректный возраст')

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if type(new_name) is str and new_name.isalpha() and len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError('Некорректное имя')

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int) and 110 >= new_age >= 0:
            self._age = new_age
        else:
            raise ValueError('Некорректный возраст')


user = User('ÐœÐµÐ³Ð°Ð½', 37)

invalid_names = (-1, True, '', [], '123456', 'ÐœÐµÐ³Ð°Ð½906090')

for name in invalid_names:
    try:
        print(name)
        user.set_name(name)
    except ValueError as e:
        print(e)
