from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Demographics(Page):
    form_model = models.Player
    form_fields = ['age',
                   'gender',
                   'field_studies',
                   'provincia',
                   'distrito',]


class gracias(Page):

    def vars_for_template(self):
        participant = self.participant
        return {
            'redemption_code': participant.label or participant.code,
        }


page_sequence = [
    Demographics,
    gracias,
]
