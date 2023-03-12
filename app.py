from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
  return '<h1> hello chaitanya</h1>'

app.run(host='0.0.0.0',debug=True)