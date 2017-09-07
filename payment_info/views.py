from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import config_leex_1

class PaymentInfo(Page):


    def vars_for_template(self):
        participant = self.participant

        return {
            'redemption_code': participant.label or participant.code,
            'paid_game' : config_leex_1.paid_game_display[config_leex_1.paid_game],
            'paid_round': config_leex_1.paid_round
        }


page_sequence = [PaymentInfo]
