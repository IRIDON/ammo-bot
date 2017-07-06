import datetime
from flask import render_template, url_for, abort

class Page(object):
    def __init__(self, settings):
        self.settings = settings
        self.date = datetime.datetime.now()
        self.pages = self.settings["PAGES"]
        self.fbUrl = self.settings["FACEBOOK_URL"]

    def page(self, name): 
        if name in self.pages.keys():
            return render_template(
                self.getPageTemplate(name),
                data=self
            )
        else:
            abort(404)

    def getPageTemplate(self, name):
        return self.pages[name]["template"]

    def getUrl(self, page):
        if page == "/":
            return url_for("index")
        else:
            return url_for("page", page=page)
