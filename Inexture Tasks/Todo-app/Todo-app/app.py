from flask import Flask, redirect, render_template, request, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

app = Flask(__name__)

# Add Database 
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost:5432/todoapp"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
app.config['SECRET_KEY'] = 'the random string'    

# initialize the database 
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# creating models for the db 
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Boolean)


@app.route('/')
def index():
    #all_tasks = Todo.query.all()
    incomplete_task = Todo.query.filter_by(complete=False).all()
    incomplete_status =True
    return render_template('index.html',all_tasks=incomplete_task,incomplete_status=incomplete_status)

@app.route('/add', methods=['POST'])
def add():
    if request.form['todoitem']!='':
        task = Todo(text=request.form['todoitem'],complete=False)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        flash('Field cannot be empty!!')
        return redirect(url_for('index'))


@app.route('/mark_complete/<int:id>')
def mark_complete(id):
    task_id = Todo.query.get_or_404(id)
    task_id.complete=True
    db.session.commit()
    return redirect('/')

@app.route('/completed_tasks')
def completed_tasks():
    complete_task = Todo.query.filter_by(complete=True).all()
    return render_template('index.html',all_tasks=complete_task)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)   
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.text = request.form['content']
        db.session.commit()
        return redirect('/')
    else:
        return render_template('update.html', task=task)

if __name__=='__main__':
    app.run(debug=True)