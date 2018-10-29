import sys
# p = "/Library/Python/2.7/site-packages"
# sys.path.append(p)
from vedis import Vedis
import ast

class Base(object):
    __slots__ = [
        "db"
    ]
    def __init__(self, **kwargs):
        self.db = Vedis(kwargs["dataFile"])

    def get(self, user_id):
        try:
            data = self.db[user_id]

            return ast.literal_eval(data)
        except KeyError:
            return None

    def set(self, user_id, shop, value):
        try:
            data = self.get(user_id)

            if not data:
                data = dict()

            data[shop] = value

            self.db[user_id] = data

            return True
        except:
            return False
