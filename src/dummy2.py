from sklearn.impute import SimpleImputer
import pandas as pd

import debug

df = pd.read_csv('input.csv', header=0)

imputer = SimpleImputer(strategy='mean')
breakpoint()
imputer.fit(df)
