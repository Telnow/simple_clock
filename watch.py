import sys
import threading

from watch_logic import Watch_logic
from PySide6.QtWidgets import QApplication


class Watch_programm(Watch_logic):
    def __init__(self):
        super().__init__()
        self.main_interface()
        threading.Thread(target=self.start_watch, daemon=True).start()


if __name__ == '__main__':
    app = QApplication()
    window = Watch_programm()
    window.show()
    sys.exit(app.exec())
