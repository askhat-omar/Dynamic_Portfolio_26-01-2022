from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import numpy
import json


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'static_portfolio_chp'
    players_per_group = None
    num_rounds = 1
    b = [136.71, 123.69, 101.83, 83.72]
    d = [300.00, 222.12, 93.43, 42.19]
    p = [0.111, 0.361, 0.403, 0.125]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    lottery_chp = models.StringField(
        choices=[[1,'I prefer asset A (not to invest)'], [2, 'I prefer asset B'], [3, 'I prefer asset C'], [4, 'I prefer asset D']], widget=widgets.RadioSelect
    )

    w_1 = models.StringField()
    w_2 = models.StringField()
    w_3 = models.StringField()
    w_4 = models.StringField()

    def set_wealth(self, w_1, w_2, w_3, w_4):
        self.w_1 = w_1
        self.w_2 = w_2
        self.w_3 = w_3
        self.w_4 = w_4

    def for_payoff(self):
        if self.lottery_chp == '1':
            k = 100
        elif self.lottery_chp == '2':
            k = numpy.random.choice(Constants.b, p=Constants.p)
        elif self.lottery_chp == '3':
            k = numpy.random.choice([self.w_1, self.w_2, self.w_3, self.w_4], p=Constants.p)
        else:
            k = numpy.random.choice(Constants.d, p=Constants.p)
        self.payoff = k
