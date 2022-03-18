def get_mood(color):
    mood_chart = {
        "red" : "angry",
        "yellow" : "mellow",
        "blue" : "sad",
        "green" : "happy",
        "black" : "scary",
        "purple" : "royal",
        "pink" : "fun"
    }
    
    color = color.strip().lower()
    
    if color in mood_chart:
        return mood_chart[color]
    else:
        return "confused"
    
    
    
print("Mood Ring!!!")

while True:
    color = input("Enter Color: ").strip().lower()
    mood = get_mood(color)
    print(f"You are feeling {mood}")
    
    command = input("Play Again (Y)es or (N)o: ").lower().strip()
    if command != "y" and command != "yes":
        break

print("Goodbye")