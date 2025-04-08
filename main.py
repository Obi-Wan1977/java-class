from flask import Flask, render_template
render_template("name_of_template.html")
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/form')
def form():
   return render_template("favorite_form.html")

@app.route('/')
def hello():
   message = "Hello, Flask!"
   return message






if __name__ == '__main__':
   app.run()