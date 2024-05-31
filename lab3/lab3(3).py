import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from lab_fraunhofer_ui import Ui_Form

class LabExperiment(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # consts
        self.wavelength = 650e-6  # Длина волны в мм
        self.distance_to_screen = 2000  # Расстояние до экрана в мм

        self.start_button.clicked.connect(self.on_start_experiment)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.graph_layout.addWidget(self.canvas)
        self.constants_label.setText(f'Постоянные значения установки:\n'
                                     f'Длина волны λ = {self.wavelength * 1e3:.0f} нм\n'
                                     f'Расстояние до экрана L = {self.distance_to_screen / 10:.0f} см')

    def plot_model(self):
        self.ax.clear()

        experiment_type = self.experiment_type_combo.currentText()
        angle = float(self.angle_input.text()) if self.angle_input.text() else 0

        if experiment_type == "Одиночная щель":
            self.plot_single_slit(angle)
        elif experiment_type == "Одномерная решетка":
            self.plot_1d_grating(angle)
        elif experiment_type == "Двумерная решетка":
            self.plot_2d_grating(angle)

        self.ax.set_xlabel('X (мм)')
        self.ax.set_ylabel('Интенсивность')
        self.ax.set_title(f'Дифракционная картина ({experiment_type})')
        self.ax.legend()
        self.canvas.draw()

    def plot_single_slit(self, angle):
        x = np.linspace(-1000, 1000, 400)
        b = 0.1  # Ширина щели в мм
        beta = (np.pi * b / self.wavelength) * np.sin(np.radians(angle))
        beta_x = beta * x
        intensity = np.where(beta_x != 0, (np.sin(beta_x) / beta_x) ** 2, 1)
        self.ax.plot(x, intensity, label=f'Одиночная щель, угол={angle}°')

    def plot_1d_grating(self, angle):
        x = np.linspace(-1000, 1000, 400)
        d = 1  # Период решетки в мм
        beta = (np.pi * d / self.wavelength) * (np.sin(np.radians(angle)) + np.sin(np.radians(angle)))
        beta_x = beta * x
        intensity = np.where(beta_x != 0, (np.sin(beta_x) / beta_x) ** 2, 1)
        self.ax.plot(x, intensity, label=f'Одномерная решетка, угол={angle}°')

    def plot_2d_grating(self, angle):
        x = np.linspace(-1000, 1000, 400)
        y = np.linspace(-1000, 1000, 400)
        X, Y = np.meshgrid(x, y)
        d1 = 1  # Период решетки в мм в направлении x
        d2 = 1  # Период решетки в мм в направлении y
        beta1 = (np.pi * d1 / self.wavelength) * np.sin(np.radians(angle))
        beta2 = (np.pi * d2 / self.wavelength) * np.sin(np.radians(angle))
        beta1_X = beta1 * X
        beta2_Y = beta2 * Y
        intensity1 = np.where(beta1_X != 0, (np.sin(beta1_X) / beta1_X) ** 2, 1)
        intensity2 = np.where(beta2_Y != 0, (np.sin(beta2_Y) / beta2_Y) ** 2, 1)
        intensity = intensity1 * intensity2

        self.ax.contourf(X, Y, intensity, levels=50, cmap='viridis')
        self.ax.set_aspect('equal')
        self.ax.set_title(f'Двумерная решетка, угол={angle}°')

    def on_start_experiment(self):
        self.plot_model()
        self.update_results()

    def update_results(self):
        experiment_type = self.experiment_type_combo.currentText()
        angle = float(self.angle_input.text()) if self.angle_input.text() else 0
        results = f'Тип эксперимента: {experiment_type}\nУгол: {angle}°\n'
        self.result_label.setText(f'Результаты эксперимента:\n{results}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LabExperiment()
    ex.show()
    sys.exit(app.exec_())