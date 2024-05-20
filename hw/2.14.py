# ♦️Работай пожалуйста ♦️-> ЭЛ-ВО
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, \
    QRadioButton, QButtonGroup

k = 8.99e9  # Константа Кулона, Н·м²/Кл²


def calculate_electric_field(sigma, R, shape) -> float:
    Q = 0
    if shape == 'half':
        Q = sigma * 2 * 3.14159 * (R ** 2)
        formula = "Q = σ * 2π * R^2"
    elif shape == 'full':
        Q = sigma * 4 * 3.14159 * (R ** 2)
        formula = "Q = σ * 4π * R^2"
    elif shape == 'third':
        Q = sigma * ((4 * 3.14159 * (R ** 2)) / 3)
        formula = "Q = σ * (4π * R^2 / 3)"
    E = ((k * Q) / (R * R))
    E_formula = "E = k * Q / R^2"
    return E, formula, E_formula


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def on_calculate(self):
        try:
            sigma = float(self.sigma_input.text())
            R = float(self.radius_input.text())
            shape = self.button_group.checkedButton().objectName()
            E, Q_formula, E_formula = calculate_electric_field(sigma, R, shape)
            self.result_label.setText(f'Результат: {E:.2f} Н/Кл')
            self.formula_label.setText(f'Используемые формулы:\n{Q_formula}\n{E_formula}')
        except ValueError:
            self.result_label.setText('ОЩИБКА, введите корректные чиловые значения.')

    def initUI(self):
        self.setWindowTitle('2.14 Расчет электрического поля сфер')
        self.setGeometry(100, 100, 800, 600)
        self.layout = QVBoxLayout()

        self.info_label = QLabel(
            'Условие задачи: Найти напряженность электрического поля в центре основания полусферы, заряженной равномерно с поверхностной плотностью σ = 60 нКл/м².')
        self.layout.addWidget(self.info_label)

        self.sigma_label = QLabel('Поверхностная плотность заряда (Кл/м²):')
        self.sigma_input = QLineEdit()
        self.radius_label = QLabel('Радиус сферы (м):')
        self.radius_input = QLineEdit()

        self.half_sphere = QRadioButton('Полусфера')
        self.half_sphere.setObjectName('half')
        self.full_sphere = QRadioButton('Полная сфера')
        self.full_sphere.setObjectName('full')
        self.third_sphere = QRadioButton('Треть сферы')
        self.third_sphere.setObjectName('third')
        self.half_sphere.setChecked(True)

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.half_sphere)
        self.button_group.addButton(self.full_sphere)
        self.button_group.addButton(self.third_sphere)

        self.calculate_button = QPushButton('Рассчитать')
        self.result_label = QLabel('Результат: Напряженность поля будет отображена здесь')
        self.formula_label = QLabel('Используемые формулы будут отображены здесь')

        self.layout.addWidget(self.sigma_label)
        self.layout.addWidget(self.sigma_input)
        self.layout.addWidget(self.radius_label)
        self.layout.addWidget(self.radius_input)
        self.layout.addWidget(self.half_sphere)
        self.layout.addWidget(self.full_sphere)
        self.layout.addWidget(self.third_sphere)
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
