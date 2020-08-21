from flask import Flask,render_template, request
import requests
import json
import random
import webbrowser
app = Flask(__name__)
correct_ans = "Arpit"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/googlesearch', methods=["POST"])
def googlesearch():
    try:
        data = request.form["Search"]
        data = data.replace(" ", '+')
        webbrowser.open(f"https://www.google.com/search?q={data}")
        print(data)
        return render_template('quiz.html',data=data)
    except Exception as e:
        print("ERRORRRR" ,e)
        return "error"

@app.route('/quiz',methods=["POST"])
def quiz():
    category = request.form['option']
    # getting category codes from OPEN TRIVIA DB
    umap ={"History": "23", "Mathematics": "19", "Computer Science": "18", "General Knowledge" : "9", "Sports":"21"}
    url = f"https://opentdb.com/api.php?amount=1&category={umap[category]}"
    json_obj = requests.get(url)
    data = json.loads(json_obj.text)
    x = data['results'][0]
    question = x['question']
    if '&quot;' in question:
        question = question.replace('&quot;', "")
    if '&#039;' in question:
        question = question.replace("&#039;","'")
    all_answer = x['incorrect_answers']+[x['correct_answer']]
    global correct_ans
    correct_ans = str(x['correct_answer'])
    return render_template('quiz.html', all_answer=all_answer, question=question, correct_ans=correct_ans )


@app.route('/verify', methods=["POST"])
def verify():
    try:
        option = request.form['option']
        correct = correct_ans == option
        return render_template('quiz.html',option=correct,correct=correct_ans)
    except Exception as e:
        print("ERROR ", e)
        return "ERROR"


@app.route('/result')
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)