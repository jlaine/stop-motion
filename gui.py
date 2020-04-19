#!/usr/bin/env python

import sys

from PySide2.QtCore import QUrl
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.load(QUrl("src/view.qml"))
engine.quit.connect(app.quit)
sys.exit(app.exec_())
