import sys
import os
import time
import typing_game
import database

if __name__ == '__main__':
    number = -1

    while str(number) != '1' and str(number) != '2' and str(number) != '3':
        os.system("cls")
        print("[ Menu ]")
        print("1. Start Game")
        print("2. Show Records")
        print("3. Exit")
        number = input("Enter number : ")

        if number == '1':
            try:
                typing_game.play_game()
            except Exception as error_msg:
                print(error_msg)
                input()
            number = '0'

        elif number == '2':
            database.show_record()
            number = '0'

        elif number == '3':
            os.system("cls")
            print("Exiting...")
            time.sleep(0.5)
            
            try:
                sys.exit()
            except Exception as error_msg:
                print(error_msg)
                input()