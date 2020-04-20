#!/usr/bin/env python

import logging

from src.camera import FfmpegCamera, Gphoto2Camera
from src.timeline import Timeline


def main():
    logging.basicConfig(
        format="%(levelname)s: %(name)s: %(message)s", level=logging.INFO
    )

    camera = FfmpegCamera()
    timeline = Timeline(directory="images")

    while True:
        try:
            input("Press a key to capture image")
        except KeyboardInterrupt:
            return

        target = timeline.next_filename()
        logging.info("Capturing image to %s", target)
        camera.capture(target)

    camera.close()


if __name__ == "__main__":
    main()
