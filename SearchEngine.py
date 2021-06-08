'''Creating a simple search engine UI'''
from flask import Flask,render_template,request
from ranking import ranker

app = Flask(__name__)

# web page rendering
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        query = request.form.get('query')
        return render_template('index.html',posts=ranker(query),q=query)
    return render_template('index_one.html')


if __name__=='__main__':
    app.run()
