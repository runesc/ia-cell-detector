from core.LF import LifeCycle
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt5.QtCore import pyqtSlot

from components.Button import Button
from components.Input import Input

class TrainerView(QWidget, LifeCycle):
	parent = None
	store = None

	def __init__(self, parent=None, **kwargs):
		super().__init__(parent=parent, objectName="Trainer-view")
		parent.D_SIGNAL.connect(self.responsiveUI)
		self.parent = parent
		self.store = parent.store
		self.parent.showPath()


	def render_(self):
		self.title = QLabel("Trainer", self,  objectName="Title")
		self.subtitle = QLabel("Entrenar la red neuronal para poder reconocer objetos y figuras dentro de muestras en tiempo real o imagenes", self,  objectName="Subtitle", wordWrap=True)
		self.label_folder = QLabel("Selecciona la carpeta/imagen para entrenar", self, objectName="Subtitle")
		layout = QHBoxLayout()
		self.container = QWidget(self)
		self.container.setLayout(layout)
		buttons = [
			Button(self, text="Seleccionar Carpeta", objectName="btn-primary"),
			Button(self, text="Seleccionar Archivo", objectName="btn-primary")
		]
		for button in buttons: layout.addWidget(button)
		self.label_obj_name = QLabel("Nombre del objeto (de esta manera lo reconocerá la IA)", self, objectName="Subtitle")
		self.obj_name = Input(self, placeholder="Ej: Linfocitos", objectName="Input")

		self.train_neural_network = Button(self, text="Entrenar red neuronal", objectName="btn-primary")


	def componentDidMount(self):
		self.train_neural_network.clicked.connect(lambda: self.parent.test_camera())

	def responsiveUI(self):
		if(self.parent):
			# Constants
			ADJUSTED_WIDTH = self.pct(2.4, self.parent.height())
			FULL_WIDTH = self.parent.width()
			FULL_HEIGHT = self.parent.height()
			# End Constants

			self.resize(self.parent.frameSize())

			self.title.resize(FULL_WIDTH, self.title.height())
			self.title.move(self.pct(2, FULL_HEIGHT), self.pct(2, FULL_HEIGHT))

			self.subtitle.resize(FULL_WIDTH, 100)
			self.subtitle.move(ADJUSTED_WIDTH, self.pct(2.5, FULL_HEIGHT))

			self.label_folder.resize(FULL_WIDTH, 100)
			self.label_folder.move(ADJUSTED_WIDTH, self.pct(25, FULL_HEIGHT))

			self.container.resize(self.pct(35, FULL_WIDTH), self.pct(10, FULL_HEIGHT))
			self.container.move(self.pct(0.5, FULL_HEIGHT), self.pct(35, FULL_HEIGHT))

			self.label_obj_name.resize(FULL_WIDTH, 100)
			self.label_obj_name.move(ADJUSTED_WIDTH, self.pct(10, FULL_HEIGHT))

			self.obj_name.resize(317, 43)
			self.obj_name.move(ADJUSTED_WIDTH, self.pct(21, FULL_HEIGHT))

			self.train_neural_network.move(self.pct(71, FULL_WIDTH - self.train_neural_network.width()/2) , FULL_HEIGHT - 55)
