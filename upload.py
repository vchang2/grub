import web

render = web.template.render('templates/')

urls = (
    '/(.*)', 'upload'
)

class upload:        
    def GET(self, name):
		return render.upload()

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()