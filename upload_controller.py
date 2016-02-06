import web

render = web.template.render('templates/')

urls = (
    '/upload_page', 'upload_page'
)

class upload_page:
	def GET(self):
		return render.upload_page()
	def POST(self):
		data = web.input()
		print ("hello")

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()