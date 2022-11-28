import pandas as pd
import datetime

print()


def to_csv(data, location, keyword):
    date = datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    pd.DataFrame(data).to_csv(f'./save/{location}{keyword}{date}.csv', encoding='utf-8-sig')

