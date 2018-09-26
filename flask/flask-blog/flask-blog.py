from flask import Flask, render_template, url_for

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

from collections import namedtuple

User = namedtuple('User', 'name contact user_name')

dummy_user = User(name='ashiqul.islam', contact='013xxx', user_name='pollob')

@app.route("/")
@app.route("/home")

def hello():
    return render_template('home.html', posts_to_render=posts)

@app.route("/know-me")
def me():
    return render_template('know-me.html', me=dummy_user)

@app.route("/contact")
def meet():
    return "<h3>meet me at ....</h3>"

if __name__ == "__main__":
    print('running flask app ....')
    app.run(debug=True)




