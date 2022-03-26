import sys, gaming_conf
class Configurate(gaming_conf.Main_data):
    def quit_app(self):
        self.destroy()
        sys.exit()

    def clear_window(self):
        for i in self.winfo_children():
            i.destroy()
        self.update()

    def check_moving_win(self):
        if self.overrideredirect() == True:
            self.text_move_btt = 'MOVE'
        else:
            self.text_move_btt = 'PIN'
    def move_wind(self):
        if self.overrideredirect() == True:
            self.overrideredirect(False)
            self.check_moving_win()
            self.move_btt['text'] = self.text_move_btt
            self.update()
        else:
            self.overrideredirect(True)
            self.check_moving_win()
            self.move_btt['text'] = self.text_move_btt
            self.update()

    def back_menu(self):
        self.clear_window()
        self.start_app()

    def table_body_update(self):
        current_my_text, current_my_fg = self.table_lg_my2['text'], self.table_lg_my2['fg']
        current_bot_text, current_bot_fg = self.table_lg_bot2['text'], self.table_lg_bot2['fg']
        self.table_lg_my3['text'], self.table_lg_my3['fg'] = current_my_text, current_my_fg
        self.table_lg_bot3['text'], self.table_lg_bot3['fg'] = current_bot_text, current_bot_fg
        current_my_text, current_my_fg = self.table_lg_my1['text'], self.table_lg_my1['fg']
        current_bot_text, current_bot_fg = self.table_lg_bot1['text'], self.table_lg_bot1['fg']
        self.table_lg_my2['text'], self.table_lg_my2['fg'] = current_my_text, current_my_fg
        self.table_lg_bot2['text'], self.table_lg_bot2['fg'] = current_bot_text, current_bot_fg
        self.update()

    def winner(self):
        self.table_lg_my1['text'], self.table_lg_my1['fg'] = f'+{str(self.bet)}', 'green'
        self.table_lg_bot1['text'], self.table_lg_bot1['fg'] = f'-{str(self.bet)}', 'red'
        self.my_bank_lbl['text'] = f'Ваш банк: \n{self.pl_bank}'
        self.bot_bank_lbl['text'] = f'Банк противника: \n{self.bot_current_bank}'
        self.update()
    def loser(self):
        self.table_lg_my1['text'], self.table_lg_my1['fg'] = f'-{str(self.bet)}', 'red'
        self.table_lg_bot1['text'], self.table_lg_bot1['fg'] = f'+{str(self.bet)}', 'green'
        self.my_bank_lbl['text'] = f'Ваш банк: \n{self.pl_bank}'
        self.bot_bank_lbl['text'] = f'Банк противника: \n{self.bot_current_bank}'
        self.update()
    def draw(self):
        self.table_lg_my1['text'], self.table_lg_my1['fg'] = '0', 'black'
        self.table_lg_bot1['text'], self.table_lg_bot1['fg'] = '0', 'black'
        self.update()

    def from_chose_menu(self):
        self.clear_window()
        self.start_app()

    def activate_all_btts(self):
        self.activate_btt()
        self.activate_bet_10()
        self.activate_bet_50()
        self.activate_bet_100()
        self.activate_bet_250()
        self.activate_bet_500()
        self.activate_bet_1000()
        self.activate_bet_all()

    def inactivate_all_btts(self):
        self.inactivate_btt()
        self.inactivate_bet_10()
        self.inactivate_bet_50()
        self.inactivate_bet_100()
        self.inactivate_bet_250()
        self.inactivate_bet_500()
        self.inactivate_bet_1000()
        self.inactivate_bet_all()