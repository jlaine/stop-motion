#!/usr/bin/env python

from __future__ import print_function

import logging
import os
import sys

import gphoto2 as gp

output_dir = 'images'
output_tpl = 'capt%.4d.jpg'


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
        format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)

    # create directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # open camera
    gp.check_result(gp.use_python_logging())
    camera = gp.check_result(gp.gp_camera_new())
    try:
        gp.check_result(gp.gp_camera_init(camera))
    except gp.GPhoto2Error as exc:
        logging.warning("Could not open camera: %s", exc)
        sys.exit(1)

    while True:
        try:
            input('Press a key to capture image')
        except KeyboardInterrupt:
            return

        print('Capturing image')
        file_path = gp.check_result(gp.gp_camera_capture(
            camera, gp.GP_CAPTURE_IMAGE))
        target = next_filename()
        print('Copying image to', target)
        camera_file = gp.check_result(gp.gp_camera_file_get(
            camera, file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL))
        gp.check_result(gp.gp_file_save(camera_file, target))
    gp.check_result(gp.gp_camera_exit(camera))


if __name__ == "__main__":
    main()
