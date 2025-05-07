import sys, pandas as pd, datetime as dt
from ResourceFile import resource_path

class AdanTimePrepare():
    def __init__(self):
        path = resource_path('resources/xlsx/Quds.xlsx')
        df = pd.read_excel(path)

        self.all_rows = [ col for col in df.itertuples() ]
        self.all_rows.pop(0)

        # self.curr_time = dt.datetime.now()

        self.callender = []
        self.current_adans_index = -1
        self.jomoaa_index = -1
        self.new_year()

    # def handle_time_updated(self, new_curr_time):
    #     self.curr_time = new_curr_time

    def clear_callender(self):
        self.callender = []

    def new_year(self):
        today = dt.date.today()

        self.clear_callender()

        for col in self.all_rows:
            date = col[2]
            date_str = (str(date))
            date_str = date_str[5:11]

            month, day = int(date_str[0:2]), int(date_str[3:])

            try:
                self.callender.append((dt.datetime(today.year, month, day),col[3:]))
            except:
                pass

    def get_current_day_adans(self):
        len_callender = len(self.callender)
        for d in range(len_callender):
            if self.callender[d][0].strftime("%d/%m") == dt.date.today().strftime("%d/%m"):
                self.adansOfToday = self.callender[d]   
                break                
        return self.adansOfToday
        
    def get_jomoaa(self):
        Friday = "Friday"
        index = self.callender.index(self.adansOfToday)
        if self.adansOfToday[0].strftime("%A") == Friday :
            self.jomoaa_index = index
        else:
            for j in range(index,len(self.callender)):
                if self.callender[j][0].strftime("%A") == Friday:
                    self.jomoaa_index = j
                    break
        return dt.datetime.combine(dt.datetime(dt.date.today().year, self.callender[self.jomoaa_index][0].month, self.callender[self.jomoaa_index][0].day), self.callender[self.jomoaa_index][1][2])

    def convert_to_dt(self, ):
        self.datetimes_of_today = [self.adansOfToday[0],[]]
        for i in range(len(self.adansOfToday[1])):
            self.datetimes_of_today[1].append(dt.datetime.combine(dt.datetime(dt.date.today().year, self.adansOfToday[0].month, self.adansOfToday[0].day), self.adansOfToday[1][i]))
        self.datetimes_of_today.insert(1,self.datetimes_of_today[1].pop(1))
        return self.datetimes_of_today

