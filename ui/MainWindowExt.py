import traceback

from ui.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalsAndSlots()

    def setupSignalsAndSlots(self):
        self.pushButtonCalculate.clicked.connect(self.Cal)
        self.pushButtonClose.clicked.connect(self.process_close)
        self.pushButtonClear.clicked.connect(self.process_clear)

    def Cal(self):
        try:
            height = float(self.lineEditHeight.text())
            weight = float(self.lineEditWeight.text())
            status = Status(height, weight)
            bmi = BMI(height, weight)
            self.labelBMI.setText(f"{round(bmi, 1)}")
            self.labelComment.setText(f"{status}")
        except:
            traceback.print_exc()

    def process_clear(self):
        self.lineEditHeight.clear()
        self.lineEditWeight.clear()
        self.labelBMI.setText("")
        self.labelComment.setText("")

    def process_close(self):
        self.MainWindow.close()
