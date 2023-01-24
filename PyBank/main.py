#import pandas as pd
import pandas as pd

import os
import csv

print ("module 3 challenge")

budget_d = pd.read_csv("../PyBank/Resources/budget_data.csv")
#print(budget_d)

#total number of months
total_months = len(budget_d['Date'].unique())


#find profit/losses
Profit = budget_d["Profit/Losses"].sum()

#change in prof/loss
change = budget_d["Profit/Losses"].diff(+1)
budget_d["change"] = change

average_change = budget_d["change"].mean()
average_change = round(int(average_change))

#greatest inc in profit
greatinc = budget_d["change"].max()
greatinc = round(int(greatinc))


#DECEREASE
decrease = budget_d["change"].min()
decrease = round(int(greatest_decrease))


#-------------------------------------------
Print("financial analysis")
Print("________________________")
Print("Total Months: " + str(total_months))
Print("Total: $" +str(Profit))
Print("Average Change:$" +str(average_change))

Print("____________________________")

Filename = "../PyBank/
File.write(Financial Analysis/n")
File.write("_________"/n")
File.write("Total Months: %d/n" % total_months)
File.write(Total Revenue: $%/n" % profit)
File.write(Average Change $%d/n" % average_change)


