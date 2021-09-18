from pathlib import Path
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QWidget
from PyQt5.QtCore import Qt, pyqtSignal

from core.LF import LifeCycle
from core.IA import NeuralNetwork
from components.Navbar import Navbar
from views.IA import IAView
from views.Trainer import TrainerView
from views.Config import ConfigView


import sys


class Main(QMainWindow, LifeCycle, NeuralNetwork, ApplicationContext):
	D_SIGNAL = pyqtSignal()
	store = {
		'PATH': str(Path.home()) + '/AIDemo/',
		'APPCTX': ApplicationContext(),
		'appVersion': ApplicationContext().build_settings['version'],
		'd-size': {},
		'SM' : None
	}

	def __init__(self):
		super().__init__()
		self.setPath(self.store['PATH'])
		self.showPath()

	def render_(self):
		navbar = Navbar(self)

		# Aqui se configuran las vistas de la app
		self.container = QWidget(self, objectName="View-container")
		self.sm = QStackedWidget(self.container, objectName="screen-manager")

		for view in [IAView, TrainerView, ConfigView]:
			self.sm.addWidget(view(self))
		self.sm.setCurrentIndex(1)

		# Esto permite que otros componentes puedan hacer switch entre vistas
		self.store['SM'] = self.sm

	def responsiveUI(self):
		self.container.resize(self.pct(85, self.width()), self.height())
		self.container.move(self.pct(15, self.width()), 0)
		self.sm.resize(self.container.width(), self.height())

	def loadCSS(self):
		stylesheet = self.store['APPCTX'].get_resource('CSS/index.css')
		with open(stylesheet, "r") as styles:
			self.setStyleSheet(styles.read())

	def resizeEvent(self, e):
		self.store['d-size'].update({'width': self.width(), 'height': self.height()})
		self.resize(self.width(), self.height())
		self.D_SIGNAL.emit()
		self.responsiveUI()

if __name__ == '__main__':
	appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
	window = Main()
	window.setMinimumSize(640, 480)
	window.resize(1200, 700)
	window.show()
	exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
	sys.exit(exit_code)