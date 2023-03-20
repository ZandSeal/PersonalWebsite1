import random
import csv
import pandas as pd

albums = pd.read_csv('top500.csv')
albums.columns = albums.columns.str.title()

albums['Album Name'] = albums['Album Name'].str.title()
albums['Artist'] = albums['Artist'].str.title()
albums['Genre'] = albums['Genre'].str.title()

print(albums.sample())
