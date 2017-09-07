from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from . import models
from .models import Constants
import config_leex_1

class Introduction(Page):
    wait_for_all_groups = True

    def is_displayed(self):
        return self.round_number == 1

class Send(Page):
    """This page is only for P1
    P1 sends amount (all, some, or none) to P2
    This amount is tripled by experimenter,
    i.e if sent amount by P1 is 5, amount received by P2 is 15"""

    form_model = models.Group
    form_fields = ['sent_amount']

    def is_displayed(self):
        return self.player.id_in_group == 1

    def vars_for_template(self):
        amount = Constants.endowment

        return{
                'amount': amount }

class SendBackWaitPage(WaitPage):
    pass


class SendBack(Page):
    """This page is only for P2
    P2 sends back some amount (of the tripled amount received) to P1"""

    form_model = models.Group
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        tripled_amount = self.group.sent_amount * Constants.multiplication_factor
        amount=Constants.endowment

        return {
                'tripled_amount': tripled_amount
        }

    def sent_back_amount_max(self):
        return self.group.sent_amount * Constants.multiplication_factor


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    """This page displays the earnings of each player"""

    def vars_for_template(self):
        return {
            'tripled_amount': self.group.sent_amount * Constants.multiplication_factor
        }

    def before_next_page(self):

        # pass payoff to new var
        self.player.round_payoff = self.player.payoff

        if config_leex_1.paid_game == Constants.name_in_url and config_leex_1.paid_round == self.round_number:
            self.player.payoff = self.player.payoff
        else:
            self.player.payoff = 0


page_sequence = [
    Introduction,
    Send,
    SendBackWaitPage,
    SendBack,
    ResultsWaitPage,
    Results,
]
