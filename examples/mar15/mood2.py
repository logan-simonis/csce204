def get_mood(color):
    if color == "red":
        return "angry"
    elif color == "yellow":
        return "mellow"
    elif color == "blue":
        return "sad"
    elif color == "green":
        return "happy"
print(get_mood("pink"))