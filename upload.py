import web
import os
from web import form

from jinja2 import Environment, FileSystemLoader

render = web.template.render('templates/')

urls = (
    '/upload', 'upload', '/addSteps', 'addSteps'
)

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

instructions = []
for i in range(6):
	instructions.append("THIS IS A STEP")

'''
uploadForm = form.Form(
	form.Textbox('name'),
	form.Textarea('description', rows=4, cols=50),
	form.Textbox('time'),
	form.Textbox('servings')
)
'''

def getHelper():
	#return render_template('upload.html', instructions = instructions)
	#return render.upload(uploadForm, instructions)
	return render.upload(instructions)

class upload:
	def GET(self):
		return getHelper()

class addSteps:
	def GET(self):
		instructions.append("I ADDED A NEW STEP")
		return getHelper()

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()