import pandas as pd

df = pd.read_csv('massive.txt', header=None, delim_whitespace=True)
if df.shape[1] != 3:
    raise ValueError("Очікується, що файл massive.txt містить рівно три стовпці.")

series1 = pd.Series(df[0])
series2 = pd.Series(df[1])
series3 = pd.Series(df[2])

common_values = series1[series1.isin(series2) & series1.isin(series3)]
with open('one.txt', 'w') as f:
    for value in common_values:
        f.write(f"{value}\n")

print("Числа, що зустрічаються у всіх трьох стовпчиках, записані у файл one.txt.")