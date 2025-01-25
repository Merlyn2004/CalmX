from flask import Flask, jsonify, request, render_template
from flask_cors import CORS  # To enable CORS if you are using a separate front-end

app = Flask(__name__,template_folder='CALMX')
CORS(app)

# In-memory storage for tasks (you can replace this with a database in production)
tasks = []

# Route to serve the main page
@app.route('/')
def index():
    return render_template('index.html')  # Your front-end HTML file

# Route to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Route to add a task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task')
    
    if task:
        tasks.append({'task': task})
        return jsonify({'message': 'Task added successfully!'}), 201
    else:
        return jsonify({'error': 'No task provided!'}), 400

# Route to delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        return jsonify({'message': 'Task deleted successfully!'})
    else:
        return jsonify({'error': 'Task not found!'}), 404

# Route to update Pomodoro timer settings (optional, can be expanded)
@app.route('/pomodoro', methods=['POST'])
def set_pomodoro():
    data = request.get_json()
    study_time = data.get('study_time', 25)  # default 25 minutes
    break_time = data.get('break_time', 5)   # default 5 minutes
    
    # Ideally, you can save these settings to a database for each user
    return jsonify({'study_time': study_time, 'break_time': break_time})

if __name__ == '__main__':
    app.run(debug=True)
