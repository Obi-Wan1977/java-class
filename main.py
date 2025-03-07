from flask import Flask, render_template
# render_template("name_of_template.html")
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/form')
def form():
   return render_template("favorite_form.html")

@app.route('/')
def hello():
   message = "Hello, Flask!"
   return message

@app.route('/thanks')
def thanks():
      person = "Bob"
      shoes = "tapshoes"
      action = "dancing"
      being = "person"
      closing = "Sincerely,"
      name2 = "Caleb"
      return render_template("tynote.html", name = person, gift = shoes, verb = action, noun = being, closing_word = closing, author = name2)






if __name__ == '__main__':
   app.run()