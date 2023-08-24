import pandas as pd
from cashflower import Runplan, ModelPointSet


runplan = Runplan(data=pd.DataFrame({"version": [1]}))

main = ModelPointSet(data=pd.DataFrame({
    "id": [1],
    "sum_assured": [100_000],
    "remaining_term": [36],
}))

assumption = {
    "DEATH_PROB": 0.003,
    "INTEREST_RATE": 0.005
}
