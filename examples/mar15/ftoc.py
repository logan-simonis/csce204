def fahr_to_celc(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9
    return celcius

def celc_to_fahr(celcius):
    fahrenheit = celcius * 9/5 + 32
    return fahrenheit

def miles_to_kilo(miles):
    kilometers = miles * 1.60934
    return kilometers

def kilo_to_miles(kilo):
    miles = kilo * 0.621371
    return miles

command = int(input(f"""
Enter type of conversion:
1. Farenheit to Celcius
2. Celcius to Farenheit
3. Miles to Kilometers
4. Kilometers to Miles: """))

value = float(input("Enter Value: "))

if command == 1:
    result = fahr_to_celc(value)
    print(f"{value}F = {round(result,1)}C")
elif command == 2:
    result = celc_to_fahr(value)
    print(f"{value}C = {round(result,1)}F")
elif command == 3:
    result = miles_to_kilo(value)
    print(f"{value}M = {round(result,1)}K")
elif command == 4:
    result = kilo_to_miles(value)
    print(f"{value}K = {round(result,1)}M")
        


    