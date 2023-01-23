import gspread


class Gsheets:
    def __init__(self, sheet_name):
        self.sheet_name = sheet_name
        self.gs = gspread.service_account("utils/misc/google_sheets/config/service_account.json")
        self.wks = None

    
    def create_new_sheet(self):
        """Creating table templates"""

        sh = self.gs.create(self.sheet_name)
        sh.share(None, perm_type = 'anyone', role = 'writer')

        self.wks = sh.add_worksheet(title = "Участники", rows=10000, cols=10)
        old = sh.worksheet("Sheet1")
        sh.del_worksheet(old)


    def update_columns(self, line, name, insta, contact):
        # Opening
        sh = self.gs.open_by_url('https://docs.google.com/spreadsheets/d/tgfdfg7')
        self.wks = sh.worksheet("Участники")


        self.wks.update(f'A{line}', name)
        self.wks.update(f'B{line}', insta)
        self.wks.update(f'C{line}', contact)
    

    def get_url(self):
        sh = self.gs.open(self.sheet_name)
        return "https://docs.google.com/spreadsheets/d/%s" % sh.id
    
