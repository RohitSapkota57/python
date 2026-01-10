# Dictionary for question and answer
words = {
    "What is 2 + 2?": "4",
    "What color is the sky on a clear day?": "blue",
    "How many days are there in a week?": "7",
    "What is 4 + 4?" : "8",
    "Which animal says “meow”?": "cat"
}

score = 0

for word, meaning in words.items():
    user_answer = input(f"Meaning of '{word}': ").lower().strip()

    if user_answer == meaning.lower():         #for answer and meaning validation
        print("Correct ✅\n")
        score += 1                            
    else:
        print("Wrong ❌ | Correct:", meaning)

print("Your score:", score, "/", len(words))