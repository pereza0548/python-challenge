# -*- coding: utf-8 -*-
# PyPoll
""" 
Created on Sat Mar 20 13:38:02 2021

@author: perez
"""

import csv
import os

election = os.path.join("Resources", "election_data.csv")

with open(election, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)
    
    total_votes = []
    candidates = []
    Khan = int()
    Khan_per = float()
    Correy = int()
    Correy_per = float()
    Li = int()
    Li_per = float()
    Otooley = int()
    Otooley_per = float()
    Oname = str("O'Tooley")
    win_name = str()
    votes_won_each = []
    winner = []
    
    for x in csvreader:
        total_votes.append(x[0])
        candidates.append(x[2])
        
total = len(total_votes)
Khan = candidates.count("Khan")
Khan_per = round((Khan/total)*100,3)   
Correy = candidates.count("Correy")
Correy_per = round((Correy/total)*100,3)
Li = candidates.count("Li") 
Li_per = round((Li/total)*100,3)
Otooley = candidates.count("O'Tooley")
Otooley_per = round((Otooley/total)*100,3)

if Khan > Correy > Li > Otooley:
    winner = Khan
    win_name = "Khan"
elif Correy > Khan > Li > Otooley:
    winner = Correy
    win_name = "Correy"
elif Li > Khan > Correy > Otooley:
    winner = Li
    win_name = "Li"
elif Otooley > Khan > Correy > Li:
    winner = Otooley
    win_name = Oname
  

print("Election Results")
print("-------------------------")
print(f'Total Votes: {total}')
print("-------------------------")
print(f'Khan:  %{Khan_per}  ({Khan})')
print(f'Correy:   %{Correy_per}  ({Correy})')
print(f'Li:  %{Li_per} ({Li})')
print(f'{Oname}:  %{Otooley_per}  ({Otooley})')
print("-------------------------")
print(f'Winner: {win_name}')
print("-------------------------")

output_file = os.path.join("..", "PyPoll","Analysis","PyPollOutput.txt")

with open(output_file, "w") as writer: 
    file_writer = csv.writer(writer, delimiter= ',')
    file_writer.writerow(["Election Results"])
    file_writer.writerow(["-------------------------"])
    file_writer.writerow([f'Total Votes: {total}'])
    file_writer.writerow(["-------------------------"])
    file_writer.writerow([f'Khan:  %{Khan_per}  ({Khan})'])
    file_writer.writerow([f'Correy:   %{Correy_per}  ({Correy})'])
    file_writer.writerow([f'Li:  %{Li_per} ({Li})'])
    file_writer.writerow([f'{Oname}:  %{Otooley_per}  ({Otooley})'])
    file_writer.writerow(["-------------------------"])
    file_writer.writerow([f'Winner: {win_name}'])
    file_writer.writerow(["-------------------------"])