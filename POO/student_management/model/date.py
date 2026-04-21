from datetime import datetime
class Date:
    Dates = {"Janvier":"January", "Fevrier":"February", "Mars":"March", "Avril":"April", "Mai":"May", "Juin":"June", "Juillet":"July", "Aout":"August", "Septembre":"September", "Octobre":"October", "Novembre":"November", "Decembre":"December"}
    dates = {"Fev":"Feb", "Avr":"Apr", "Mai":"May", "Jui":"Jun", "Jui":"Jul", "Aou":"Aug"}
    def __init__(self, student):
        self.student = student

    def separator(self):
        for sep in [' ', '/', '_',  '-', ',', '|', '.', ':']:
            if sep in self.student.date:
                return sep
        
    def parse_date(self):
        day, month, year = '', '', ''
        date_part = self.student.date.split(self.separator())
        if len(date_part) == 3:
            day, month, year = date_part
        return day, month, year


    def str_date_dmy(self, day, month, year):
        date = f'{day}/{month}/{year}'
        try:
            date = datetime.strptime(date, "%d/%m/%y").date()
            date = date.strftime('%d/%m/%Y')
            return date
        except:
            return ""
        
    def validate_dmy(self, d, m, y):
        date = self.str_date_dmy(d, m, y)
        if date:
            self.student.date = date
        else:
            self.student.valid = False
            self.student.erreurs.append('date incorrect')

                


    def str_date_dmyear(self, day, month, year):
        date = f'{day}/{month}/{year}'
        try:
            date = datetime.strptime(date, "%d/%m/%Y").date()
            date = date.strftime('%d/%m/%Y')
            return date
        except:
            return ""
        
    def validate_dmyear(self, d, m, y):
        date = self.str_date_dmyear(d, m, y)
        if date:
            self.student.date = date
        else:
            self.student.valid = False
            self.student.erreurs.append('date incorrect')


    def str_date_dMonthyear(self, day, month, year):
        if month.capitalize() in self.Dates.keys():
            month = self.Dates[month.capitalize()]

        if month.capitalize() in self.dates.keys():
            month = self.dates[month.capitalize()]

        date = f'{day}/{month.capitalize()}/{year}'
        if len(month)>3:
            try:
                date = datetime.strptime(date, "%d/%B/%Y").date()
                date = date.strftime("%d/%m/%Y")
                return True
            except:
                return ""
        elif len(month)==3:
            try:
                date = datetime.strptime(date, "%d/%b/%Y").date()
                date = date.strftime("%d/%m/%Y")
                return date
            except:
                return ""    
            

    def validate_dMonthyear(self, d, m, y):
        date = self.str_date_dMonthyear(d, m, y)
        if date:
            self.student.date = date
        else:
            self.student.valid = False
            self.student.erreurs.append('date incorrect')