qna = {
    'Hello': 'hi',
    'I am Robot': 'I am Awl',
    'What is your name': 'mikyawal',
    'Where are you from': 'amazon',
    'You are so cute': 'Thank you'
}

while True:
    try:
        ques = input()
        if ques == 'quit':
            break
        else:
            print(qna[ques])
    except:
        print('I dont know')