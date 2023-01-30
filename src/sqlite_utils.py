import sqlite3


def insert_index_as_table(dbPath, indexName, index):
    # Connect to database
    sqliteConnection = sqlite3.connect(dbPath)
    cursor = sqliteConnection.cursor()

    # Convert dict to list of tuples
    index_tuple_list = [(k, str(v)) for k, v in index.items()]

    cursor.execute('''CREATE TABLE IF NOT EXISTS ''' + indexName + ''' (id TEXT, topic TEXT)''')
    # Insert into database
    Delete_all_rows = """delete from """ + indexName
    cursor.execute(Delete_all_rows)
    try:
        cursor.executemany('INSERT INTO '+ indexName + ' VALUES (?,?)', index_tuple_list)
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    sqliteConnection.commit()
    cursor.close()
    sqliteConnection.close()
