temp = int(input("Enter Temp: "))
percip = int(input("Enter Percipitation: ").lower().strip())

if temp <= 32 and percip == "s":
    print("Wear a snow suit")
if temp <= 70 and percip == "r":
    print("wear a rain jacket")
if temp >= 80 and percip == "r":
    print("wear a swimsuit")
else:
    print("You choose")