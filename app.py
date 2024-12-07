from flask import Flask,render_template
app = Flask(__name__)
JOBS=[
        {
            'id':1,
            'name':'Ganesh',
            'salary':'Rs. 150000'
        },
        {
            'id':2,
            'name':'Om',
            'salary':'Rs. 160000'
        },
        {
            'id':3,
            'name':'Ajinkya',
            'salary':'Rs. 170000'
        }
    ]
@app.route("/")
def index():
    return render_template('home.html',jobs=JOBS,company="GM(Code Crafter)")
if __name__=="__main__":
    app.run(debug=True)