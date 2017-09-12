from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import config_leex_1

doc = """
Ultimatum game with two treatments: direct response 
In the former, one player makes an offer and the other either accepts or rejects.
It comes in two flavors, with and without hypothetical questions about the second player's 
response to offers other than the one that is made.
"""


class Constants(BaseConstants):
    name_in_url = 'ultimatum'
    players_per_group = 2
    num_rounds = config_leex_1.UG_number_rounds ## Notice this come from a config file
    instructions_template = 'ultimatum/Instructions.html'
    endowment = c(config_leex_1.UG_endowment) ## Notice this come from a config file
    payoff_if_rejected = c(0)
    offer_increment = c(1)
    offer_choices = currency_range(0, endowment, offer_increment)
    offer_choices_count = len(offer_choices)
    keep_give_amounts = []

    for offer in offer_choices:
        keep_give_amounts.append((offer, endowment - offer))

class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)
        if self.round_number == 1:
            paying_round = config_leex_1.paid_round
            self.session.vars['paying_round'] = paying_round

def question(amount):
    return 'Acep    tarías una oferta de {}?'.format(c(amount))


class Group(BaseGroup):

    amount_offered = models.CurrencyField(choices=Constants.offer_choices)
    offer_accepted = models.BooleanField(
        doc="if offered amount is accepted (direct response method)"
    )
    real_payoff = models.CurrencyField()


    def set_payoffs(self):
        p1, p2 = self.get_players()
        if self.offer_accepted:
            p1.payoff = Constants.endowment - self.amount_offered
            p2.payoff = self.amount_offered
        else:
            p1.payoff = Constants.payoff_if_rejected
            p2.payoff = Constants.payoff_if_rejected
        for player in [p1, p2]:
            if self.round_number == self.session.vars['paying_round']:
                player.real_payoff = player.payoff

class Player(BasePlayer):

    round_payoff = models.FloatField()
    real_payoff = models.CurrencyField()
    # def varpayment(self):
    #     self.participant.vars['player_payment'] = 1
    def role(self):
        if self.id_in_group == 1:
            return 'A'
        else:
            return 'B'
