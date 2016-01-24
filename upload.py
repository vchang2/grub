import web

render = web.template.render('templates/')

urls = (
    '/(.*)', 'upload', '/upload', 'steps', '/steps'
)

instructions = []
for i in range(6):
	instructions.append("THIS IS A STEP")

class upload:
	def GET(self, name):
		print "IN UPLOAD"
		return render_template('upload.html', instructions)

class steps:
	def GET(self):
		print "I AM PRINTING"
		instructions.append("I ADDED A NEW STEP")
		return render_template('upload.html', instructions)

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
	app = web.application(urls, globals())
	app.run()