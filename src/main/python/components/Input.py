from core.LF import LifeCycle
from PyQt5.QtWidgets import QLineEdit, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor

class Input(QLineEdit, LifeCycle):
	parent = None
	store = None

	baseShadow = QGraphicsDropShadowEffect(color=QColor(0, 0, 0, 255 * 0.1), blurRadius=5, xOffset=1, yOffset=2)
	focusShadow = QGraphicsDropShadowEffect(color=QColor(0, 0, 0, 255 * 0.1), blurRadius=4, xOffset=1, yOffset=3)

	currentShadow = True

	def __init__(self, parent=None,objectName="", **kwargs):
		super().__init__(parent=parent, objectName=objectName)
		self.parent = parent
		self.store = parent.store
		self.setPlaceholderText(kwargs['placeholder'])

	def render_(self):
		self.setGraphicsEffect(self.baseShadow)

	def mousePressEvent(self, event):
		self.setGraphicsEffect(self.focusShadow)
		self.currentShadow = True

	def switchShadow(self):
		self.currentShadow != self.currentShadow
		if self.currentShadow: self.setGraphicsEffect(self.focusShadow)
		else: currentShadow = self.setGraphicsEffect(self.base)