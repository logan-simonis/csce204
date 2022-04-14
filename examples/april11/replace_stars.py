def replace_stars(word):
    answer = ""
    global word
    
    for letter in word:
        if letter == "*":
            answer += "."
        else:
            answer += letter
    
    word = answer

word = "a*b*c*d*"
replace_stars()
print(word)