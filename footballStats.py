import csv
class Team():
    def __init__(self, name, year):
        self.name = name
        f = open("nfl.csv", 'r')
        csvreader = csv.reader(f)
        self.nfl = list(csvreader)
        self.year = year

    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count
    
    def count_wins_in_year(self):
        yearlySum = 0
        for row in self.nfl:
            if row[0] == self.year:
                if row[2] == self.name:
                    yearlySum = yearlySum + 1
        return yearlySum

niners = Team("San Francisco 49ers", "2013")
niners_wins_2013 = niners.count_wins_in_year()