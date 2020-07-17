import os
import random
import time
import winsound
import datetime
import database

def play_game():
    cursor = database.create_db()
    name = ''
    words = []  
    n = 1     
    score = 0 

    with open(".\\resource\\word.txt", 'r') as f:
        for c in f:
            words.append(c.strip())

    start = time.time()

    while n <= 5:
        os.system("cls")

        random.shuffle(words)
        q = random.choice(words)

        print("[ Q {} ]".format(n))
        print(q)

        answer = input()
        print("result : ", end='')

        if str(q).strip() == str(answer).strip():
            print("Correct!!!")
            winsound.PlaySound(".\\resource\\sound\\correct.wav", winsound.SND_FILENAME)
            score = score + 1
        else:
            print("Wrong...")
            winsound.PlaySound(".\\resource\\sound\\wrong.wav", winsound.SND_FILENAME)

        n = n + 1

    end = time.time()
    play_time = end - start
    play_time = format(play_time, ".3f")

    os.system("cls")

    if score >=3:
        print("Pass!!!")
    else:
        print("Fail...")

    print("Play time : ", play_time, "s, ", "Score : {}".format(score))
    print()

    while name == '':
        name = input(">>> Enter your name (No blank) : ")

    database.insert_record(cursor, name, score, play_time)