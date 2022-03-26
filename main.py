import tkinter as tk
from tkinter import messagebox
import configure_widg

class App(tk.Tk, configure_widg.Configurate):
    def __init__(self):
        tk.Tk.__init__(self)
        self.txt_bg = '#007f2b'
        self.resizable(False, False)
        self.attributes('-alpha', 1)
        self.nickname = False
        self.pl_bank = False
        self.start_app()

    def start_app(self):
        self.make_bg()
        self.starting_menu_ui()

    def make_bg(self):
        self.img_bg = tk.PhotoImage(file = 'project_files\\pole.png')
        self.bg_lbl = tk.Label(self, image = self.img_bg)
        self.bg_lbl.pack(side = tk.RIGHT)
        self.game_name_lbl = tk.Label(self, text = 'DICES', font = 'Times 30', bg = self.txt_bg, fg = 'white')
        self.game_name_lbl.place(relx = 0.425, rely = 0.1)

    def starting_menu_ui(self):
        self.starting_btt = tk.Button(self, text = 'START', width = 15, font = 'Times 18', command = self.choosing_ui)
        self.starting_btt.place(relx = 0.375, rely = 0.3)
        self.get_info_btt = tk.Button(self, text = 'GET INFO', width = 15, font = 'Times 18', command = self.info_ui)
        self.get_info_btt.place(relx = 0.375 , rely = 0.4)
        self.options_btt = tk.Button(self, text = 'OPTIONS', width = 15, font = 'Times 18', command = self.options_ui)
        self.options_btt.place(relx = 0.375, rely = 0.5)
        self.quit_btt = tk.Button(self, text = 'QUIT', width = 15, font = 'Times 18', command = self.quit_ask)
        self.quit_btt.place(relx = 0.375 , rely = 0.6)
        self.made_by_lbl = tk.Label(self, text = 'Made by Tony Kuzmenko', bg = self.txt_bg, fg = 'white')
        self.made_by_lbl.place(relx = 0.425, rely = 0.95)

    def choosing_ui(self):
        self.read_bot_prts()
        self.make_bot_banking()
        self.clear_window()
        self.make_bg()
        self.bot_img = tk.PhotoImage(file = self.bot_prt_adr[0])
        self.bot_img_ind = 0
        self.bot_prt = tk.Label(self, image = self.bot_img)
        self.bot_prt.place(relx = 0.375, rely = 0.2)
        self.left_arr = tk.Button(self, text = '\N{Leftwards Black Arrow}', command = self.left_arrow)
        self.left_arr.place(relx = 0.3425, rely = 0.35)
        self.right_arr = tk.Button(self, text = '\N{Rightwards Black Arrow}', command = self.right_arrow)
        self.right_arr.place(relx = 0.6375, rely = 0.35)
        self.bot_name_lbl = tk.Label(self, text = f'{self.bot_current_name} : {self.bot_current_bank}', font = 'Times 15',
                                     bg = self.txt_bg, fg = 'white')
        self.bot_name_lbl.place(relx = 0.425, rely = 0.55)
        self.nickname_lbl = tk.Label(self, text = 'NICKNAME:', width = 10, font = 'Times 15', bg = self.txt_bg, fg = 'white')
        self.nickname_lbl.place(relx = 0.355, rely = 0.6)
        self.nickname_ent = tk.Entry(self, width = 10, font = 'Times 15')
        self.nickname_ent.place(relx = 0.5, rely = 0.6)
        if self.nickname:
            self.nickname_ent.insert(0, f'{self.nickname}')
        self.bank_lbl = tk.Label(self, text = 'BANK:', width = 10, font = 'Times 15', bg = self.txt_bg, fg = 'white')
        self.bank_lbl.place(relx = 0.3825, rely= 0.67)
        self.bank_ent = tk.Entry(self, width = 10, font = 'Times 15')
        self.bank_ent.place(relx = 0.5, rely = 0.67)
        if self.pl_bank:
            self.bank_ent.insert(0, f'{self.pl_bank}')
        self.back_menu_btt = tk.Button(self,text = 'BACK TO MENU', font = 'TIMES 18', width = 15, command = self.from_chose_menu)
        self.back_menu_btt.place(relx = 0.375, rely = 0.75)
        self.start_game_btt = tk.Button(self, text = 'START GAME', font = 'TIMES 18', width = 15, command = self.start_game)
        self.start_game_btt.place(relx = 0.375, rely = 0.85)

    def set_gaming_ui(self):
        self.clear_window()
        background = tk.Label(self, image = self.img_bg)
        background.pack(side = tk.LEFT)
        self.right_frame = tk.Frame(bg = self.txt_bg, width = 400)
        self.right_frame.pack(side = tk.LEFT, fill = tk.BOTH)
        self.table_ui()
        self.bet_ui_bttns()
        self.check_bets()
        self.update()
        self.back_to_choose_btt = tk.Button(self, text = 'BACK', font = 'Times 9', width = 12, command = self.choosing_ui)
        self.back_to_choose_btt.place(relx = 0.01, rely = 0.01)
        self.player_img = tk.PhotoImage(file = 'project_files\\portraits\\user\\1.png')
        self.player_lbl = tk.Label(self, image = self.player_img)
        self.player_lbl.place(relx = 0.01, rely = 0.3)
        self.bot_lbl = tk.Label(self, image = self.bot_img)
        self.bot_lbl.place(relx = 0.49, rely = 0.3)
        self.dice_btt = tk.Button(self, width = 15 , font = 'Times 20', text = 'DICE', command = self.dice_it)
        self.dice_btt.place(relx = 0.2325, rely = 0.05)
        self.bet_lbl = tk.Label(self, text = f'Ваша ставка: \n{self.bet}', font = 'Times 20', bg = self.txt_bg, fg = 'white')
        self.bet_lbl.place(relx = 0.275 , rely = 0.75)
        self.my_bank_lbl = tk.Label(self, text = f'Ваш банк: \n{self.pl_bank}', font = 'Times 15')
        self.my_bank_lbl.place(relx = 0.12, rely = 0.9)
        self.bot_bank_lbl = tk.Label(self, text = f'Банк противника: \n{self.bot_current_bank}', font = 'Times 15')
        self.bot_bank_lbl.place(relx = 0.4, rely = 0.9)

    def dices_ui(self):
        self.my_dice_lbl = tk.Label(self)
        self.my_dice_lbl.place(relx = 0.2, rely = 0.2)
        self.my_dice_lbl1 = tk.Label(self)
        self.my_dice_lbl1.place(relx = 0.2, rely = 0.5)
        self.bot_dice_lbl = tk.Label(self)
        self.bot_dice_lbl.place(relx = 0.355, rely = 0.2)
        self.bot_dice_lbl1 = tk.Label(self)
        self.bot_dice_lbl1.place(relx = 0.355, rely = 0.5)
        self.change_dices_img()

    def table_ui(self):
        self.table_fr = tk.Frame(self.right_frame, relief = tk.SUNKEN, borderwidth = 3)
        self.table_fr.rowconfigure([0,1,2,3], weight = 0, minsize = 50)
        self.table_fr.columnconfigure([0,1], weight = 0 , minsize = 15)
        self.table_fr.place(relx = 0.05, rely = 0.2)
        self.table_name_pl = tk.Label(self.table_fr, text = f'{self.nickname}', width = 15, font = 'Times 15')
        self.table_name_pl.grid(row = 0, column = 0)
        self.table_bot_name = tk.Label(self.table_fr, text = f'{self.bot_current_name}', width = 15, font = 'Times 15')
        self.table_bot_name.grid(row = 0 , column = 1)
        self.table_lg_my1 = tk.Label(self.table_fr, text = '-', width = 15, font = 'Times 15')
        self.table_lg_my1.grid(row = 1, column = 0)
        self.table_lg_my2 = tk.Label(self.table_fr, text = '-', width = 15, font = 'Times 15')
        self.table_lg_my2.grid(row = 2, column = 0)
        self.table_lg_my3 = tk.Label(self.table_fr, text = '-', width = 15, font = 'Times 15')
        self.table_lg_my3.grid(row = 3, column = 0)
        self.table_lg_bot1 = tk.Label(self.table_fr, text = '-', width = 15, font = 'Times 15')
        self.table_lg_bot1.grid(row = 1, column = 1)
        self.table_lg_bot2 = tk.Label(self.table_fr, text = '-', width = 15, font = 'Times 15')
        self.table_lg_bot2.grid(row = 2, column = 1)
        self.table_lg_bot3 = tk.Label(self.table_fr, text = '-', width = 15, font = 'Times 15')
        self.table_lg_bot3.grid(row = 3, column = 1)
        self.update()

    def bet_ui_bttns(self):
        self.bet_10 = tk.Button(self.right_frame, text = '10', font = 'Times 18', command = self.make_bet_10)
        self.bet_10.place(relx = 0.25, rely = 0.6)
        self.bet_50 = tk.Button(self.right_frame, text = '50', font = 'Times 18', command = self.make_bet_50)
        self.bet_50.place(relx = 0.5, rely = 0.6)
        self.bet_100 = tk.Button(self.right_frame, text = '100', font = 'Times 18', command = self.make_bet_100)
        self.bet_100.place(relx = 0.75, rely = 0.6 )
        self.bet_250 = tk.Button(self.right_frame, text = '250', font = 'Times 18', command = self.make_bet_250)
        self.bet_250.place(relx = 0.25, rely = 0.75)
        self.bet_500 = tk.Button(self.right_frame, text = '500', font = 'Times 18', command = self.make_bet_500)
        self.bet_500.place(relx = 0.5, rely = 0.75)
        self.bet_1000 = tk.Button(self.right_frame, text = '1000', font = 'Times 18', command = self.make_bet_1000)
        self.bet_1000.place(relx = 0.75, rely = 0.75)
        self.bet_all = tk.Button(self.right_frame, text = 'ALL IN', font = 'Times 18', command = self.make_bet_all)
        self.bet_all.place(relx = 0.45, rely = 0.9)
        self.update()

    def info_ui(self):
        self.clear_window()
        self.make_bg()
        self.info_txt_lbl = tk.Label(self, text = 'Ваша задача - выиграть банк противника.\n'
                                            'Каждая из сторон бросает кости.\n'
                                            'Выигрывает партию тот, у кого сумма значений\n'
                                            'костей больше.\n'
                                            'Так-же в игре есть ставки.\n'
                                            'Вы можете повышать или понижать ставку,\n'
                                            'чтобы быстрее выиграть банк противника.', bg = self.txt_bg, fg = 'white',
                                            justify = tk.LEFT, font = 'Times 15')
        self.info_txt_lbl.place(relx = 0.25, rely = 0.2)
        self.back_btt = tk.Button(self, text = 'BACK', width = 15, font = 'Times 18', command = self.back_menu)
        self.back_btt.place(relx = 0.375, rely = 0.9)
        self.update()

    def options_ui(self):
        self.clear_window()
        self.make_bg()
        self.check_moving_win()
        self.move_btt = tk.Button(self, text = self.text_move_btt, width = 15, font = 'Times 18', command = self.move_wind)
        self.move_btt.place(relx = 0.375, rely = 0.3)
        self.back_btt = tk.Button(self, text = 'BACK', width = 15, font = 'Times 18', command = self.back_menu)
        self.back_btt.place(relx = 0.375, rely = 0.4)
        self.update()


    def quit_ask(self):
        msgask = messagebox.askyesno('QUIT', 'Вы точно хотите выйти?')
        if msgask == True:
            self.quit_app()

    def call_bank_err(self):
        msgask = messagebox.showerror('DICES', 'Введите число в графу "BANK" ')

    def change_dices_img(self):
        my_dic_adr1 , my_dic_adr2 = self.get_random_dice(), self.get_random_dice()
        self.my_dic_val1, self.my_dic_val2 = list(map(int, (my_dic_adr1[-5], my_dic_adr2[-5])))
        bot_dic_adr1, bot_dic_adr2 = self.get_random_dice(), self.get_random_dice()
        self.bot_dic_val1, self.bot_dic_val2 =  list(map(int, (bot_dic_adr1[-5], bot_dic_adr2[-5])))
        self.my_dice_img = tk.PhotoImage(file = my_dic_adr1)
        self.my_dice_img1 = tk.PhotoImage(file = my_dic_adr2)
        self.bot_dice_img = tk.PhotoImage(file = bot_dic_adr1)
        self.bot_dice_img1 = tk.PhotoImage(file = bot_dic_adr2)
        self.my_dice_lbl['image'] = self.my_dice_img
        self.my_dice_lbl1['image'] = self.my_dice_img1
        self.bot_dice_lbl['image'] = self.bot_dice_img
        self.bot_dice_lbl1['image'] = self.bot_dice_img1
        self.update()


    def right_arrow(self):
        self.bot_prt_change(True)
        self.bot_img = tk.PhotoImage(file = self.bot_prt_adr[self.bot_img_ind])
        self.bot_prt['image'] = self.bot_img
        self.bot_name_lbl['text'] = f'{self.bot_current_name} : {self.bot_current_bank}'
        self.update()

    def left_arrow(self):
        self.bot_prt_change(False)
        self.bot_img = tk.PhotoImage(file = self.bot_prt_adr[self.bot_img_ind])
        self.bot_prt['image'] = self.bot_img
        self.bot_name_lbl['text'] = f'{self.bot_current_name} : {self.bot_current_bank}'
        self.update()

    def inactivate_btt(self):
        self.dice_btt['state'] = tk.DISABLED
        self.update()

    def activate_btt(self):
        self.dice_btt['state'] = tk.NORMAL
        self.update()

    def inactivate_bet_10(self):
        self.bet_10['state'] = tk.DISABLED
        self.update()

    def inactivate_bet_50(self):
        self.bet_50['state'] = tk.DISABLED
        self.update()

    def inactivate_bet_100(self):
        self.bet_100['state'] = tk.DISABLED
        self.update()

    def inactivate_bet_250(self):
        self.bet_250['state'] = tk.DISABLED
        self.update()

    def inactivate_bet_500(self):
        self.bet_500['state'] = tk.DISABLED
        self.update()

    def inactivate_bet_1000(self):
        self.bet_1000['state'] = tk.DISABLED
        self.update()

    def inactivate_bet_all(self):
        self.bet_all['state'] = tk.DISABLED
        self.update()

    def inactivate_back_btt(self):
        self.back_to_choose_btt['state'] = tk.DISABLED

    def activate_back_btt(self):
        self.back_to_choose_btt['state'] = tk.NORMAL

    def activate_bet_10(self):
        self.bet_10['state'] = tk.NORMAL
        self.update()

    def activate_bet_50(self):
        self.bet_50['state'] = tk.NORMAL
        self.update()

    def activate_bet_100(self):
        self.bet_100['state'] = tk.NORMAL
        self.update()

    def activate_bet_250(self):
        self.bet_250['state'] = tk.NORMAL
        self.update()

    def activate_bet_500(self):
        self.bet_500['state'] = tk.NORMAL
        self.update()

    def activate_bet_1000(self):
        self.bet_1000['state'] = tk.NORMAL
        self.update()

    def activate_bet_all(self):
        self.bet_all['state'] = tk.NORMAL
        self.update()

    def winner_menu_ui(self):
        self.clear_window()
        self.make_bg()
        self.winner_lbl = tk.Label(self, text='YOU WIN!', font='Times 30', bg=self.txt_bg, fg= 'white')
        self.winner_lbl.place(relx=0.38, rely=0.3)
        self.restart_btt = tk.Button(self, text='RESTART', width = 15, font='Times 18', command = self.choosing_ui)
        self.restart_btt.place(relx=0.37, rely=0.5)
        self.exit_btt = tk.Button(self, text='EXIT', width = 15, font='Times 18', command = self.quit_ask)
        self.exit_btt.place(relx=0.37, rely=0.6)

    def loser_menu_ui(self):
        self.clear_window()
        self.make_bg()
        self.loser_lbl = tk.Label(self, text='YOU LOST', font='Times 30', bg=self.txt_bg, fg = 'white')
        self.loser_lbl.place(relx=0.38, rely=0.3)
        self.restart_btt = tk.Button(self, text='RESTART', width = 15, font='Times 18', command = self.choosing_ui)
        self.restart_btt.place(relx=0.37, rely=0.5)
        self.exit_btt = tk.Button(self, text='EXIT', font='Times 18', width = 15, command = self.quit_ask)
        self.exit_btt.place(relx = 0.37, rely = 0.6)

if __name__ == '__main__':
    root = App()
    root.mainloop()