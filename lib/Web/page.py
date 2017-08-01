import datetime
from flask import render_template, make_response, url_for, abort, request

class Page(object):
    def __init__(self, settings):
        self.settings = settings
        self.date = datetime.datetime.now()
        self.pages = self.settings["PAGES"]
        self.fbUrl = self.settings["FACEBOOK_URL"]
        self.siteName = self.settings["BOT_NAME"]

    def page(self, name):
        if name in self.pages.keys():
            self.title = self.getPageName(name)

            return render_template(
                self.getPageTemplate(name),
                data=self
            )
        else:
            abort(404)

    def getPageTemplate(self, name):
        return self.pages[name]["template"]

    def getPageName(self, name):
        return self.pages[name]["name"]

    def getUrlStatic(self, name):
        return url_for(
            "static",
            filename='css/' + name
        )

    def getUrl(self, page):
        if page == "/":
            return url_for("index")
        else:
            return url_for("page", page=page)

    def seCookies(self, name, value, page="/"):
        resp = make_response(render_template(page))
        resp.set_cookie(name, value)

        return resp

    def getCookies(self, name):
        return request.cookies.get(name)
