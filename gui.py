#!/usr/bin/env python

import os
import sys

from PySide2.QtCore import QUrl
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

from src.camera import CameraNotFound, FfmpegCamera, Gphoto2Camera
from src.timeline import Timeline

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()

try:
    camera = Gphoto2Camera()
except CameraNotFound:
    camera = FfmpegCamera()

timeline = Timeline(os.path.abspath("images"))

context = engine.rootContext()
context.setContextProperty("camera", camera)
context.setContextProperty("timeline", timeline)

engine.load(QUrl("src/qml/MainWindow.qml"))
engine.quit.connect(app.quit)
app.exec_()

camera.close()
