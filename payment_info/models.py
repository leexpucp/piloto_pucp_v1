from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class Constants(BaseConstants):
    name_in_url = 'payment_info'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    # variables that change for each group
    treatment_endowment = models.IntegerField()
    treatment_treatment = models.TextField()

    def final_pay(self):
        p = self.get_player_by_id()
        p.final_reward = self.treatment_endowment+ p.payoff
class Player(BasePlayer):
    pass


