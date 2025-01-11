from sqlite3 import Error

def execute_sql_script(conn, sql_file_path):
    try:
        with open(sql_file_path, "r", encoding="utf-8") as file:
            sql_script = file.read()

        cursor = conn.cursor()
        cursor.executescript(sql_script)

        conn.commit()
        print(f"SQL script executed successfully from {sql_file_path}")
    except FileNotFoundError:
        print(f"File not found: {sql_file_path}")
    except Error as e:
        print(f"Error executing script: {e}")

