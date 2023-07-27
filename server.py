from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
  return '<h1 style="color: red">Heyyyy Buddy......! Welcome to my Flask App Version 4 #####!</h1>'


app.run(port=3333, host="0.0.0.0", debug=True)
