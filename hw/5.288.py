# Работай пожалуйста -> СТРАШНО (ЯДЕРКА)
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


def calculate_neutron_energy(K_alpha, Q) -> float:
    # Энергия нейтрона по законам сохранения энергии и импульса
    # K_alpha + Q = K_neutron + K_Carbon
    # Поскольку нейтрон и углерод движутся в разные стороны, можно упростить расчет
    # используя ЗСЭ и относительные массы
    m_alpha = 4
    m_be = 9
    m_c = 12
    m_n = 1
    E_neutron = (K_alpha + Q) / (1 + m_c / m_n)

    return E_neutron


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def on_calculate(self):
        try:
            K_alpha = float(self.energy_input.text())
            Q = float(self.q_value_input.text())
            E_neutron = calculate_neutron_energy(K_alpha, Q)
            self.result_label.setText(
                f'Результат: Кинетическая энергия нейтрона: {E_neutron:.4f} МэВ')
            self.formula_label.setText(
                f'Используемые формулы:\n'
                f'E_neutron = (K_alpha + Q) / (1 + m_Carbon / m_neutron)')
        except ValueError:
            self.result_label.setText('ОШИБКА, введите корректные числовые значения.')

    def initUI(self):
        self.setWindowTitle('5.288 Расчет кинетической энергии нейтрона')
        self.layout = QVBoxLayout()

        self.info_label = QLabel(
            'Условие задачи: Альфа-частица с кинетической энергией K = 5.3 МэВ возбуждает \n'
            'реакцию 9Be(α,n)12C, энергия которой Q = +5.7 МэВ. Найти кинетическую \n'
            'энергию нейтрона, вылетевшего под прямым углом к направлению движения α-частицы.')
        self.layout.addWidget(self.info_label)

        self.energy_label = QLabel('Кинетическая энергия альфа-частицы K (МэВ):')
        self.energy_input = QLineEdit()
        self.energy_input.setText('5.3')
        self.q_value_label = QLabel('Энергия реакции Q (МэВ):')
        self.q_value_input = QLineEdit()
        self.q_value_input.setText('5.7')

        self.calculate_button = QPushButton('Рассчитать')
        self.result_label = QLabel(
            'Результат: Кинетическая энергия нейтрона будет отображена здесь')
        self.formula_label = QLabel('Используемые формулы будут отображены здесь')

        self.layout.addWidget(self.energy_label)
        self.layout.addWidget(self.energy_input)
        self.layout.addWidget(self.q_value_label)
        self.layout.addWidget(self.q_value_input)
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
