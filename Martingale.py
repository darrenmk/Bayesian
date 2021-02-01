# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:08:53 2021
"""

import numpy as np

def play(start_chips, start_bet, odds, house_edge):
    chips = start_chips
    bet = start_bet
    count = 0
    while chips > bet:
        p = ( odds[1] / (odds[0] + odds[1]) ) * (1 - house_edge)
        if np.random.binomial(1, p):
            chips += odds[0] * ( bet / odds[1] )
            bet = start_bet
        else:
            chips -= bet
            bet *= 2
        winnings = chips - start_chips
        count += 1
        if chips > start_chips:
            outcome = "success"
            break
        else:
            outcome = "catastrophic failure"
    return winnings, count, outcome

def simulate(n_sims, start_chips, start_bet, odds, house_edge):
    n_wins = 0
    total_winnings = 0
    for i in range(n_sims):
        winnings, count, outcome = play(start_chips, start_bet, odds, house_edge)
        if winnings > 0:
            n_wins += 1
        total_winnings += winnings
    percent_wins = n_wins/n_sims
    print(percent_wins, total_winnings)

simulate(n_sims=1000, start_chips=1000, start_bet=20, odds=[50,1], house_edge=0) #