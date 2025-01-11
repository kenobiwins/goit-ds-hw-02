SELECT * FROM tasks WHERE user_id = 1;--Отримати всі завдання певного користувача--

SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'completed');--Вибрати завдання за певним статусом--

UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'pending') WHERE id = 1 ;--Оновити статус конкретного завдання--

SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT  user_id FROM tasks); --Отримати список користувачів, які не мають жодного завдання--

INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('learn sql','for a reason',1,1) ; --Додати нове завдання для конкретного користувача--

SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');--Отримати всі завдання, які ще не завершено--

DELETE FROM tasks WHERE id=1; --Видалити конкретне завдання--

SELECT * FROM users WHERE email LIKE '%@gmail.com'; --Знайти користувачів з певною електронною поштою--

UPDATE users SET fullname  = 'hello world' WHERE id = 2; --Оновити ім'я користувача--

SELECT status.name , COUNT(tasks.id) as tasks_count 
FROM status 
LEFT JOIN tasks ON status.id = tasks.status_id
GROUP BY status.name; --Отримати кількість завдань для кожного статусу--

SELECT tasks.*
FROM tasks
JOIN users ON tasks.user_id = users.id
WHERE users.email LIKE '%@example.com';

SELECT * FROM tasks WHERE description IS NULL; -- Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти--

SELECT users.fullname, tasks.title, tasks.description
FROM users
INNER JOIN tasks ON users.id = tasks.user_id
WHERE tasks.status_id = (SELECT id FROM status WHERE name = 'in_progress'); -- Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. 

SELECT users.fullname, COUNT(tasks.id) AS task_count
FROM users
LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.fullname; --Отримати користувачів та кількість їхніх завдань