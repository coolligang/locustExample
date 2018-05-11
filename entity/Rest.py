# encoding:utf-8

class Rest:

    def __init__(self, method, url):
        self.method = str(method).upper()
        self.url = url

    def getMethod(self):
        return self.method

    def getUrl(self):
        return self.url

    def setParams(self, params):
        self.params = params

    def getparams(self):
        return self.params

    def setForm(self, form):
        self.form = form

    def getForm(self):
        return self.form

    def setJson(self, _json):
        self._json = _json

    def getJson(self):
        return self._json

    def setHeaders(self, headers):
        self.headers = headers

    def getHeaders(self):
        return self.headers

    def setCookies(self, cookies):
        self.cookies = cookies

    def getCookies(self):
        return self.cookies

    def setExcepts(self, excepts):
        self.excepts = excepts

    def getExcepts(self):
        return self.excepts
