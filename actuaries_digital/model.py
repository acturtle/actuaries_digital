from cashflower import variable

from input import assumption, main
from settings import settings


@variable()
def survival_rate(t):
    if t == 0:
        return 1
    return survival_rate(t-1) * (1-assumption["DEATH_PROB"])


@variable()
def expected_benefit(t):
    if t == 0:
        return 0
    if t > main.get("remaining_term"):
        return 0
    return survival_rate(t-1) * assumption["DEATH_PROB"] * main.get("sum_assured")


@variable()
def net_single_premium(t):
    if t == settings["T_MAX_CALCULATION"]:
        return expected_benefit(t)
    return expected_benefit(t) + net_single_premium(t+1) * 1/(1+assumption["INTEREST_RATE"])
