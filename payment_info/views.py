from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import config_leex_1

class part1(Page):

    def vars_for_template(self):
        return {'payoff': self.participant.vars['player_payment']}

    def before_next_page(self):
        self.player.payoff = self.participant.vars['player_payment']
#        self.group.final_pay()
#        self.player.set_payment()

class PaymentInfo(Page):
    #form_model = models.Player
    #form_fields = ['payoff']

    def vars_for_template(self):
    #    participant = self.player.participant

        return {
            #'payoff': self.participant.vars['player_payment'],
            'redemption_code': self.participant.label or self.participant.code,
            'participant': self.participant,
            'paid_game': config_leex_1.paid_game_display[config_leex_1.paid_game],
            'paid_round': config_leex_1.paid_round,
            'participation_fee': config_leex_1.participation_fee,
            'player_payment': self.player.payoff,
            'total_payment': self.player.payoff,

        }


page_sequence = [part1,
                 PaymentInfo]
