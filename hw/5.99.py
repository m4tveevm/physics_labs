# Работай пожалуйста -> ОПТИКА
import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

h = 6.62607015e-34  # постоянная Планка, Дж·с
m_e = 9.10938356e-31  # масса электрона, кг
eV_to_J = 1.60218e-19  # перевод из эВ в Джоули



def get_interplanar_distance(K, theta, n) -> float:
    K_J = K * eV_to_J
    lambda_ = h / math.sqrt(2 * m_e * K_J)
    d = (n * lambda_) / (2 * math.sin(math.radians(theta)))
    return d


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def on_calculate(self):
        try:
            K = float(self.energy_input.text())
            theta = float(self.angle_input.text())
            n = 4
            d = get_interplanar_distance(K, theta, n)
            self.result_label.setText(f'Результат: {d:.4e} м')
            self.formula_label.setText(
                f'Используемые формулы:\nλ = h / sqrt(2m_eK)\nd = (nλ) / (2sinθ)')
        except ValueError:
            self.result_label.setText('ОШИБКА, введите корректные чиловые значения.')

    def initUI(self):
        self.setWindowTitle('5.99 Расчет межплоскостного расстояния')
        self.layout = QVBoxLayout()

        self.info_label = QLabel(
            'Условие задачи: Узкий пучок моноэнергетических электронов падает \n'
            'нормально на поверхность монокристалла никеля. В направлении, составляющем \n'
            'угол θ = 55° с нормалью к поверхности, наблюдается максимум отражения четвертого\n'
            'порядка при энергии электронов K = 180 эВ. Вычислить соответствующее \n'
            'межплоскостное расстояние.')
        self.layout.addWidget(self.info_label)

        self.energy_label = QLabel('Энергия электронов (эВ):')
        self.energy_input = QLineEdit()
        self.energy_input.setText('180')
        self.angle_label = QLabel('Угол отражения θ (градусы):')
        self.angle_input = QLineEdit()
        self.angle_input.setText('55')

        self.calculate_button = QPushButton('Рассчитать')
        self.result_label = QLabel('Результат: Межплоскостное расстояние будет отображено здесь')
        self.formula_label = QLabel('Используемые формулы будут отображены здесь')

        self.layout.addWidget(self.energy_label)
        self.layout.addWidget(self.energy_input)
        self.layout.addWidget(self.angle_label)
        self.layout.addWidget(self.angle_input)
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
