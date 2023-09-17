import datetime as dt

date_format = '%d.%m.%Y'

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, next_record: 'Record'):
        self.records.append(next_record)
    
    def get_today_stats(self):
        d_today = dt.date.today()
        return sum(i.amount for i in self.records 
                   if i.date == d_today) 

    def get_week_stats(self):
        d_today = dt.date.today()
        return sum(i.amount for i in self.records
                   if i.date >= d_today - dt.timedelta(days=7))   
    # вывод результата списка
    # def show_records(self):
    #     print(self.records[0].date)
    
class Record:
    def __init__(self, amount: float, comment: str, date: str=None):
        self.amount = amount
        self.comment = comment
        if date is not None:
            self.date = dt.datetime.strptime(date, date_format).date()
        else:
            self.date = dt.date.today()
  

r1 = Record(amount=145, comment='кофе')
r2 = Record(amount=300, comment='Серёге за обед')
r3 = Record(amount=3000, comment='Бар на Танин день рождения', 
date='15.09.2023')

    # записи для калорий
r4 = Record(amount=118, comment='Кусок тортика. И ещё один.')
r5 = Record(amount=84, comment='Йогурт.')
r6 = Record(amount=1140, comment='Баночка чипсов.',
date='16.09.2023')

limit = 100
cash_calculator = Calculator(limit)
calories_calculator = Calculator(limit)
cash_calculator.add_record(r1)
cash_calculator.add_record(r2)
cash_calculator.add_record(r3)

# "вывод результата списка"
# cash_calculator.show_records()



calories_calculator.add_record(r4)
calories_calculator.add_record(r5)
calories_calculator.add_record(r6)

    # вывод результатов
# print(cash_calculator.get_today_cash_remained('rub'))
# print(calories_calculator.get_calories_remained())
print(cash_calculator.get_today_stats())
print(cash_calculator.get_week_stats())
print(calories_calculator.get_week_stats())
