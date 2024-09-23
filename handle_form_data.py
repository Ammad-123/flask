from flask import Flask,request

app = Flask(__name__)

@app.route('/submit',methods=['POST'])
def submit():
    username=request.form['username']
    age = int(request.form['age'])
    
    return f"hello,{username}, your age is {age}"

if __name__== '__main__':
    app.run(debug=True)