"""   import the flask libraries to create app"""
from flask import Flask,render_template,request,redirect
import string
import random


"""initiated the app"""
app = Flask(__name__)



""" function to create short url
     input=list of already existed url
     returns-three random letters"""
def short_urlfn(short_url):
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=3)
        rand_letters = "".join(rand_letters)
        if rand_letters not in short_url:
            return rand_letters

"""declaring  2 list to store long and short urls"""
long_url=[]
lstshort_url=[]


""" index route from which we can receive long url"""
@app.route('/',methods=['GET','POST'])
def index():

    if request.method=='POST':
        received_url=request.form['nm']
        if received_url in long_url:
            return lstshort_url[long_url.index(received_url)]

        else:
            shorten_url=short_urlfn(lstshort_url)
            lstshort_url.append(shorten_url)
            long_url.append(received_url)
            return shorten_url

    else:
        return render_template('home.html')

"""route to redirect to long url if short url provided """
@app.route('/<short_url>')
def redirection(short_url):
    if short_url in lstshort_url:
        return redirect(long_url[lstshort_url.index(short_url)])
    else:
        return f'<h1>Url doesnt exist</h1>',400


if __name__ == "__main__" :
    app.run(host="0.0.0.0",port=5000,debug=True)