import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Certified Kubernetes Adminstrator', 'The Certified Kubernetes Administrator (CKA) program provides assurance that CKAs have the skills, knowledge, and competency to perform the responsibilities of Kubernetes administrators.')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Azure DevOps Engineer (AZ-400)', 'The Azure DevOps engineer certification (Microsoft AZ-400) is an expert-level exam that certifies subject matter experts’ ability to work with processes and technology while also incorporating people skills to bring commercial value to clients.')
            )

connection.commit()