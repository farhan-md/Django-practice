import sqlite3
# creating database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# creating table if not exist
cursor.execute("" \
"CREATE TABLE IF NOT EXISTS students(" \
"id INTEGER PRIMARY KEY," \
"name TEXT," \
"major TEXT," \
"grade REAL)")

# INSERT students
students_data = [
    ("reza ahmadi","computer",14),
    ("mohsen reazei","psychology",18),
    ("zahra moradi","math",16),
    ("mehdi moosavi","electrical",15)
]

cursor.executemany("INSERT INTO students(name,major,grade) VALUES(?,?,?)",students_data)
conn.commit()

for item in cursor.execute("SELECT * FROM students"):
    print(item)

# UPDATE student grade
cursor.execute("UPDATE students SET grade =? WHERE name = ?",(19,"mehdi moosavi"))
conn.commit()

print("\n-------------The table after update----------------\n")
for item in cursor.execute("SELECT * FROM students"):
    print(item)

# DELETE student  from table
cursor.execute("DELETE FROM students WHERE name = ?",("reza ahmadi",))
conn.commit()

print("\n--------------------The table after delete---------------\n")
for item in cursor.execute("SELECT * FROM students"):
    print(item)

conn.close()
