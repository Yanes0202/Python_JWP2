from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug = True)