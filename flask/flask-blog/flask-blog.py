from flask import Flask, render_template

app = Flask(__name__)

posts = [
        {
            'name': 'xyz',
            'post_date': '9/12/2018',
            'text': 'dummy first post'            
        },
        {
            'name': 'abc',
            'post_date': '18/09/2016',
            'text': 'dummy second post'            
        },
        {
            'name': 'one two three',
            'post_date': 'none',
            'text': 'dummy third post'            
        }
]

@app.route("/")
@app.route("/home")

def hello():
    return render_template('home.html', posts_to_render=posts)

@app.route("/know-me")
def me():
    return "<h2>dude what's up</h2>"

@app.route("/contact")
def meet():
    return "<h3>meet me at ....</h3>"

if __name__ == "__main__":
    print('running flask app ....')
    app.run(debug=True)




