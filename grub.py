import sys; sys.path.insert(0, 'lib') # this line is necessary for the rest
import os                             # of the imports to work!

import web
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import sqlitedb
        
urls = (
    '/(.*)', 'hello', '/hello', 'upload', '/upload'
)
app = web.application(urls, globals())

class hello:        
    def GET(self, name):
        #sqlitedb.addUser('adam', 111)
        users_search_results = sqlitedb.getUsers()
    	return render_template('curr_time.html', users = users_search_results)
        return 'Grub! Personalized cooking suggestions'

class upload:
    def POST(self):
        post_params = web.input()
        itemID = post_params['itemID']

# helper method to render a template in the templates/ directory
#
# `template_name': name of template file to render
#
# `**context': a dictionary of variable names mapped to values
# that is passed to Jinja2's templating engine
#
# See curr_time's `GET' method for sample usage
#
# WARNING: DO NOT CHANGE THIS METHOD
def render_template(template_name, **context):
    extensions = context.pop('extensions', [])
    globals = context.pop('globals', {})

    jinja_env = Environment(autoescape=True,
            loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
            extensions=extensions,
            )
    jinja_env.globals.update(globals)

    web.header('Content-Type','text/html; charset=utf-8', unique=True)

    return jinja_env.get_template(template_name).render(context)

if __name__ == "__main__":
    app.run()