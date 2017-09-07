from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

import config_leex_1

doc = """
This is a standard 2-player trust game where the amount sent by player 1 gets
tripled. The trust game was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.
"""


class Constants(BaseConstants):
    name_in_url = 'trust'
    players_per_group = 2
    num_rounds = config_leex_1.TG_number_rounds

    instructions_template = 'trust/Instructions.html'

    # Initial amount allocated to each player
    endowment = c(config_leex_1.TG_endowment)
    multiplication_factor = 3


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()

class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        min=0, max=Constants.endowment,
        doc="""Amount sent by P1""",
    )

    sent_back_amount = models.CurrencyField(
        doc="""Amount sent back by P2""",
        min=c(0),
    )

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
        p2.payoff = self.sent_amount * Constants.multiplication_factor - self.sent_back_amount


class Player(BasePlayer):

    round_payoff = models.FloatField()

    def role(self):
        return {1: 'A', 2: 'B'}[self.id_in_group]
