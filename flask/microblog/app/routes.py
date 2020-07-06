from app import flask_app 
from flask import render_template

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

