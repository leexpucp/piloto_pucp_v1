from mock.mock import self
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import config_leex_1


doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class Constants(BaseConstants):
    name_in_url = 'payment_info'
    players_per_group = None
    num_rounds = 1
    paid_game = config_leex_1.paid_game
    paid_round = config_leex_1.paid_round
    participation_fee = c(config_leex_1.participation_fee)
class Subsession(BaseSubsession):
    def before_session_starts(self):
        for p in self.get_players():
            p.payoff = 0


class Group(BaseGroup):

    def final_pay(self):
        p = self.get_players()
        p.final_reward = Constants.participation_fee

class Player(BasePlayer):
    round_payoff = models.FloatField()
    payoff = models.CurrencyField()
    final_reward=models.CurrencyField()

    def set_payment(self):
        #self.participant.vars['player_payment'],
        self.participant.vars.get('player_payment')





