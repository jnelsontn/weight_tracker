import sqlite3
from datetime import date

def check_for_database():
    '''on startup check to see if database exists
    if not, create it'''

    with sqlite3.connect('db.db') as conn:
        c = conn.cursor()

    try:
        c.execute('''CREATE TABLE Users
            (
            Id INTEGER PRIMARY KEY,
            Name VARCHAR(20) NOT NULL,
            Initial_Weight INTEGER NOT NULL,
            Created_At DATE
            )
            ''')

        c.execute('''CREATE TABLE WeightChart
            (
            Id INTEGER PRIMARY KEY,
            UserId INTEGER,
            WeightOnDate INTEGER NOT NULL,
            DateOfWeighIn DATE,

            FOREIGN KEY(UserId) REFERENCES Users(Id)
            )
            ''')

        conn.commit()

    except:
        pass

def create_user(name, initial_weight):

    with sqlite3.connect('db.db') as conn:
        c = conn.cursor()
        creation_date = date.today()

        c.execute('INSERT INTO Users VALUES (?, ?, ?, ?)',
            (None, name, initial_weight, creation_date))

        conn.commit()

def list_users():
    '''list all users in the system'''
    with sqlite3.connect('db.db') as conn:
        c = conn.cursor()

        c.execute('''SELECT Id, Name FROM USERS''')
        return c.fetchall()

def weigh_in(current_user, weight):
    '''
    user weights in for a current date
    only allows one weigh in per day
    '''
    with sqlite3.connect('db.db') as conn:
        c = conn.cursor()
        current_date = date.today()

        try:
            c.execute('''
                SELECT UserId FROM WeightChart
                WHERE UserId = {}
                AND DateOfWeighIn = "{}"
                '''.format(
                    current_user, current_date))

            if not c.fetchone():
                raise
            else:
                print('User already weighed in today')

        except:
            c.execute('INSERT INTO WeightChart VALUES (?, ?, ?, ?)',
                (None, current_user, weight, current_date))          

def user_weight_history(current_user):
    '''list a history of the user's weight'''
    with sqlite3.connect('db.db') as conn:
        c = conn.cursor()

        c.execute('''SELECT DateOfWeighIn, WeightOnDate
            FROM WeightChart
            WHERE UserId = {}'''.format(
                current_user))

        results = c.fetchall()

        if len(results) > 0:
            return results
        else:
            return None

def compare_previous_and_current_weigh_in(current_user):
    '''Retrieve user's initial weight'''
    with sqlite3.connect('db.db') as conn:
        c = conn.cursor()
        current_date = date.today()

        try:
            c.execute('''SELECT Initial_Weight
                FROM Users
                WHERE Id = {}'''.format(
                    current_user))

            initial_weight = c.fetchone()[0]

            '''Retrieve the user's previous and current
            weight'''
            c.execute('''
                SELECT WeightOnDate FROM WeightChart
                WHERE UserId = {}
                ORDER BY DateOfWeighIn DESC
                LIMIT 2
                '''.format(
                    current_user))

            current_and_previous_weight = c.fetchall()

            previous_weight = current_and_previous_weight[1][0]
            current_weight = current_and_previous_weight[0][0]

            init_prev_cur_weight = [initial_weight, previous_weight, current_weight]

            return init_prev_cur_weight

        except TypeError:
            pass

