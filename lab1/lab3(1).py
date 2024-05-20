import sys
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from lab_experiment_ui import Ui_Form


class LabFirst(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ra = 5
        self.rb = 3

        self.get_measurement_button.clicked.connect(self.on_get_measurement)
        self.random_coords_button.clicked.connect(self.get_random_coords)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.verticalLayout.addWidget(self.canvas)

        self.plot_model()

    def plot_model(self):
        ax = self.figure.add_subplot(111)
        ax.clear()

        electrode1 = Ellipse((0, -10), width=self.ra * 2, height=self.rb * 2, edgecolor='red',
                             facecolor='none', label='Электрод 1')
        electrode2 = Ellipse((0, 10), width=self.ra * 2, height=self.rb * 2, edgecolor='blue',
                             facecolor='none', label='Электрод 2')
        ax.add_patch(electrode1)
        ax.add_patch(electrode2)

        ax.set_xlim(-20, 20)
        ax.set_ylim(-20, 20)
        ax.set_xlabel('X (мм)')
        ax.set_ylabel('Y (мм)')
        ax.set_title('Модель электростатического поля')
        ax.legend()

        self.canvas.draw()

    def on_get_measurement(self):
        try:
            x_mm = float(self.x_input.text())
            y_mm = float(self.y_input.text())
            x_cm = x_mm / 10
            y_cm = y_mm / 10

            potential = self.get_potencial(x_cm, y_cm)
            self.result_label.setText(f'Потенциал в точке ({x_mm}, {y_mm}) мм: {potential:.2f} В')

            self.plot_model()
            ax = self.figure.gca()
            ax.plot(x_mm, y_mm, 'o', color='orange', label='Измеренная точка')
            ax.legend()
            self.canvas.draw()
        except ValueError:
            self.result_label.setText('Пожалуйста, введите корректные числовые значения.')

    def get_random_coords(self):
        x_mm = random.uniform(-15, 15)
        y_mm = random.uniform(-15, 15)

        self.x_input.setText(f'{x_mm:.2f}')
        self.y_input.setText(f'{y_mm:.2f}')

        self.on_get_measurement()

    def get_potencial(self, x_cm, y_cm):
        V1 = 40
        V2 = -40
        d_cm = 2
        potential = V1 * (1 - abs(y_cm) / d_cm) + V2 * (abs(y_cm) / d_cm)
        return potential


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LabFirst()
    ex.show()
    sys.exit(app.exec_())
