#!/usr/bin/env python

import logging
import os
import sys

from src.camera import FfmpegCamera, Gphoto2Camera

output_dir = "images"
output_tpl = "capt%.4d.jpg"


def next_filename():
    # check existing files
    filenames = frozenset(os.listdir(output_dir))
    counter = 1
    while True:
        filename = output_tpl % counter
        if filename not in filenames:
            return os.path.join(output_dir, filename)
        counter += 1


def main():
    logging.basicConfig(
        format="%(levelname)s: %(name)s: %(message)s", level=logging.INFO
    )

    # create directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    camera = Gphoto2Camera()

    while True:
        try:
            input("Press a key to capture image")
        except KeyboardInterrupt:
            return

        target = next_filename()
        logging.info("Capturing image to %s", target)
        camera.capture(target)

    camera.close()


if __name__ == "__main__":
    main()
