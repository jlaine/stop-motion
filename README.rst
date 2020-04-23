Stop-motion animation tools
===========================

Requirements
------------

Install FFmpeg and the gphoto2 development files:

  sudo apt-get install ffmpeg libgphoto2-dev

Next create a Python virtual environment and install required packages:

  python3 -m venv env
  source env/bin/activate
  pip install -r requirements.txt

Running
-------

Connect your camera using a USB cable then launch the graphical user interface:

  python3 gui.py

You can start capturing frames by pressing the "Capture" button or simply pressing
the "Return" key. The frame will be captured in the "images" directory and should
appear on the screen.

At any time you can delete the latest captured frame by pressing the "Delete" button
or the "Delete" key on your keyboard.

Once you have enough frames you can press the "Render" button which will output a
video at 5 frames per second.
