from flask import Flask , render_template

app = Flask(__name__)

Jobs = [
  {
  'id':1,
  'title':'Data Analyst',
  'location':'Bengaluru, India',
  'salary':'Rs. 10,00,000'
},
{
  'id':2,
  'title':'Data science',
  'location':'Deihi, India',
  'salary':'Rs. 15,00,000'
} , 
{
   'id':4,
   'title':'front-end',
   'location':'Newyork , USA',
   'salary':'Dolar. 15,000'
}
  ]


@app.route("/")
def hello_world():
    return render_template("main.html" , jobs=Jobs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)