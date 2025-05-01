requests = [
    (
        "Отримати всі завдання певного користувача",
        "SELECT * FROM tasks WHERE user_id = ?",
        "Введіть id користувача, щоб отримати всі його завдання",
    ),
    (
        "Вибрати завдання за певним статусом",
        "SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = ?)",
        "Введіть статус завдання, щоб отримати всі завдання з цим статусом",
    ),
    (
        "Оновити статус конкретного завдання",
        "UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = ?) WHERE id = ?",
        "Введіть новий статус (new, in progress, completed) завдання, щоб оновити його",
        "Введіть id завдання, щоб оновити його статус",
    ),
    (
        "Отримати список користувачів, які не мають жодного завдання",
        "SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks)",
    ),
    (
        "Додати нове завдання для конкретного користувача",
        "INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, (SELECT id FROM status WHERE name = ?), ?)",
        "Введіть назву завдання",
        "Введіть опис завдання",
        "Введіть статус (new, in progress, completed)",
        "Введіть id користувача",
    ),
    (
        "Отримати всі завдання, які ще не завершено",
        "SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed')",
    ),
    (
        "Видалити конкретне завдання",
        "DELETE FROM tasks WHERE id = ?",
        "Введіть id завдання, щоб видалити його",
    ),
    (
        "Знайти користувачів з певною електронною поштою",
        "SELECT * FROM users WHERE email LIKE ?",
        "Введіть частину email, наприклад: %example.com%",
    ),
    (
        "Оновити ім'я користувача",
        # "UPDATE users SET fullname = ? WHERE id = ?",
        "UPDATE users SET fullname = ? WHERE id = ? AND NOT EXISTS (SELECT 1 FROM users WHERE fullname = ? AND id != ?)",
        "Введіть нове ім’я користувача",
        "Введіть id користувача",
    ),
    (
        "Отримати кількість завдань для кожного статусу",
        "SELECT status.name, COUNT(tasks.id) as task_count FROM status LEFT JOIN tasks ON status.id = tasks.status_id GROUP BY status.name",
    ),
    (
        "Отримати завдання за доменом email",
        "SELECT tasks.* FROM tasks JOIN users ON tasks.user_id = users.id WHERE users.email LIKE '%' || '@' || ? GROUP BY tasks.user_id",
        "Введіть домен, наприклад: %@gmail.com%",
    ),
    (
        "Отримати список завдань, що не мають опису",
        "SELECT * FROM tasks WHERE description IS NULL OR description = ''",
    ),
    (
        "Користувачі та їхні завдання зі статусом 'in progress'",
        "SELECT users.fullname, tasks.title FROM tasks INNER JOIN users ON tasks.user_id = users.id INNER JOIN status ON tasks.status_id = status.id WHERE status.name = 'in progress'",
    ),
    (
        "Отримати користувачів та кількість їхніх завдань",
        "SELECT users.fullname, COUNT(tasks.id) as task_count FROM users LEFT JOIN tasks ON users.id = tasks.user_id GROUP BY users.id",
    ),
]
