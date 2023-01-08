from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

books_list = [
     {
         "id": 0,
         "author":"Islamic book", 
         "language":"Arabic",
         "title":"Quran",
     },
     {
         "id": 1,
         "author":"Islamic book", 
         "language":"Arabic",
         "title":"Ahadeees",
     },
]

@app.route('/')
def index():
    return '<h1 style="color: blue; text-align: center; text-decoration: underline;">Hello Are you excited to go through this api</h1><br><h3>please stay tuned, this will be a book library</h3>'

@app.route('/<name>')
def print_name(name):
    return"<h1 style='color: blue; text-align: center; text-decoration: underline;'>Hi, {}</h1>".format(name)

@app.route('/books', methods=['GET', 'POST'])
def book_name():
        #return'<h1 style="color: blue; text-align: center; text-decoration: underline;">Helle Esmani SKRR</h1><br><a href="/" style="color: blue; text-align: center; text-decoration: none; font-size: bolder;">click here</a><button formmethod="get">Get</button>'
        #  if request.method == 'GET':
        #     if len(books_list) > 0:
        #        return jsonify(books_list)
        #     else:
        #        'Nothing Found', 404
        return'<h1 style="color: blue; text-align: center; text-decoration: underline;">Helle Esmani SKRR</h1><br><a href="/" style="color: blue; text-align: center; text-decoration: none; font-size: bolder;">click here</a>'

        if request.method == 'POST':
            new_author = request.form('author')
            new_lang = request.form('language')
            new_title = request.form('title')
            iD = books_list[-1]['id'] + 1

            new_obj = {
                "id": iD,
                "author":new_author, 
                "language":new_lang,
                "title":new_title,
                }
            books_list.append(new_obj)
            return jsonify(books_list),201

@app.route('/contact')
def contact_page():
    return render_template('./form.html')
    # return"<h1>hello</h1>"


@app.route('/result')
def result_page():
    return render_template('result.html', firstname=request.args['firstname'], lastname=request.args['lastname'], country=request.args['country'], subject=request.args['subject'])
    

if __name__ == '__main__':
    app.run(debug=True)