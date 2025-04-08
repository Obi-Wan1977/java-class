from flask import Flask, render_template, request
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


@app.route('/results', methods=["POST"])
def results():
   color = request.form['color']
   luck_num = request.form['luck_num']
   fav_class = request.form['fav_class']
   best_pix = request.form['best_pix'].lower().strip()
   films = ["toy story","a bug's life","toy story 2","monsters, inc.",
      "finding nemo", "the incredibles","cars","ratatouille","wall-e","up",
      "toy story 3","cars 2", "brave","monsters university","inside out",
      "the good dinosaur","finding dory", "cars 3","coco","incredibles 2",
      "toy story 4","onward","soul"]
   colors = ["red", "orange", "yellow", "green", "blue", "purple"]
   if best_pix not in films:
      best_pix = "Sorry, '{0}' isn't a Pixar film.".format(best_pix.title())
   else:
      best_pix = best_pix.title()

   if color not in colors:
      color = "Sorry, '{0}' isn't a color option.".format(color.title())
   else:
      color = color.title()

   return render_template('form_results.html', color = color, luck_number = luck_num, fav_class = fav_class, best_pix = best_pix)


if __name__ == '__main__':
   app.run()