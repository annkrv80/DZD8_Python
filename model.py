from asyncore import write
import csv
from turtle import title


def data_open():
    with open('Phonebook1.csv', encoding='utf-8') as f:
        f_reader = csv.reader(f, delimiter=(','))
        res = list(f_reader)
        return res


def add_info(list):
    with open('Phonebook1.csv', 'a', encoding='utf-8', newline='') as f:
        f_writer = csv.writer(f, delimiter=',')
        f_writer.writerow(list)


def del_info(index):
    data = data_open()
    del data[index]
    with open('Phonebook1.csv', 'w', encoding='utf-8', newline='') as f:
        f_writer = csv.writer(f, delimiter=',')
        for row in data:
            f_writer.writerow(row)


def update_info(index, tel):
    data = data_open()
    data[index][2] = tel
    with open('Phonebook1.csv', 'w', encoding='utf-8', newline='') as f:
        f_writer = csv.writer(f, delimiter=',')
        for row in data:
            f_writer.writerow(row)


def inport_export():
    with open('Phonebook1.csv', encoding="utf8") as f1, open('Phonebook2.csv', 'w', encoding="utf8", newline='') as f2:
        f_reader = csv.reader(f1, delimiter=';')
        f_writer = csv.writer(f2, delimiter=';')
        for row in f_reader:
            f_writer.writerow(row)
