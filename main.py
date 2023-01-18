import pandas as pd
import os
import csv

print ("module 3 challenge")
print ("Dominique Villarreal")


budget_d = os.path.join('..','PyBank','Resources', 'budget_data.csv')
#print(budget_d)

#total number of months
total_months = len(budget_file['Date'].unique())


#find profit/losses
Profit = budget_d["Profit/Losses"].sum()

#change in prof/loss
Change = budget_d["Profit/Losses"].diff(+1)
budget_d["Change"] = Change

average_change = budget_d["change"].mean()
average_change = round(int(average_change))

#greatest inc in profit
greatinc = budget_d["change"].max()
greatinc = round(int(greatinc))


