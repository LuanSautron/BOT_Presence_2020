import xlsxwriter

class Xlwriter:
    workbook = None
    def __init__(self):
        if Xlwriter.workbook == None:
            Xlwriter.workbook = xlsxwriter.Workbook('Presence.xlsx')
        
class Liststudent:
    worksheet = Xlwriter().workbook.add_worksheet()
    tab = []
    def __init__(self, file_name=None):
        try:
            fd = open(file_name, "r")
            p = fd.read().split('\n')
            for i in p:
                self.tab.append([i, "absent"])
        except:
            return
        fd.close()
    
    def update_presence(self, email=None, presence=None):
        x = 0

        for i, j in self.tab:
            if i == email:
                self.tab[x][1] = presence
                break
            x += 1

    def is_email_in(self, email=None):
        for i, j in self.tab:
            if i == email:
                return True
        return False

    def create_xls(self):
        row = 0
        col = 0

        for email, presence in self.tab:
            self.worksheet.write(row, col,     email)
            self.worksheet.write(row, col + 1, presence)
            row += 1
        Xlwriter().workbook.close()

class Listpedago:
    tab = []

    def __init__(self, file_name=None):
        try:
            fd = open(file_name, "r")
            self.tab = fd.read().split('\n')
        except:
            return
        fd.close()

    def is_pedago(self, email):
        for i in self.tab:
            if i == email:
                return True
        return False