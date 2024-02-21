print("\t\tПрограмма Кучук")
print("\t\tВикторина")

import sys

def open_file(file_name, mode):
    """Открывает файл"""
    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print("Невозможно открыть файл ", file_name, "ошибка", e)
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Возвращает в отформатированном виде строку игрового файла"""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Возвращает блок данных из игрового файла"""
    category = next_line(the_file)
    question =  next_line(the_file)
    answers = []
    nominal = 0
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
        nominal = int(next_line(the_file).strip())
    explantaion = next_line(the_file)
    return category, question, answers, correct, explantaion

def welcome(title):
    """Приветствует игрока и сообщает тему игры"""
    print("Добро пожаловать на викторину\n")
    print("\n\n", title, "\n\n")

def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    category, question, answers, correct, explantaion, nominal = next_block(trivia_file)
    while (category):
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, " ", answers[i])
    answer = input("Ваш ответ (1-4)\n")
    if answer == correct:
        print("\nДа!", end=" ")
        score += 1
    else:
        print("\nНет")
    print(explantaion)
    print("Счет: ", score, "\n\n")
    category, question, answers, correct, explantaion = next_block(trivia_file)
    trivia_file.close()
    print("Это был последний вопрос")
    print("Вы заработали ", score, "очков")

open_file()
next_line()
next_block()
welcome()
main()
