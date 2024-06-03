import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QLabel, \
    QLineEdit, QPushButton, QRadioButton, QSlider, QCheckBox
from PyQt5.QtCore import Qt
from lab_fraunhofer_ui import Ui_Form


class PhotoEffectExperiment(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Const
        self.R = 3.863
        self.U = 0
        self.dark_current = 0
        self.photo_current = 0
        self.distance = 20
        self.illumination = 500

        self.start_button.clicked.connect(self.start_experiment)
        self.distance_slider.valueChanged.connect(self.update_distance)
        self.voltage_input.textChanged.connect(self.calculate_current)
        self.dark_current_radio.toggled.connect(self.update_experiment_type)
        self.photo_current_radio.toggled.connect(self.update_experiment_type)

    def update_distance(self):
        value = self.distance_slider.value()
        self.distance_value_label.setText(f'{value} см')
        self.distance = value

    def get_voltage(self):
        try:
            self.U = float(self.voltage_input.text())
        except ValueError:
            self.U = 0

    def calculate_dark_current(self):
        if self.U == 0:
            self.dark_current = 0
        else:
            self.dark_current = (self.U * self.R) - 0.667

    def calculate_photo_current(self):
        denominator = self.distance + 19
        denominator2 = denominator * denominator
        self.photo_current = 5000 * self.U / denominator2

    def calculate_current(self):
        self.get_voltage()
        self.calculate_dark_current()
        self.update_distance()
        if self.photo_current_radio.isChecked():
            self.calculate_photo_current()
            self.total_current = self.dark_current + self.photo_current
        else:
            self.total_current = self.dark_current

        experiment_type = "Темновой ток" if self.dark_current_radio.isChecked() else "Фототок"

        self.result_label.setText(f'Результаты эксперимента:\n'
                                  f'Напряжение: {self.U:.2f} В\n'
                                  f'Освещенность: {self.illumination} лк\n'
                                  f'Ток: {self.total_current:.2e} А\n'
                                  f'Расстояние до экрана: {self.distance} см\n'
                                  f'Тип эксперимента: {experiment_type}')

    def start_experiment(self):
        self.calculate_current()

    def update_experiment_type(self):
        if self.photo_current_radio.isChecked():
            self.dark_current_radio.setText('Темновой ток')
            self.photo_current_radio.setText('Фототок')
        elif self.dark_current_radio.isChecked():
            self.photo_current_radio.setText('Фототок')
            self.dark_current_radio.setText('Темновой ток')


if __name__:
    app = QApplication(sys.argv)
    ex = PhotoEffectExperiment()
    ex.show()
    sys.exit(app.exec_())
