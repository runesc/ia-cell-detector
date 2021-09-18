from core.LF import LifeCycle
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class Button(QPushButton, LifeCycle):
	parent = None

	def __init__(self, parent=None, objectName="btn-link", text="", **kwargs):
		super().__init__(parent=parent, objectName=objectName, text=text)
		self.parent = parent
		self.store = parent.store

	def render_(self):
		self.setCursor(Qt.PointingHandCursor)
