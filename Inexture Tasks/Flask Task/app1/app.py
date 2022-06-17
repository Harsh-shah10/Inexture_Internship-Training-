from flask import Flask, redirect,render_template,request,flash, url_for

app = Flask(__name__)
app.secret_key='fsdfsfsf2342'

@app.route('/')
def index():
    flash("What's your name ?")
    return render_template('index.html')

@app.route('/greet',methods=['POST','GET'])
def greet():
    if request.method == 'GET' and request.args.get('name_input')!='': 
        #print(f"REQUEST {request.args}")
        #print(request.args.get('name_input')=='')
        flash(f"HI {request.args.get('name_input')}. So! Happy to see you!!")
        return render_template('index.html') 
    return redirect(url_for('index'))

if __name__==('__main__'):
    app.run(debug=True)