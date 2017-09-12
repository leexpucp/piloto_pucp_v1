from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from . import models
from .models import Constants
import config_leex_1

class Introduction(Page):
    wait_for_all_groups = True

    def is_displayed(self):
        return self.round_number == 1


class Offer(Page):
    form_model = models.Group
    form_fields = ['amount_offered']
    def vars_for_template(self):
        return {
            'player_in_previous_rounds': self.player.in_previous_rounds(),
        }
    def is_displayed(self):
        return self.player.id_in_group == 1


class WaitForProposer(WaitPage):
    pass


class Accept(Page):
    form_model = models.Group
    form_fields = ['offer_accepted']
    def vars_for_template(self):
        return {
            'player_in_previous_rounds': self.player.in_previous_rounds(),
        }

    def is_displayed(self):
        return self.player.id_in_group == 2   #and not self.group.use_strategy_method


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):


    def before_next_page(self):

        # pass payoff to new var
        self.player.round_payoff = self.player.payoff

        if config_leex_1.paid_game == Constants.name_in_url and config_leex_1.paid_round == self.session.vars['paying_round']:
            self.player.payoff = self.player.round_payoff
            self.participant.vars['player_payment'] = self.player.round_payoff,
        else:
            self.player.payoff = 0
            self.participant.vars['player_payment'] = self.player.round_payoff,

        self.participant.vars['player_payment2'] = self.player.real_payoff,
        self.participant.vars['player_payment'] = self.player.round_payoff,
        self.session.vars['paying_round'] = self.player.payoff

page_sequence = [Introduction,
                 Offer,
                 WaitForProposer,
                 Accept,
                 ResultsWaitPage,
                 Results]
