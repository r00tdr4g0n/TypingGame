import os
import sqlite3
import datetime
import pandas as pd

def create_db():
    conn = sqlite3.connect('D:\\Yong\\Python\\typing_game\\resource\\record.db', isolation_level=None)
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS record(\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        name text,\
        score INTEGER,\
        record text,\
        regdate text\
    )")

    return cursor
    
def insert_record(cursor, name, score, play_time):
    cursor.execute("INSERT INTO record('name', 'score', 'record', 'regdate') VALUES (?,?,?,?)",\
    (name, score, play_time, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

def show_record():
    os.system("cls")
    conn = sqlite3.connect('D:\\Yong\\Python\\typing_game\\resource\\record.db', isolation_level=None)
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS record(\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        name text,\
        score INTEGER,\
        record text,\
        regdate text\
    )")

    records = cursor.execute("SELECT * FROM record desc")
    # print(type(records.fetchall()))

    records_list = records.fetchall()
    records_list.sort(key = lambda x:(-x[2], x[1]))

    print("NAME\tSCORE")

    for record in records_list:
        print("{}\t{}\t".format(record[1], record[2]))

    input()