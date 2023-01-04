class Time:
    """docstring for Time"""
    def __init__(self, mins):

        self.mins = mins

        print(f'{self.mins} წუთი არის {Time.to_hour(self)},{Time.to_sec(self)}')


    def to_hour(self):

        hours = self.mins // 60
        mins = self.mins % 60
        return f'{hours} საათი და {mins} წუთი'

    def to_sec(self):

        secs = self.mins*60

        return f'{secs} წამი.'


minutes = input('შეიყვანეთ წუთების რაოდენობა: ')

if minutes.isdigit():
    minutes = int(minutes)
    time_onject = Time(minutes)
else:print('შეიყვანეთ რიცხვი!')

