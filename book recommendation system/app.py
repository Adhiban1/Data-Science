from flask import Flask, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)
db = sqlite3.connect('test.db', check_same_thread=False)
cursor = db.cursor()

@app.route('/')
def home():
    cursor.execute('select * from todolist')
    tasks = list(cursor.fetchall())
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_list():
    if request.method == 'POST':
        cursor.execute('insert into todolist (item) values (\'{}\')'.format(request.form.get('taskname')))
        db.commit()
    return redirect(url_for('home'))

@app.route('/delete/<int:index>', methods=['GET'])
def delete(index):
    cursor.execute('delete from todolist where id = {}'.format(index))
    db.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)