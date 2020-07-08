from app import flask_app 

# not used to with this syntax to import modules!
from app.forms import LoginForm

from flask import render_template, flash, redirect

@flask_app.route("/")
@flask_app.route("/index")

def index():
    # return render_template('index.html', title='Home', user={ 'username': 'miguel' })
    # return render_template('index.html', user={ 'username': 'miguel' })

    posts = [ {'author': { 'name':'miguel' }, 'body': 'QRT' }, { 'author': { 'name':'juan' }, 'body': 'RTS'} ]

    return render_template('index.html', user={ 'username': 'miguel' }, posts=posts)

# Author {{ post.author.name }} says {{ post.body }}

#   # ''' allows multi line string 

#   return '''
#       <html>

#           <head>
#               <title>
#                   Blog
#               </title>
#           </head>

#           <body>
#               Hello ''' + user['username'] + '''
#           </body>

#       </html>
#   '''

@flask_app.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()

    # we don't need to check for method in controller-action. only validate_on_submit is enough because submit happens only on POST method (PUT method too!)
    if form.validate_on_submit():

        # .data returns the data from the control. 
        # .label returns the label (textual representation). 
        # invoking the control as method returns the renderable HTML

        flash('Login requested for user {}. Remember me: {}'.format(form.user_name.data, form.remember_me.data))

        # both flash and redirect are flask methods
        return redirect('/index')

    return render_template('login.html', form=form, title='Sign In')

