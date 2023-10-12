#! /usr/bin/python3

level1_questions = ('How much is 2*7?: ',
                    'How much is 45 + 90?: ',
                    'What is the biggest country in the world?: ',
                    'What is the capital of Turkey?: ',
                    'Where is Dublin?: ',)

level1_options = (('A. 12', 'B. 14', 'C. 13', 'D. 16'),
                  ('A. 125', 'B. 130', 'C. 135', 'D. 145'),
                  ('A. China', 'B. USA', 'C. Australia', 'D. Russia'),
                  ('A. Istanbul', 'B. Kairo', 'C. Rabat', 'D. Ankara'),
                  ('A. Scotland', 'B. Ireland', 'C. Arab Emirates', 'D. Denmark'))

level1_answers = ('B', 'C', 'D', 'D', 'B')

level2_questions = ('How much is 27 + 123?: ',
                    'What language has the words: Да and Жена?: ',
                    'What country takes the most of Himalaya?: ',
                    'What continent is country Ben located?: ',
                    'How many states are in the US?: ',)

level2_options = (('A. 163', 'B. 140', 'C. 147', 'D. 150'),
                  ('A. Armenian', 'B. Latvian', 'C. German', 'D. Russian'),
                  ('A. Nepal', 'B. India', 'C. Bhutan', 'D. China'),
                  ('A. Afrika', 'B. South-America', 'C. Asia', 'D. Oceania'),
                  ('A. 47', 'B. 50', 'C. 52', 'D. 54'))

level2_answers = ('D', 'D', 'A', 'A', 'B')

level3_questions = ('What is the number 13 as hexadecimal?: ',
                    'How many bones are in the human body?: ',
                    'Which planet in the solar system has the most moons?: ',
                    'What is North Koreas population?: ',
                    'Which of these rivers is located in Europe: ',)

level3_options = (('A. E', 'B. B', 'C. F', 'D. D'),
                  ('A. 198', 'B. 201', 'C. 214', 'D. 206'),
                  ('A. Saturn', 'B. Mars', 'C. Uranus', 'D. Jupiter'),
                  ('A. ≈6 million', 'B. ≈3 million', 'C. ≈9 million', 'D. Can we trust Google???'),
                  ('A. Volga', 'B. Yellow', 'C. Elbe', 'D. Fraser'))

level3_answers = ('D', 'D', 'A', 'D', 'C')

level1_guesses=[]
level1_score=0
level1_question_num=0

for question in level1_questions:
    print('--------------------')
    print(question)
    for option in level1_options[level1_question_num]:
        print(option)
    guess=input('Enter (A,B,C,D): ').upper()
    level1_guesses.append(guess)
    if guess==level1_answers[level1_question_num]:
        level1_score+=1
        print('        CORRECT!')
    else:
        print('        INCORRECT :(')
    level1_question_num+=1

print('---------------')
print('    RESULTS    ')
print('---------------')

print('right answers: ', end=' ')
for answer in level1_answers:
    print(answer, end=' ')
print()

print('Your guesses: ', end=' ')
for guess in level1_guesses:
    print(guess, end=' ')
print()

score=int(level1_score/len(level1_questions)*100)
print(f'Your score is {score}%')
if score > 70:
    print('        YOU GOT TO LEVEL 2!    ')
    
    # Level 2
    level2_guesses=[]
    level2_score=0
    level2_question_num=0

    for question in level2_questions:
        print('--------------------')
        print(question)
        for option in level2_options[level2_question_num]:
            print(option)
        guess=input('Enter (A,B,C,D): ').upper()
        level2_guesses.append(guess)
        if guess==level2_answers[level2_question_num]:
            level2_score+=1
            print('        CORRECT!')
        else:
            print('        INCORRECT :(')
        level2_question_num+=1

    print('---------------')
    print('    RESULTS    ')
    print('---------------')

    print('right answers: ', end=' ')
    for answer in level2_answers:
        print(answer, end=' ')
    print()

    print('Your guesses: ', end=' ')
    for guess in level2_guesses:
        print(guess, end=' ')
    print()

    score=int(level2_score/len(level2_questions)*100)
    print(f'Your score is {score}%')
    if score >= 80:
        print('        YOU GOT TO LEVEL 3!')
        
        # Level 3
        level3_guesses=[]
        level3_score=0
        level3_question_num=0

        for question in level3_questions:
            print('--------------------')
            print(question)
            for option in level3_options[level3_question_num]:
                print(option)
            guess=input('Enter (A,B,C,D): ').upper()
            level3_guesses.append(guess)
            if guess==level3_answers[level3_question_num]:
                level3_score+=1
                print('        CORRECT!')
            else:
                print('        INCORRECT :(')
            level3_question_num+=1

        print('---------------')
        print('    RESULTS    ')
        print('---------------')

        print('right answers: ', end=' ')
        for answer in level3_answers:
            print(answer, end=' ')
        print()

        print('Your guesses: ', end=' ')
        for guess in level3_guesses:
            print(guess, end=' ')
        print()

        score=int(level3_score/len(level3_questions)*100)
        print(f'Your score is {score}%')
        if score > 80:
            print('        CONGRATULATIONS YOU WON THE WHOLE QUIZ!')
        else:
            print('        BACK TO THE START!')
    else:
        print('         TO THE START!')
else:
    print('        BETTER LUCK NEXT TIME! ;)')