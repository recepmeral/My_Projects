from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "I am gonna be a good DevOps and AWS Solution Architech"

@app.route('/second')
def second():
    return 'Re Re Re Ra Ra Ra Galatasaray Galatasaray Cimbombom'

@app.route('/third/subthird')
def third():
    return 'This is the subpage of third page'

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page is {id}'

if __name__=='__main__':
    app.run(debug=True,)