import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.rand(20, 5), columns=list('ABCDE'))
writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
data.to_excel(writer, index=False, sheet_name="test")

