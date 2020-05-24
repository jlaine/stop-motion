import os

from PySide2.QtCore import (
    Property,
    QFileSystemWatcher,
    QObject,
    QProcess,
    QUrl,
    Signal,
    Slot,
)


class Item(QObject):
    changed = Signal()

    def __init__(self, path, parent=None):
        super().__init__(parent=parent)
        self._name = os.path.basename(path)
        self._url = QUrl(path)

    @Property(str, notify=changed)
    def name(self):
        return self._name

    @Property(QUrl, notify=changed)
    def url(self):
        return self._url


class Timeline(QObject):
    changed = Signal()

    def __init__(self, directory, template="capt%.4d.jpg"):
        super().__init__()
        self._directory = directory
        self._filepaths = []
        self._items = []
        self._template = template

        # create directory
        if not os.path.exists(self._directory):
            os.makedirs(self._directory)

        # watch changes
        self._watcher = QFileSystemWatcher([directory], self)
        self._watcher.directoryChanged.connect(self._directoryChanged)
        self._directoryChanged(self._directory)

    @Property("QVariantList", notify=changed)
    def items(self):
        return self._items

    @Property(str, notify=changed)
    def nextFilePath(self):
        counter = 1
        while True:
            path = os.path.join(self._directory, self._template % counter)
            if path not in self._filepaths:
                return path
            counter += 1

    @Slot()
    def deleteLast(self):
        if self._filepaths:
            os.unlink(self._filepaths[-1])

    @Slot(str)
    def render(self, path):
        self._renderer = QProcess(self)
        self._renderer.finished.connect(self._rendererFinished)
        self._renderer.start(
            "ffmpeg",
            [
                "-r",
                "6",
                "-i",
                os.path.join(self._directory, self._template.replace("%.4d", "%04d")),
                "-vf",
                "scale=1404:-1",
                "-pix_fmt",
                "yuv420p",
                "-r",
                "24",
                "-strict",
                "-2",
                "-movflags",
                "faststart",
                "-y",
                path,
            ],
        )

    @Slot(str)
    def _directoryChanged(self, path):
        self._filepaths = sorted(
            [
                os.path.join(self._directory, name)
                for name in os.listdir(self._directory)
            ]
        )
        self._items = [Item(path, parent=self) for path in sorted(self._filepaths)]
        self.changed.emit()

    @Slot(int)
    def _rendererFinished(self, exitCode):
        print(self._renderer.readAllStandardError())
        print("exitCode", exitCode)
