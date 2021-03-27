# -*- coding: utf-8 -*-
# PyBank
"""
Created on Sat Mar 20 13:38:41 2021

@author: perez
"""

import csv
import os

budget_file = os.path.join("Resources","budget_data.csv")

with open(budget_file, newline='') as csvfile:
      csvreader = csv.reader(csvfile, delimiter= ",")
     
      header = next(csvreader)
      
      months = []
      total_amount = []
      avg_change = []
      great_in = []
      great_de = []
      
      for row in csvreader:
          months.append(row[0])
          total_amount.append(int(row[1]))
      
for x in range(len(total_amount)-1):
    avg_change.append(total_amount[x+1]-total_amount[x])
    
great_in = max(avg_change)
great_de = min(avg_change)

miprint = avg_change.index(great_in)+1
mdprint = avg_change.index(great_de)+1
    
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {len(months)}')
print(f'Total Amount: ${round(sum(total_amount))}')
print(f'Average Change: ${round((sum(avg_change)/len(avg_change)), 2)}')     
print(f'Greatest Increase in Profits: {months[miprint]} (${great_in})')
print(f'Greatest Decrease in Profits: {months[mdprint]} (${great_de})')  

output_file = os.path.join("..", "PyBank","Analysis","PyBankOutput.txt")

with open(output_file, "w") as writer: 
    file_writer = csv.writer(writer, delimiter= ',')
    file_writer.writerow(["Financial Analysis"])
    file_writer.writerow(["----------------------------"])
    file_writer.writerow([f'Total Months: {len(months)}'])
    file_writer.writerow([f'Total Amount: ${round(sum(total_amount))}'])
    file_writer.writerow([f'Average Change: ${round((sum(avg_change)/len(avg_change)), 2)}'])     
    file_writer.writerow([f'Greatest Increase in Profits: {months[miprint]} (${great_in})'])
    file_writer.writerow([f'Greatest Decrease in Profits: {months[mdprint]} (${great_de})']) 
    
         
      
          