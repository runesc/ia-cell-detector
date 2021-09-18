from core.LF import LifeCycle
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSlot

class Navbar(QWidget, LifeCycle):
	parent = None
	store = None

	def __init__(self, parent=None, **kwargs):
		super().__init__(parent=parent, objectName="Navbar")
		parent.D_SIGNAL.connect(self.responsiveUI)
		self.parent = parent
		self.store = parent.store

	def render_(self):
		self.container = QWidget(self, objectName="button-container")

		layout = QVBoxLayout()
		self.buttons = [QPushButton(text="IA", objectName="IA"), QPushButton(text="Trainer", objectName="Trainer"), QPushButton(text="Config", objectName="Config")]
		for x in self.buttons: layout.addWidget(x)
		self.container.setLayout(layout)

	def componentDidMount(self):
		if self.store:
			self.buttons[0].clicked.connect(lambda: self.store['SM'].setCurrentIndex(0))
			self.buttons[1].clicked.connect(lambda: self.store['SM'].setCurrentIndex(1))
			self.buttons[2].clicked.connect(lambda: self.store['SM'].setCurrentIndex(2))

			#for item in range(len(self.buttons)): self.buttons[item].clicked.connect(lambda: self.store['SM'].setCurrentIndex(item))


	def responsiveUI(self):
		if self.parent:
			self.resize(self.pct(15, self.parent.width()), self.parent.height())
			self.container.resize(self.width(), self.pct(40, self.height()))
			self.container.move(0, self.pct(5, self.height()))

			# Refrescar componente
			self.componentDidMount()
