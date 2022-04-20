
from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = "keep it secret and safe"

@app.route('/')
def index():
    if 'views' not in session:
        session['views'] = 0
    else:
        session['views'] = session['views'] + 1
    print(request.form)
    return render_template("index.html")


@app.route('/destroy_session', methods = ['POST'])
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/add_two')
def add_two():
    # session['views'] = int(request.form['views'])
    # if 'views' in session:
    #     session['views'] + 2

    session['views'] += 1
    return redirect('/')


# @app.route('/display')
# def display():
#     print(session)
#     return render_template("display.html")



if __name__ == "__main__":
    app.run(debug = True, port = 5000)