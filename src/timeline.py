import os


class Timeline:
    def __init__(self, directory, template="capt%.4d.jpg"):
        self._directory = directory
        self._template = template

        # create directory
        if not os.path.exists(self._directory):
            os.makedirs(self._directory)

    def next_filename(self):
        # check existing files
        filenames = frozenset(os.listdir(self._directory))
        counter = 1
        while True:
            filename = self._template % counter
            if filename not in filenames:
                return os.path.join(self._directory, filename)
            counter += 1
