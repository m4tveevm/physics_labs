# Работай пожалуйста -> ЭЛЕКТРОДИНАМИКА
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


def calculate_induced_charges(q, x, l) -> (float, float):
    q1 = -q * (l - x) / l
    q2 = -q * x / l
    return q1, q2


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def on_calculate(self):
        try:
            q = float(self.charge_input.text())
            x = float(self.distance_input.text())
            l = float(self.spacing_input.text())
            q1, q2 = calculate_induced_charges(q, x, l)
            self.result_label.setText(f'Результат:\nНаведенный заряд на пластине 1: {q1:.4e} Кл\n'
                                      f'Наведенный заряд на пластине 2: {q2:.4e} Кл')
            self.formula_label.setText(
                f'Используемые формулы:\nq1 = -q * (l - x) / l\nq2 = -q * x / l')
        except ValueError:
            self.result_label.setText('Пожалуйста, введите корректные числовые значения.')

    def initUI(self):
        self.setWindowTitle('3.67 Расчет наведенных зарядов на пластинах')
        self.layout = QVBoxLayout()

        self.info_label = QLabel(
            'Условие задачи: Две безграничные проводящие пластины 1 и 2 расположены на\n'
            'расстоянии l друг от друга. Между пластинами на расстоянии x от пластины 1 находится\n'
            'точечный заряд q. Найти заряды, наведенные на каждой из пластин.')
        self.layout.addWidget(self.info_label)

        self.charge_label = QLabel('Точечный заряд q (Кл):')
        self.charge_input = QLineEdit()
        self.distance_label = QLabel('Расстояние x от пластины 1 (м):')
        self.distance_input = QLineEdit()
        self.spacing_label = QLabel('Расстояние l между пластинами (м):')
        self.spacing_input = QLineEdit()

        self.calculate_button = QPushButton('Рассчитать')
        self.result_label = QLabel('Результат: Наведенные заряды будут отображены здесь')
        self.formula_label = QLabel('Используемые формулы будут отображены здесь')

        self.layout.addWidget(self.charge_label)
        self.layout.addWidget(self.charge_input)
        self.layout.addWidget(self.distance_label)
        self.layout.addWidget(self.distance_input)
        self.layout.addWidget(self.spacing_label)
        self.layout.addWidget(self.spacing_input)
        self.layout.addWidget(self.calculate_button)
        self.layout.addWidget(self.result_label)
        self.layout.addWidget(self.formula_label)

        self.setLayout(self.layout)

        self.calculate_button.clicked.connect(self.on_calculate)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
