


class Timetable:
    names = None
    lernig_name = []
    today = None
    group_nam_order = {}

    key = None
    times = {'8:30-9:15': 0, '9:30-10:15': 1, '15:00-15:45': 2, '16:00-16:45': 3, '17:00-18:45': 4, '17:00-19:45': 5}
    days = {'Понедельник': 0, 'Вторник': 1, 'Среда': 2, 'Четверг': 3, 'Пятница': 4, 'Суббота': 5}
    week = [0] * len(days)
    for i in range(len(times)):
        week[i] = [0] * len(times)
    def __init__(self, names='', today='',time='', key=False, namber=0):
        self.names = names
        self.setdata(today, time, key, namber)

    def setdata(self, today, time, key, nam=1):
        if key:
            self.week[self.times[time]][self.days[today]] = 1
        # for i in self.dataTable:
        #     print(i)
        #     for j in i:
        #         print(j)
    def getdata(self):
        for d in self.days:
            for t in self.times:
                if self.week[self.times[t]][self.days[d]] == 1:
                    print(f'{self.names} {t} {d} {self.lernig_name}')



    def setlern(self, lerns="Учу что хочу."):
        self.lernig_name.append(lerns)



german = Timetable("Герман", "Вторник", '8:30-9:15', 1, 1)

german.setlern('Програмрование Arduino')
german.setdata("Четверг", '8:30-9:15', 1)
german.setdata("Вторник", '15:00-15:45', 1)
german.setdata("Четверг", '15:00-15:45', 1)

german.getdata()
#print(tuple(german.week))





