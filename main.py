import PyQt5
from PyQt5 import QtWidgets
from qtwidgets import AnimatedToggle

toggle_2 = AnimatedToggle(
    checked_color="#FFB000",
    pulse_checked_color="#44FFB000"
)

container = QtWidgets.QWidget()
layout = QtWidgets.QVBoxLayout()
layout.addWidget(toggle_2)
container.setLayout(layout)


app = QtWidgets.QApplication([])
app.exec_()
