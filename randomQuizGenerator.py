#! python3
# Name: Jack Shao
# File Name: randomQuizGenerator.py
# Description: generates 35 different variations of a multiple choice quiz, along with their answer keys

import random

# quiz data, keys are states, values are capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virgina': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# generate 35 quiz and answer key files
for numQuiz in range(35):
    # create quiz and answer key files
    quizFile = open('capitalsQuiz%s.txt' % (numQuiz + 1), 'w')
    answerKeyFile = open('capitalsQuiz_answers%s.txt' % (numQuiz + 1), 'w')

    # write quiz header
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'US State Capitals Quiz (Form %s)' % (numQuiz + 1))
    quizFile.write('\n\n')

    # shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # generate a question for each of the 50 states
    for numQues in range(50):
        correctAnswer = capitals[states[numQues]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # write the questions and answer options into the quiz file
        quizFile.write('%s. What is the capital of %s?\n' % (numQues + 1, states[numQues]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # write the answer key into the answer key file
        answerKeyFile.write('%s. %s\n' % (numQues + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()
