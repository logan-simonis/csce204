from datetime import date

birthdays = {date(2022, 11, 1), 
    "Amy" : date(2023, 1, 22), 
    "Bobby" : date(2022, 3, 14),
    "Charlie" : date(2022, 7, 11), 
    "Erin" : date(2022, 8, 18), 
    "Frank" : date(2022, 5, 2)
}


#loop through
for friend in birthdays:
    daysTill = (birthdays[friend] - date.today()).days
    
