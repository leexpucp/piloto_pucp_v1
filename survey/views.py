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

class Question(Page):
    form_model = models.Player
    form_fields = ['submitted_answer']

    def submitted_answer_choices(self):
        qd = self.player.current_question()
        return [
            qd['choice1'],
            qd['choice2'],
            qd['choice3'],
            qd['choice4'],
            qd['choice5'],
            qd['choice6'],
            qd['choice7'],
            qd['choice8'],
            qd['choice9'],
            qd['choice10'],
            qd['choice11'],
            qd['choice12'],
            qd['choice13'],
            qd['choice14'],
            qd['choice15'],
            qd['choice16'],
            qd['choice17'],
            qd['choice18'],
            qd['choice19'],
            qd['choice20'],
            qd['choice21'],
            qd['choice22'],
            qd['choice23'],
            qd['choice24'],
            qd['choice25'],
            qd['choice26'],
            qd['choice27'],
            qd['choice28'],
            qd['choice29'],
            qd['choice30'],
            qd['choice31'],
            qd['choice32'],
            qd['choice33'],
            qd['choice34'],
            qd['choice35'],
            qd['choice36'],
            qd['choice37'],
            qd['choice38'],

        ]

# class CognitiveReflectionTest(Page):
#     form_model = models.Player
#     form_fields = ['crt_bat',
#                    'crt_widget',
#                    'crt_lake']


page_sequence = [
    Demographics,
    #Question,
    #CognitiveReflectionTest
]
