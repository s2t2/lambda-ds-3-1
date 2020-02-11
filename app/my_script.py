
import random
#import my_mod
from my_mod import announce

#import pandas
#import pandas as pd
from pandas import DataFrame

#df = pandas.DataFrame({"a":[1,2,3], "b":[4,5,6]})
#df = pd.DataFrame({"a":[1,2,3], "b":[4,5,6]})
df = DataFrame({"a":[1,2,3], "b":[4,5,6]})

print(df.head())

print(random.choice(["rock", "paper", "scissors"]))

#my_mod.announce()
announce()
