from faker import Faker

fake = Faker()

def insert_user(connection, fullname, email):
    query = "INSERT INTO users (fullname, email) VALUES (?, ?)"
    connection.execute(query, (fullname, email))


def insert_status(connection, name):
    query = "SELECT id FROM status WHERE name = ?"
    existing_status = connection.execute(query, (name,)).fetchone()

    if existing_status is None:  
        query = "INSERT INTO status (name) VALUES (?)"
        connection.execute(query, (name,))
    else:
        print(f"Status '{name}' already exists.")


def insert_task(connection, title, description, status_id, user_id):
    query = """
    INSERT INTO tasks (title, description, status_id, user_id)
    VALUES (?, ?, ?, ?)
    """
    connection.execute(query, (title, description, status_id, user_id))


def seed_data(connection):
    statuses = ["pending", "in_progress", "completed"]
    for status in statuses:
        insert_status(connection, status)

    users = []
    for _ in range(10):  
        fullname = fake.name()
        email = fake.unique.free_email()
        users.append((fullname, email))
        insert_user(connection, fullname, email)

    status_ids = [
        row[0] for row in connection.execute("SELECT id FROM status").fetchall()
    ]
    user_ids = [row[0] for row in connection.execute("SELECT id FROM users").fetchall()]

    for _ in range(20):  
        title = fake.sentence(nb_words=6)
        description = fake.text(max_nb_chars=200)
        status_id = fake.random.choice(status_ids)
        user_id = fake.random.choice(user_ids)
        insert_task(connection, title, description, status_id, user_id)

    print("Database seeding completed.")
