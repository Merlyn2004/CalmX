from flask import Flask, render_template, request, jsonify
import mysql.connector


app = Flask(__name__)

# Initialize SQLite Database
def init_db():
    conn = sqlite3.connect('database/calmexam.db')
    cursor = conn.cursor()

    # Table for Study Planner
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS study_planner (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            hours INTEGER NOT NULL
        )
    ''')

    # Table for Community Comments
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            comment TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Route: Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Route: Add Study Task
@app.route('/add_task', methods=['POST'])
def add_task():
    subject = request.form['subject']
    hours = request.form['hours']

    conn = sqlite3.connect('database/calmexam.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO study_planner (subject, hours) VALUES (?, ?)', (subject, hours))
    conn.commit()
    conn.close()

    return jsonify({"message": "Task added successfully!"})

# Route: Get Study Tasks
@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    conn = sqlite3.connect('database/calmexam.db')
    cursor = conn.cursor()
    cursor.execute('SELECT subject, hours FROM study_planner')
    tasks = cursor.fetchall()
    conn.close()

    return jsonify(tasks)

# Route: Add Comment
@app.route('/add_comment', methods=['POST'])
def add_comment():
    comment = request.form['comment']

    conn = sqlite3.connect('database/calmexam.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO comments (comment) VALUES (?)', (comment,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Comment added successfully!"})

# Route: Get Comments
@app.route('/get_comments', methods=['GET'])
def get_comments():
    conn = sqlite3.connect('database/calmexam.db')
    cursor = conn.cursor()
    cursor.execute('SELECT comment FROM comments')
    comments = cursor.fetchall()
    conn.close()

    return jsonify(comments)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
