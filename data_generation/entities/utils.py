from datetime import datetime

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

    def first_name_generator(self):
        return names.get_first_name()

    def last_name_generator(self):
        return names.get_last_name()

    def date_generator(self, args):
        assert 'start_date', 'end_date' in args.keys()
        start_date = datetime.datetime.strptime(args['start_date'], '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(args['end_date'], '%Y-%m-%d').date()
        assert start_date <= end_date
        num_days = (end_date - start_date).days
        #TODO: not take randomly but depending on a law specified
        if 'distribution' not in args.keys():
            rand_days = random.randint(1, num_days)
        random_date = start_date + datetime.timedelta(days=rand_days)
        return random_date


class DirtyDataUtils(CommonUtils):
    pass


class CleanDataUtils(CommonUtils):

    def address_generator(self):
        return

    def gender_generator(self):
        return random.choice(['Male', 'Female', 'Undefined'])

    def salary_generator(self):
        return

    def profession_generator(self):
        return


def date_generator(beg_date, end_date):
        return beg_date, end_date