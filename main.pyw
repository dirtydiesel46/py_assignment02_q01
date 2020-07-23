from __future__ import division
import sys
from display import *

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.sunrise_time = QtCore.QTime(7, 44, 00)
        self.ui.lcdSunriseTime.display(self.sunrise_time.toString('hh:mm:ss'))
        self.sunset_time = QtCore.QTime(18, 1, 0)
        self.ui.lcdSunsetTime.display(self.sunset_time.toString('hh:mm:ss'))
        self.int_sunrise = self.sunrise_time.hour() * 3600 + self.sunrise_time.minute() * 60
        self.int_sunset = self.sunset_time.hour() * 3600 + self.sunset_time.minute() * 60

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.showTime()

    def showTime(self):
        current_time = QtCore.QTime.currentTime()
        text = current_time.toString('hh:mm:ss')
        self.ui.lcdCurrentTime.display(text)
        self.showLapsedTime()
        self.showTimeToSunset()

    def showLapsedTime(self):
        current_time = QtCore.QTime.currentTime()
        int_current_time = current_time.hour() * 3600 + current_time.minute() * 60 + current_time.second()

        # Display lapsed time
        if int_current_time >= self.int_sunrise:
            int_time_lapsed = int_current_time - self.int_sunrise
            self.ui.lcdTimeLapsed.display(self.returnQTimeObject(int_time_lapsed).toString('hh:mm:ss'))
        else:
            self.ui.lcdTimeLapsed.display(QtCore.QTime(0, 0, 0).toString('hh:mm:ss'))

    def showTimeToSunset(self):
        current_time = QtCore.QTime.currentTime()
        int_until_sunset = current_time.secsTo(self.sunset_time)

        # Display Time to Sunset
        if int_until_sunset >= 0:
            until_sunset = self.returnQTimeObject(int_until_sunset)
            self.ui.lcdUntilSunset.display(until_sunset.toString('hh:mm:ss'))
        else:
            total = 86400 - (current_time.hour() * 3600 + current_time.minute() * 60 + current_time.second()) + self.int_sunset
            time = self.returnQTimeObject(total)
            #self.ui.lcdUntilSunset.display(QtCore.QTime(0, 0, 0).toString('hh:mm:ss'))
            self.ui.lcdUntilSunset.display(time.toString('hh:mm:ss'))

    def returnQTimeObject(self, value):
        return QtCore.QTime(value // 3600, (value % 3600) // 60, (value %3600) % 60)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())