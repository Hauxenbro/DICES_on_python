import random, time

class Main_data:

    def read_bot_prts(self):
        self.bot_prt_adr = []
        for i in range(1,20):
            adr = 'project_files\\portraits\\'
            adr += str(i) + '.png'
            self.bot_prt_adr.append(adr)

    def set_bot_names(self):
        self.bot_names = ['Андрей', 'Антон', 'Ирина', 'Игорь', 'Иван', 'Джейкоб', 'Анна', 'Такидо',
                             'Серёга', 'Жан-Жак', 'Хуарес', 'Дмитрий', 'Василий', 'Нинтендо',
                             'Изира','Анна-Мария','Сирена', 'Алексей', 'Кевин']
        self.bot_current_name = self.bot_names[0]

    def set_bot_banks(self):
        self.bot_bank = [100, 20000, 20000, 300, 500, 500, 500, 1000, 20000, 15000, 2500, 5000, 4000, 9000, 12000, 12000,
                         19000, 15000, 15000]

    def make_bot_banking(self):
        self.set_bot_names()
        self.set_bot_banks()
        self.bot_bank = dict(zip(self.bot_names, self.bot_bank))
        self.bot_current_bank = self.bot_bank[self.bot_current_name]

    def get_dices(self):
        self.dices = []
        for i in range(1,7):
            adr = 'project_files\\' + str(i) + '.png'
            self.dices.append(adr)

    def bot_prt_change(self, side):
        if side:
            if self.bot_img_ind != 18:
                self.bot_img_ind += 1
            else:
                self.bot_img_ind = 0
        else:
            if self.bot_img_ind != 0:
                self.bot_img_ind -= 1
            else:
                self.bot_img_ind = 18

        self.bot_current_name = self.bot_names[self.bot_img_ind]
        self.bot_current_bank = self.bot_bank[self.bot_current_name]

    def start_game(self):
        self.get_dices()
        self.bet = 10
        nick_get = self.nickname_ent.get()
        pl_bank = self.bank_ent.get()
        if nick_get != '':
            self.nickname = nick_get
        else:
            self.nickname = 'UNKNOWN'
        try:
            pl_bank = int(pl_bank)
            self.pl_bank = pl_bank
            self.set_gaming_ui()
        except Exception:
            self.call_bank_err()

    def cnt_winner(self):
        my_sum = self.my_dic_val1 + self.my_dic_val2
        bot_sum = self.bot_dic_val1 + self.bot_dic_val2
        self.table_body_update()
        if my_sum > bot_sum:
            self.pl_bank += self.bet
            self.bot_current_bank -= self.bet
            self.winner()
        elif my_sum < bot_sum:
            self.pl_bank -= self.bet
            self.bot_current_bank += self.bet
            self.loser()
        else:
            self.draw()

    def get_random_dice(self):
        return random.choice(self.dices)

    def check_win(self):
        if self.pl_bank < 10:
            self.loser_menu_ui()
        elif self.bot_current_bank < 10:
            self.winner_menu_ui()

    def check_bets(self):
        if self.pl_bank >= 1000 and self.bot_current_bank >= 1000:
            self.activate_bet_10()
            self.activate_bet_50()
            self.activate_bet_100()
            self.activate_bet_250()
            self.activate_bet_500()
            self.inactivate_bet_1000()
            self.activate_bet_all()
            self.update()
        elif self.pl_bank >= 500 and self.bot_current_bank >= 500:
            self.activate_bet_10()
            self.activate_bet_50()
            self.activate_bet_100()
            self.activate_bet_250()
            self.activate_bet_500()
            self.inactivate_bet_1000()
            self.activate_bet_all()
            self.update()
        elif self.pl_bank >= 250 and self.bot_current_bank >= 250:
            self.activate_bet_10()
            self.activate_bet_50()
            self.activate_bet_100()
            self.activate_bet_250()
            self.inactivate_bet_500()
            self.inactivate_bet_1000()
            self.activate_bet_all()
            self.update()
        elif self.pl_bank >= 100 and self.bot_current_bank >= 100:
            self.activate_bet_10()
            self.activate_bet_50()
            self.activate_bet_100()
            self.inactivate_bet_250()
            self.inactivate_bet_500()
            self.inactivate_bet_1000()
            self.activate_bet_all()
            self.update()
        elif self.pl_bank >= 50 and self.bot_current_bank >= 50:
            self.activate_bet_10()
            self.activate_bet_50()
            self.inactivate_bet_100()
            self.inactivate_bet_250()
            self.inactivate_bet_500()
            self.inactivate_bet_1000()
            self.activate_bet_all()
            self.update()
        else:
            self.activate_bet_10()
            self.inactivate_bet_50()
            self.inactivate_bet_100()
            self.inactivate_bet_250()
            self.inactivate_bet_500()
            self.inactivate_bet_1000()
            self.activate_bet_all()
            self.update()

    def check_current_bet(self):
        if self.bet > self.pl_bank or self.bet > self.bot_current_bank:
            self.inactivate_btt()
            self.update()
        else:
            self.activate_btt()
            self.update()

    def make_bet_10(self):
        self.activate_btt()
        self.bet = 10
        self.bet_lbl['text'] = f'Ваша ставка: \n{self.bet}'
        self.update()

    def make_bet_50(self):
        self.activate_btt()
        self.bet = 50
        self.bet_lbl['text'] = f'Ваша ставка: \n{self.bet}'
        self.update()

    def make_bet_100(self):
        self.activate_btt()
        self.bet = 100
        self.bet_lbl['text'] = f'Ваша ставка: \n{self.bet}'
        self.update()

    def make_bet_250(self):
        self.activate_btt()
        self.bet = 250
        self.bet_lbl['text'] = f'Ваша ставка: \n{self.bet}'
        self.update()

    def make_bet_500(self):
        self.activate_btt()
        self.bet = 500
        self.bet_lbl['text'] = f'Ваша ставка: \n{self.bet}'
        self.update()

    def make_bet_1000(self):
        self.activate_btt()
        self.bet = 1000
        self.bet_lbl['text'] = f'Ваша ставка: \n{self.bet}'
        self.update()

    def make_bet_all(self):
        self.activate_btt()
        if self.pl_bank >= self.bot_current_bank:
            self.bet = self.bot_current_bank
        else:
            self.bet = self.pl_bank
        self.bet_lbl['text'] = f'Ваша ставка: \n{self.bet}'
        self.update()

    def dice_it(self):
        self.inactivate_all_btts()
        for i in range(10):
            self.dices_ui()
            time.sleep(0.1)
        self.cnt_winner()
        self.activate_all_btts()
        self.check_bets()
        self.check_current_bet()
        self.check_win()