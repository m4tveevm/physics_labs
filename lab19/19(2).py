import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit, \
    QPushButton
from lab_hall_effect_ui import Ui_Form


class HallEffectExperiment(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Consts
        self.B_n = 0.1  # начальная индукция магнитного поля сердечника электромагнита
        self.a = 0.5  # коэффициент пропорциональности
        self.k = 100  # коэффициент усиления операционного усилителя
        self.R = 1  # сопротивление R

        # Подключение элементов к функциям
        self.start_button.clicked.connect(self.start_experiment)

    def calculate_ux(self, u1):
        return u1 / self.k

    def calculate_magnetic_induction(self, i2):
        return self.B_n + self.a * i2

    def calculate_hall_constant(self, ux, i1, b):
        return ux * self.R / (i1 * b)

    def start_experiment(self):
        try:
            i1 = float(self.input_current_I1.text())
            i2 = float(self.input_current_I2.text())
        except ValueError:
            self.result_label.setText("Пожалуйста, введите корректные числовые значения для токов.")
            return

        u1 = 5  # пример значения напряжения на выходе ОУ
        ux = self.calculate_ux(u1)
        b = self.calculate_magnetic_induction(i2)
        hall_constant = self.calculate_hall_constant(ux, i1, b)

        self.result_label.setText(f'Результаты эксперимента:\n'
                                  f'Ток ДХ (I1): {i1:.2f} мА\n'
                                  f'Ток ЭМ (I2): {i2:.2f} мА\n'
                                  f'Напряжение U1: {u1:.2f} В\n'
                                  f'ЭДС Холла Ux: {ux:.2f} В\n'
                                  f'Индукция магнитного поля B: {b:.2f} Тл\n'
                                  f'Постоянная Холла R: {hall_constant:.2e} Ом/Тл')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HallEffectExperiment()
    ex.show()
    sys.exit(app.exec_())
