# Challenge: Modules, Classes, Error Handling, and List Comprehensions
########################################################################

# Introduction to the Data and Unique Values
import csv

with open('nfl_suspensions_data.csv', 'r') as csvfile:
    in_file = csv.reader(csvfile)
    nfl_suspensions = list(in_file)
nfl_suspensions = nfl_suspensions[1:len(nfl_suspensions)]

years = {}
for row in nfl_suspensions:
    row_year = row[5]
    if row_year in years:
        years[row_year] += 1
    else:
        years[row_year] = 1

team_list = []
for row in nfl_suspensions:
    team_list.append(row[1])
unique_teams = set(team_list)

game_list = []
for row in nfl_suspensions:
    game_list.append(row[2])
unique_games = set(game_list)

print(years)
print(unique_teams)
print(unique_games)

########################################################################
# Create a 'Suspension' class
class Suspension():
    def __init__(self, row):
        # Only interested in a few items in each row.
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        self.year = row[5]

third_suspension = Suspension(nfl_suspensions[2])

########################################################################
# Create a 'Suspension' class that sets the year column as an Integer and
# set missing year values to zero.
class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0
    def get_year(self):
        return(self.year)
    
missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()