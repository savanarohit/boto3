# import pandas
import pandas as pd
pd_object = pd.read_json('astronomy_simple.json', type='series')

df = pd.DataFrame(pd_object)
print(df)
