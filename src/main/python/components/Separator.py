from core.LF import LifeCycle
from PyQt5.QtWidgets import QFrame
from PyQt5.QtGui import QColor

class Separator(QFrame, LifeCycle):
	parent = None

	def __init__(self, parent=None, coords={"x": 0, "y": 0, "width": 0, "height": 2}, **kwargs):
		super().__init__(parent=parent, objectName="Separator")
		self.parent = parent
		self.store = parent.store

		c = coords
		self.setGeometry(c['x'], c['y'], c['width'], c['height'])

	def render_(self):
		self.setFrameShape(QFrame.HLine)
		self.setFrameShadow(QFrame.Sunken)
		self.setObjectName("line")