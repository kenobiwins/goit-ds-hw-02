from connect import create_connection
from execute_sql_script import execute_sql_script
from seed import seed_data

database = "./db/db.sqlite"


def main() -> None:
    with create_connection(database) as connection:
        if connection is not None:
            execute_sql_script(connection, "./scripts/create_users_table.sql")
            execute_sql_script(connection, "./scripts/create_status_table.sql")
            execute_sql_script(connection, "./scripts/create_tasks_table.sql")
            with connection:
                seed_data(connection)

if __name__ == '__main__':
    main()
