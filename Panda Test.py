# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("c:/users/e1ze4m0/desktop/employees.csv")

# generating one row
row1 = data.sample(n = 1)

# display
row1

# generating another row
row2 = data.sample(n = 1)

# display
row2
