questions = ['name', 'questions', 'favourite color']
answer = ['Lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answer):
    print("What's yours {}? It's {}".format(q, a))