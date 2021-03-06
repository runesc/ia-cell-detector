from core.LF import LifeCycle
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import pyqtSlot

from components.Input import Input

class IAView(QWidget, LifeCycle):
	parent = None
	store = None

	def __init__(self, parent=None, **kwargs):
		super().__init__(parent=parent, objectName="IA-view")
		parent.D_SIGNAL.connect(self.responsiveUI)
		self.parent = parent
		self.store = parent.store

	def render_(self):
		mensaje = Input(self, placeholder="Hola mundo")
		mensaje.resize(317, 43)


	def responsiveUI(self): pass