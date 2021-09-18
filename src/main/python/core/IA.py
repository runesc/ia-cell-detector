import cv2
import numpy as np
import os
from PyQt5.QtCore import QThreadPool, QRunnable

class Worker(QRunnable):
	def __init__(self, function, *args, **kwargs):
		super().__init__()

		self.function = function
		self.args = args
		self.kwargs = kwargs

class NeuralNetwork:
    def __init__(self):
        self.path = "/"
        self.cam = 0

        self.threadpool = QThreadPool()

        self.cap = cv2.VideoCapture(self.cam)
        self.cap.set(3,640) # set Width
        self.cap.set(4,480) # set Height

    def setPath(self, path):
        self.path = path

    def showPath(self):
        print(self.path)

    def stream_camera(self):
        worker = Worker(self.test_camera)
        self.threadpool.start(worker)

    def test_camera(self):
        while True:
            ret, frame = self.cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', frame)
            k = cv2.waitKey(30) & 0xff
            if k == 27: break
        self.cap.release()
        cv2.destroyAllWindows()

    def set_camera(self, CAM=0):
        self.cam = CAM

    def data_gathering(self, mode="real-time"): pass

    def trainer(self): pass