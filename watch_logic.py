import time

from interface import Watch_interface


class Watch_logic(Watch_interface):

    def start_watch(self):
        while True:
            time.sleep(1)
            self.label.setText(time.strftime('%H:%M:%S'))
