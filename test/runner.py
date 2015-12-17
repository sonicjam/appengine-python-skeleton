#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest


def run():
    from tap import TAPTestRunner

    test_path = os.path.dirname(os.path.abspath(__file__))

    loader = unittest.TestLoader()
    tests = loader.discover(test_path)

    runner = TAPTestRunner()
    runner.set_stream(True)
    runner.run(tests)

if __name__ == '__main__':
    sys.path.insert(0, os.environ.get('GAE_SDK_PATH'))

    import dev_appserver
    dev_appserver.fix_sys_path()

    try:
        import appengine_config
        (appengine_config)
    except ImportError:
        print "Note: unable to import appengine_config."

    # lib/ 以下のローカルパッケージ読込に対応
    from google.appengine.ext import vendor
    vendor.add('lib')

    # .env による環境変数の設定
    from dotenv import load_dotenv
    load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

    run()
