import sys
from cashflower import start
from settings import settings


if __name__ == "__main__":
    output = start("actuaries_digital", settings, sys.argv)

    # Pretty-print
    pretty_output = output
    pretty_output['survival_rate'] = pretty_output['survival_rate'].map(lambda x: '{0:.6f}'.format(x))
    pretty_output['expected_benefit'] = pretty_output['expected_benefit'].map(lambda x: '{0:.2f}'.format(x))
    pretty_output['net_single_premium'] = pretty_output['net_single_premium'].map(lambda x: '{0:.2f}'.format(x))

    print(pretty_output.iloc[[0, 1, 2, 3, 34, 35, 36]].to_string(index=False))
