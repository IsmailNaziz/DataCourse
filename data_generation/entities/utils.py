import names
import random

res = {}
key_words = ['Société générale', 'Test', 'Entretien', 'RH', 'Proposition', 'Microsoft teams']

for i in range(300):
    num = random.randint(0, len(key_words) - 1)
    rand_num_for_mail = random.randint(20000, 40000)
    key_word = key_words[num]
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    email = f'{first_name}.{last_name}.{rand_num_for_mail}@gmail.com'
    res[i] = [first_name, last_name, email]


class CommonUtils(object):
    @staticmethod
    def idle_func():
        return 0


class DirtyDataUtils(CommonUtils):
    @staticmethod
    def idle_func():
        return 0


class CleanDataUtils(CommonUtils):

    def first_name_generator(self):
        return names.get_first_name()

    def date_generator(self, beg_date, end_date):
        return beg_date, end_date

    def address_generator(self):
        return

    def gender_generator(self):
        return

    def salary_generator(self):
        return

    def profession_generator(self):
        return
