import subprocess

import gphoto2 as gp
from PySide2.QtCore import QObject, Slot


class CameraNotFound(Exception):
    pass


class FfmpegCamera(QObject):
    @Slot(str)
    def capture(self, path):
        subprocess.check_call(
            [
                "ffmpeg",
                "-loglevel",
                "fatal",
                "-f",
                "v4l2",
                "-i",
                "/dev/video0",
                "-frames:v",
                "1",
                path,
            ]
        )

    def close(self):
        pass


class Gphoto2Camera(QObject):
    def __init__(self):
        super().__init__()

        gp.check_result(gp.use_python_logging())

        try:
            self._camera = gp.check_result(gp.gp_camera_new())
            gp.check_result(gp.gp_camera_init(self._camera))
        except gp.GPhoto2Error:
            raise CameraNotFound

    @Slot(str)
    def capture(self, path):
        file_path = gp.check_result(
            gp.gp_camera_capture(self._camera, gp.GP_CAPTURE_IMAGE)
        )
        camera_file = gp.check_result(
            gp.gp_camera_file_get(
                self._camera, file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL
            )
        )
        gp.check_result(gp.gp_file_save(camera_file, path))

    def close(self):
        gp.check_result(gp.gp_camera_exit(self._camera))
