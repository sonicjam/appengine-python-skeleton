#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import webapp2

# lib/ 以下のローカルパッケージ読込に対応
from google.appengine.ext import vendor
vendor.add('lib')

# .env による環境変数の設定
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))  # ファイル名が . 始まりだとエラーになる。


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
