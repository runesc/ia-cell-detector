import logging
from pathlib import Path
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QPushButton

from core.LF import LifeCycle
from components.Navbar import Navbar


import sys


class Main(QMainWindow, LifeCycle, ApplicationContext):
    def __init__(self):
        super().__init__()
        self.store = {
            'PATH': str(Path.home()) + '/AIDemo/',
            'APPCTX': ApplicationContext(),
			'appVersion': self.build_settings['version'],
			'debug': True,
            'SM' : None
        }

    def render_(self): pass



if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = Main()
    window.resize(1200, 700)
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)