def find_highest_score(*args) : 
    highest_score = args[0] 
    for score in args:
        if score > highest_score:
            highest_score = score 
    return highest_score


highest = find_highest_score(78, 88, 90, 98, 62)
print("The highest score is:", highest)