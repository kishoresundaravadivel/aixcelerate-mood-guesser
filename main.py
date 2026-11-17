
# Happy or Sad Mood Guesser

# Given training data

train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad")
]


# LEVEL 1 - Count the moods

def count_moods(data):
    happy_count = 0
    sad_count = 0

    for sentence, mood in data:
        if mood == "Happy":
            happy_count += 1
        elif mood == "Sad":
            sad_count += 1

    return happy_count, sad_count


print("Mood Count:", count_moods(train_data))


# LEVEL 2 - Guess the mood

happy_words = [
    "won", "full", "marks", "surprise", "tasty",
    "excited", "selected", "learned", "favourite"
]

sad_words = [
    "lost", "failed", "moving", "rained", "cancelled",
    "missed", "upset", "stopped", "lonely"
]


def guess_mood(sentence):

    sentence = sentence.lower()

    clean_sentence = ""

    for ch in sentence:
        if ch.isalpha() or ch.isspace():
            clean_sentence += ch

    words = clean_sentence.split()

    happy_count = 0
    sad_count = 0

    for word in words:
        if word in happy_words:
            happy_count += 1
        elif word in sad_words:
            sad_count += 1

    if happy_count > sad_count:
        return "Happy"
    elif sad_count > happy_count:
        return "Sad"
    else:
        # If both counts are equal, choose Sad
        return "Sad"


# LEVEL 3 - Test the program

practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy")
]

correct = 0

print("\nPractice Results:")

for sentence, actual_mood in practice_data:

    predicted_mood = guess_mood(sentence)

    print(sentence, "->", predicted_mood)

    if predicted_mood == actual_mood:
        correct += 1

accuracy = (correct / len(practice_data)) * 100

print("\nCorrect Predictions:", correct)
print("Accuracy:", accuracy, "%")
