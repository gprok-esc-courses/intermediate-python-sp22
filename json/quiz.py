import requests
import json

url = 'https://opentdb.com/api.php?amount=10'
response = requests.get(url)

data = json.loads(response.text)

questions = data['results']

print(questions)

for question in questions:
    print(question['question'])
    print("1 " + question['correct_answer'])
    counter = 2
    for ans in question['incorrect_answers']:
        print(str(counter) + " " + ans)
        counter += 1
    answer = input("Your answer: ")

# give score like: SCORE 3/10

