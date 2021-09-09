from PyQt5.QtWidgets import QLabel, QWidget, QPushButton

from core.LF import LifeCycle

class Navbar(QPushButton):
	def __init__(self, parent=None, *args):
		super(Navbar, self).__init__()
		self.parent = parent