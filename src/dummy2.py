from sklearn.impute import SimpleImputer
import pandas as pd

import debug

df = pd.read_csv('input.json')

imputer = SimpleImputer(strategy='mean')
breakpoint()
imputer.fit(df)
