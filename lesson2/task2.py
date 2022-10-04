season_by_month = {
    "1": "Winter",
    "2": "Winter",
    "3": "Spring",
    "4": "Spring",
    "5": "Spring",
    "6": "Summer",
    "7": "Summer",
    "8": "Summer",
    "9": "Autumn",
    "10": "Autumn",
    "11": "Autumn",
    "12": "Winter",
    "January": "Winter",
    "February": "Winter",
    "March": "Spring",
    "April": "Spring",
    "May": "Spring",
    "June": "Summer",
    "July": "Summer",
    "August": "Summer",
    "September": "Autumn",
    "October": "Autumn",
    "November": "Autumn",
    "December": "Winter"
}

print("Supported months")
print(*(season_by_month.keys()))

month = input('Enter a month: ')

if month not in season_by_month:
    print("Invalid month")
    quit()

season = season_by_month[month]
print(f'Season is {season}')


