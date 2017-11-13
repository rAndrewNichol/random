import pymysql
import pandas as pd
import numpy as np

# These functions operate for a table "employee" with certain parameters, but can easily be adjusted to any table
# by changing the SQL queries and the respective python list/database formats.

# This part is easier to simply complete through mysql but is included here in case you would like to
# complete all of your queries through python.
def create_table(host = "localhost", port = 3306, u = 'root', p = '', db = 'mysql'):
    # Open database connection
    db = pymysql.connect(host = host, port = port, user = u, passwd = p, db = db)

    # Prepare a cursor object
    cursor = db.cursor()

    # Delete table if it already exists
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    # Create table in specified sql database
    sql_create = """CREATE TABLE EMPLOYEE (
             FIRST_NAME  CHAR(20) NOT NULL,
             LAST_NAME  CHAR(20),
             AGE INT,
             SEX CHAR(1),
             INCOME FLOAT,
             ID INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT)"""

    cursor.execute(sql_create)

    # Disconnect from server
    cursor.close()
    db.close()


# This function assumes that you will be passing a dataframe (or numpy array/nested list) that matches the table
# in your database and that the columns ARE IN THE SAME ORDER (you may have to reorder the columns of your
# dataframe in python first.
def insert_dataframe(dataframe, host = "localhost", port = 3306, u = 'root', p = '', db = 'mysql'):
    # Open database connection
    db = pymysql.connect(host = host, port = port, user = u, passwd = p, db = db)

    # Prepare a cursor object
    cursor = db.cursor()

    df = pd.DataFrame(dataframe)

    # pandas.values returns
    tuples = [tuple(row) for row in df.values]

    try:
        for x in tuples:
            sql_insert = """INSERT INTO EMPLOYEE(FIRST_NAME,
                   LAST_NAME, AGE, SEX, INCOME)
                   VALUES ('%s', '%s', '%d', '%c', '%d')""" % x
            cursor.execute(sql_insert)
        # Commit changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # Disconnect from server
    cursor.close()
    db.close()


# Retrieves an SQL table and creates a pandas dataframe.
def retrieve_dataframe(host = "localhost", port = 3306, u = 'root', p = '', db = 'mysql'):
    # Open database connection
    db = pymysql.connect(host = host, port = port, user = u, passwd = p, db = db)

    # Prepare a cursor object
    cursor = db.cursor()

    sql_select = """SELECT * FROM days d, classes c WHERE d.day_id = c.day_id"""

    try:
        cursor.execute(sql_select)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        # Results is a tuple with each row.

        day_id, date, dow, sleep, gym, talentiq, reading, fun, econ_class, econ_study, \
        econ_work, ieor_class, ieor_study, ieor_work, stat_class, stat_study, \
        stat_work, cs_study, cs_work, lab_prep = [],[],[],[],[],[],[],[],[],[],[],[], \
        [],[],[],[],[],[],[],[]
        
        for row in results:
            day_id.append(row[0])
            date.append(row[1])
            dow.append(row[2])
            sleep.append(row[3])
            gym.append(row[4])
            talentiq.append(row[5])
            reading.append(row[6])
            fun.append(row[7])
            econ_class.append(row[9])
            econ_study.append(row[10])
            econ_work.append(row[11])
            ieor_class.append(row[12])
            ieor_study.append(row[13])
            ieor_work.append(row[14])
            stat_class.append(row[15])
            stat_study.append(row[16])
            stat_work.append(row[17])
            cs_study.append(row[18])
            cs_work.append(row[19])
            lab_prep.append(row[20])

    except:
        print("Error: unable to fetch data")
    
    # Disconnect from server
    db.close()
    cursor.close()

    # create a dataframe with our lists
    data = {'day_id' : day_id,
            'date' : date,
            'dow' : dow,
            'sleep' : sleep,
            'gym' : gym,
            'talentiq' : talentiq,
            'reading' : reading,
            'fun' : fun,
            'econ_class' : econ_class,
            'econ_study' : econ_study,
            'econ_work' : econ_work,
            'ieor_class' : ieor_class,
            'ieor_study' : ieor_study,
            'ieor_work' : ieor_work,
            'stat_class' : stat_class,
            'stat_study' : stat_study,
            'stat_work' : stat_work,
            'cs_study' : cs_study,
            'cs_work' : cs_work,
            'lab_prep' : lab_prep
            }

    pandas_dataframe = pd.DataFrame(data)
    # Pandas may alphabetize the order of your columns.

    return pandas_dataframe
