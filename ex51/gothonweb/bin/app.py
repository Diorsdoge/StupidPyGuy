# -- coding: utf-8 --

import web

urls = (
	'/hello', 'index'
	)

app = web.application(urls, globals())

render = web.template.render('templates/', base = "layout")

class index(object):

	def GET(self):
		return render.hello_form()

	def POST(self):
		form  = web.input(name = "Nobody", greet = "Hello")
		if form.greet:
			greeting = "%s, %s" % (form.greet, form.name)
			return render.index(greeting = greeting)
		else:
			return "EORROR: greet is required."

if __name__ == "__main__":
	app.run()