import sqlite3
import ast


def load_table_to_dict(db_file: str, table_name: str):
    """
    This function loads the entire table from an SQLite database into a Python dict.

    Args:
    - db_file (str): The path to the SQLite database file.
    - table_name (str): The name of the table to be loaded.

    Returns:
    - data_dict (dict): A dictionary where the key is the 'id' and the value is the 'topic'
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    # Retrieve data from the table
    c.execute("SELECT * FROM {}".format(table_name))
    rows = c.fetchall()

    # Create a dictionary from the data
    data_dict = {row[0]: ast.literal_eval(row[1]) for row in rows}

    # Close the connection to the database
    conn.close()

    return data_dict