import sqlite3 as sq

class Base:  # работа с базой данных
    """__init__ - создание базы, соединения и курсора
       createTable - создание таблицы
       insert - добавление информации в таблицу
       insertInto - добавление в определённое место
       giveSomething - получить счёт игрока по его нику
       all - запрос на данные из всей таблицы
       maxFive - заменяет счёт ника при необходимости. Возвращает 5 лучщих результатов с никами
       del - удаление соединения"""
    def __init__(self, name='table.db'):  # создание базы
        self.con = sq.connect(name)  # создание соединения
        self.cur = self.con.cursor()  # создание курсора
        self.createTable()  # создание таблицы

    def createTable(self, name='score'):  # создание таблицы
        self.cur.execute(f"""CREATE TABLE IF NOT EXISTS '{name}'(nic text, score int)""")  # создание таблицы score
        all = self.all()
        if len(all) < 5:
            for i in range(5):
                self.insert(f'bot {i}', i)

    def insert(self, nic_us, score, name='score'):  # добавление
        self.cur.execute(f"""INSERT INTO {name} (nic, score) VALUES('{nic_us}', '{score}')""")  # добавление данных в таблицу
        self.con.commit()  # сохранение изменений

    def insertInto(self, name_us, score, name = 'score'): # перезапись счёта игрока
        self.cur.execute(f"""
        UPDATE '{name}' SET score = '{score}' WHERE nic = '{name_us}'""")
        self.con.commit()   # сохранение изменений

    def giveSomething(self, nic_us, name = 'score'):   # получение счёта определённого игрока
        self.cur.execute(f"""SELECT score FROM '{name}' WHERE nic = '{nic_us}'""")   # выделение нужного
        result = self.cur.fetchone()   # возврат счёта игрока
        if result == None:
            return None
        else:
            return result[0]

    def all(self, name='score'):  # получение данных таблицы
        self.cur.execute(f"SELECT * FROM {name}")  # выделение всей таблицы
        return self.cur.fetchall()  # возврат данных

    def maxFive(self, nic, score, add):
        if add:
            oldScore = self.giveSomething(nic)
            if oldScore == None:
                self.insert(nic, score)
            else:
                if oldScore < score:
                    self.insertInto(nic, score)

        info = self.all()

        for i in range(5):
            max = i
            for j in range(i, len(info)):
                if info[max][1] < info[j][1]:
                    max = j
            info[i], info[max] = info[max], info[i]

        top = []
        for i in range(5):
            top.append(info[i])
        return top

    def __del__(self):  # закрытие соединения
        self.con.close()


