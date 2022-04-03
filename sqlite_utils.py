import sqlite3


def insert_index_as_table(indexName, index):
    # Connect to database
    sqliteConnection = sqlite3.connect('D:/Research/Implementation/undergrad-research-indexing/dewey_db.db')
    cursor = sqliteConnection.cursor()

    # Convert dict to list of tuples
    index_tuple_list = [(k, v) for k, v in index.items()]

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

