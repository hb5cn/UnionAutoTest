# !/usr/local/python
# -*- coding: UTF-8 -*-
import os


class Screen(object):
    """
    截图功能的装饰器
    """
    def __init__(self, driver, test_method_name):
        self.driver = driver
        self.test_method_name = test_method_name

    def __call__(self, f):
        def inner(*args):
            try:
                return f(*args)
            except Exception:
                import time
                nowtime = time.strftime("%Y%m%d%H%M%S")
                png_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                        'Screenshots', '%s_%s.png' % (self.test_method_name, nowtime))

                self.driver.get_screenshot_as_file(png_path)
                raise
        return inner
