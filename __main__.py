import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QPalette, QColor, QKeyEvent


class TankEncyclopediaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tank_database = self.create_tank_database()
        self.current_image_path = None
        self.current_tank_name = None
        self.init_ui()

    def create_tank_database(self):
        # База данных танков СССР 1924-1941
        return {
            "т-35": {
                "name": "Т-35",
                "year": "1933",
                "description": "Советский тяжёлый многобашенный танк межвоенного периода. Единственный в мире серийный пятибашенный танк. Символ мощи и страха противника РККА 1930-х годов.",
                "image": "T-35.jpg",
                "characteristics": "• Экипаж: 11 человек\n• Вооружение: 76-мм пушка, 2×45-мм пушки, 5-7 пулемётов\n• Броня: 10-30 мм\n• Скорость: 30 км/ч\n• Масса: 50 тонн"
            },
            "т-46": {
                "name": "Т-46",
                "year": "1936",
                "description": " Советский опытный лёгкий колёсно-гусеничный танк 1930-х годов. Создавался как танк поддержки пехоты, при этом широко использовались узлы и агрегаты лёгкого танка Т-26.",
                "image": "T-46.jpg",
                "characteristics": "• Экипаж: 3 человек\n• 45-мм пушка 20К\n• Броня: 15-22мм\n• V-образный 8-цилиндровый карбюраторный жидкостного охлаждения, мощность — 330 л. с.\n• Скорость: 58 км/ч(на гусеницах) и 80км/ч(на колесах)"
            },
            "т-100": {
                "name": "Т-100",
                "year": "1939",
                "description": "Опытный советский двухбашенный тяжёлый танк конца 1930-х годов, но провалился кв-1. ",
                "image": "T-100.jpg",
                "characteristics": "• Экипаж: 8 человек\n•В главной задней башне — 76,2-мм пушка Л-11 обр. 1938/39 гг., в малой передней башне — 45-мм танковая пушка обр. 1934 г.\n• Броня: 20-60 мм и масса 58т \n• 850 л.с\n• Скорость: 37 км/ч"
            },
            "A-20": {
                "name": "А-20",
                "year": "1940",
                "description": "Создавался в 1939 году, к 1940 году был выпущен один опытный образец, в будущем использовался для создания т-34 ",
                "image": "A-20.jpg",
                "characteristics": "• Экипаж: 3-4 человек\n• Вооружение: 45-мм танковая пушка 20-К образца 1938 года.\n• Броня: +-25 мм\n• Двигатель: В-2 мощностью 500 л.с. (368 кВт).\n• Скорость: 70 км/ч"
            },
            "бт-7": {
                "name": "БТ-7",
                "year": "1935",
                "description": "Легкий танк, имеющий возможность ездить как на гусеницах, так и на колесах.",
                "image": "BT-7.jpg",
                "characteristics": "• Экипаж: 3 человека\n• Вооружение: 45-мм пушка\n• Броня: 6-22 мм\n• Двигатель: авиационный М-17Т, 400 л.с.\n• Скорость: до 72 км/ч на колёсах"
            },
            "т-24": {
                "name": "Т-24",
                "year": "1943",
                "description": "Советский средний танк, созданный в 1929–1930 годах как улучшенная версия опытного танка Т-12.",
                "image": "T-24.jpg",
                "characteristics": "• Экипаж: 5 человек\n• Вооружение: 45-мм пушка 20К и два 7,62-мм пулемёта ДТ в малой башне\n• Броня: +-25 мм\n• Двигатель: бензиновый М-6 мощностью 250 л. с. при 2200 об/мин.\n• Скорость: 30 км/ч"
            },
            "T-28": {
                "name": "T-28",
                "year": "1930-1932",
                "description": "Трёхбашенный советский средний танк межвоенного периода, первый в СССР средний танк, запущенный в массовое производство. ",
                "image": "T-28.jpg",
                "characteristics": "• Экипаж: 6 человек\n• Вооружение: 76,2-мм пушка КТ-28 и 4–5 пулемётов ДТ\n• Броня: +-25 мм\n• Двигатель: мощность — 450 л.с\n• Скорость: 42 км/ч"
            },
            "Kv-1": {
                "name": "Кв-1",
                "year": "1939",
                "description": "КВ-1 (названный в честь Климента Ворошилова, как и остальные танки серии КВ) — советский легендарный тяжёлый танк времён Великой Отечественной Войны.",
                "image": "Kv-1.jpg",
                "characteristics": "• Экипаж: 5 человек\n• Вооружение: калибр пушки — 76 мм\n• Броня: 30-75 мм\n• Двигатель: 11,6 л. с./т\n• Скорость: 34 км/ч"
            },
            "T-27": {
                "name": "T-27",
                "year": "1931-1933",
                "description": "КВ-1 (названный в честь Климента Ворошилова, как и остальные танки серии КВ) — советский легендарный тяжёлый танк времён Великой Отечественной Войны.",
                "image": "T-27.jpg",
                "characteristics": "• Экипаж: 2 человека\n• Вооружение: 7,62-мм пулемёт ДТ\n• Броня: 4-10 мм\n• Двигатель:  карбюраторный «ГАЗ-АА», мощность 40 л.с.\n• Скорость: 42 км/ч"
            },
            "T-26": {
                "name": "T-26",
                "year": "1931",
                "description": "Советский лёгкий танк, созданный на основе британского танка Vickers Mk E («Виккерс 6-тонный»).",
                "image": "T-26.jpg",
                "characteristics": "• Экипаж: 3 человека\n• Вооружение: 45-мм пушка 20К и 7,62-мм пулемёт ДТ\n• Броня: 4-9 мм\n• Двигатель: 4-цилиндровый бензиновый ГАЗ-Т-26 мощностью 90 л. с. при 2100 об/мин.\n• Скорость: 32 км/ч"
            },
            "T-37A": {
                "name": "T-37A",
                "year": "1933-1936",
                "description": " советский малый плавающий танк (в документах иногда также именуется танкеткой). В литературе танк часто обозначается как Т-37, однако формально это название носил другой танк, не вышедший за стадию прототипа. Т-37А — первый серийный плавающий танк в мире.",
                "image": "T-37A.jpg",
                "characteristics": "• Экипаж: 2 человека\n• Вооружение: 1 пулемёт ДТ образца 1929 года калибра 7,62 мм.\n• Броня: 4-9 мм\n• Двигатель: 40 л. с. при 2200 об/мин\n• Скорость: 35 км/ч"
            }
        }

    def init_ui(self):
        # Пользовательский интерфейс
        self.setWindowTitle("Энциклопедия танков СССР с 1924-1940 года")
        self.resize(1000, 1000) # размера окна
        self.setMinimumSize(1500, 1500)
        centr_widget = QWidget()

        self.setCentralWidget(centr_widget)
        centr_widget.setStyleSheet("background: #1a1a1a;")
        layout = QVBoxLayout(centr_widget)
        layout.setContentsMargins(0, 0, 0, 0) # отступы
        layout.setSpacing(0)

        title_label = QLabel("Энциклопедия танков СССР с 1924-1940")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Установка CSS - стилей для заголовка
        title_label.setStyleSheet(""" 
            QLabel {
                background: #2b2b2b; 
                color: white; 
                font-size: 28px; 
                font-weight: bold; 
                padding: 25px; 
                border-bottom: 3px solid #4CAF50; 
            }
        """)
        layout.addWidget(title_label)

        content_widget = QWidget()
        content_widget.setStyleSheet("background: #2c3e50;") # черный фон
        content_layout = QHBoxLayout(content_widget) # горизонт layot
        content_layout.setContentsMargins(15, 15, 15, 15) # отступы
        content_layout.setSpacing(20) # расстояние между элементами

        # Настройка левой и правой панели
        self.setup_tank_list(content_layout)
        self.setup_tank_info(content_layout)

        layout.addWidget(content_widget, 1)

        self.select_first_tank()

    def setup_tank_list(self, parent_layout):
        # Настройка списка танков
        list_widget = QWidget()
        list_widget.setStyleSheet("background: #34495e; border-radius: 10px;") # скругление углов и синий цвет левой панели
        list_layout = QVBoxLayout(list_widget)
        list_layout.setContentsMargins(10, 10, 10, 10) # отступы со всех сторон

        #  Заголовок списка танков
        list_label = QLabel("Список танков")
        list_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        list_label.setStyleSheet("""
            QLabel {
                color: white; 
                font-size: 18px; 
                font-weight: bold; 
                padding: 12px; 
                background: #2c3e50); 
                border-radius: 8px; 
                margin-bottom: 8px; 
            }
        """)
        list_layout.addWidget(list_label)

        # Виджет списка
        self.tank_list = QListWidget()
        self.tank_list.setStyleSheet("""
            QListWidget {
                background: #2c3e50; 
                border: 2px solid #34495e; 
                border-radius: 8px; 
                color: white; 
                font-size: 14px; 
                outline: none; 
            }
            QListWidget::item {
                padding: 10px; 
                border-bottom: 1px solid #34495e; 
                background: #34495e; 
                margin: 2px; 
                border-radius: 5px; 
            }
            QListWidget::item:selected {
                background: #4CAF50; 
                color: white; 
                font-weight: bold; 
            }
            QListWidget::item:hover {
                background: #3498db; 
            }
        """)

        for tank_key in self.tank_database:
            tank = self.tank_database[tank_key]
            item = QListWidgetItem(f"{tank['name']} ({tank['year']})")
            item.setData(Qt.ItemDataRole.UserRole, tank_key)
            self.tank_list.addItem(item)

        self.tank_list.itemClicked.connect(self.on_tank_selected)
        list_layout.addWidget(self.tank_list)

        parent_layout.addWidget(list_widget, 1)

    def setup_tank_info(self, parent_layout):
        # Настройка панели информации о танке
        info_widget = QWidget()
        info_widget.setStyleSheet("background: #34495e; border-radius: 10px;")

        info_layout = QVBoxLayout(info_widget)
        info_layout.setContentsMargins(15, 15, 15, 15)
        info_layout.setSpacing(15)

        self.info_label = QLabel()
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 20px; 
                font-weight: bold;
                padding: 15px; 
                background: #2c3e50v ; 
                border-radius: 8px;
            }
        """)
        info_layout.addWidget(self.info_label)

        self.image_container = QWidget()
        self.image_container.setStyleSheet("""
            QWidget {
                background: #1a1a1a; 
                border: 2px solid #2c3e50; 
                border-radius: 8px; 
                min-height: 300px; 
            }
        """)
        image_layout = QVBoxLayout(self.image_container)
        image_layout.setContentsMargins(10, 10, 10, 10)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Установка стилей для текстовой информации
        self.image_label.setStyleSheet("""
            QLabel {
                color: #bdc3c7; 
                font-size: 14px; 
                font-weight: bold; 
            }
        """)
        self.image_label.setScaledContents(True)
        self.image_label.setText("Изображение танка\n(поместите файлы в папку с программой)")
        image_layout.addWidget(self.image_label)
        info_layout.addWidget(self.image_container)

        # Конт для текстовой информации
        info_container = QWidget()
        info_container.setStyleSheet("""
            QWidget {
                background: #2c3e50; 
                border: 2px solid #34495e; 
                border-radius: 8px; 
            }
        """)
        info_container_layout = QVBoxLayout(info_container)
        info_container_layout.setContentsMargins(15, 15, 15, 15)

        self.info_text = QLabel()
        # Установка стилей для текстовой информации
        self.info_text.setStyleSheet("""
            QLabel {
                color: white; 
                font-size: 14px; 
                line-height: 1.6; 
            }
        """)
        self.info_text.setText("Выберите танк из списка для просмотра подробной информации")
        self.info_text.setWordWrap(True)
        self.info_text.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        info_container_layout.addWidget(self.info_text)
        info_layout.addWidget(info_container, 1)

        parent_layout.addWidget(info_widget, 2)

    def select_first_tank(self):
        # Выбрать первый танк в списке при запуске

        if self.tank_list.count() > 0:
            self.tank_list.setCurrentRow(0)
            first_item = self.tank_list.item(0)
            self.on_tank_selected(first_item)

    def on_tank_selected(self, item):
        # Обработка выбора танка из списка
        tank_key = item.data(Qt.ItemDataRole.UserRole)
        self.show_tank_info(tank_key)

    def show_tank_info(self, tank_key):
        # Показать информацию о выбранном танке
        if tank_key not in self.tank_database:
            return

        tank = self.tank_database[tank_key] # Получение данных о танке

        self.info_label.setText(f"{tank['name']} ({tank['year']} г.)")
        # HTML
        info_html = f"""
        <div style='font-size: 16px; margin-bottom: 12px; color: #4CAF50;'><b>{tank['name']}</b></div>
        <div style='margin-bottom: 12px; font-size: 14px;'>{tank['description']}</div>
        <div style='background: rgba(52, 73, 94, 0.8); padding: 12px; border-radius: 6px; font-size: 13px;'>
            <b style='color: #3498db;'>ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ:</b><br>
            {tank['characteristics'].replace(chr(10), '<br>')}
        </div>
        """
        self.info_text.setText(info_html)

        self.current_image_path = tank["image"]
        self.current_tank_name = tank["name"]
        self.load_tank_image(self.current_image_path, self.current_tank_name)

    def load_tank_image(self, image_name, tank_name):
        # Загрузка изображения танка
        if os.path.exists(image_name):
            try:
                pixmap = QPixmap(image_name)
                if pixmap.isNull():
                    self.image_label.setText(f"Ошибка загрузки:\n{image_name}")
                    return

                self.image_label.setPixmap(pixmap)
                self.image_label.setText("")

            except Exception as e:
                self.image_label.setText(f"Ошибка загрузки:\n{image_name}")
                print(f"Ошибка загрузки изображения {image_name}: {e}")
        else:
            self.image_label.setText(f"{tank_name}\n(файл: {image_name} не найден)")\

    def resizeEvent(self, event):
        super().resizeEvent(event)

    def closeEvent(self, event):
            dialog = QMessageBox(self)
            dialog.setWindowTitle("Подтверждение выхода")
            dialog.setText("Вы действительно хотите выйти из энциклопедии?")

            dialog.setStyleSheet("""
                QMessageBox {
                    backround: #2c3e50;
                    color: white;
                }
                QMessageBox QLabel {
                    color: white;
                    font-size: 14px;
                }
                QMessageBox QPushButton {
                    background: #34495e; 
                    border: 1px solid #4CAF50; 
                    border-radius: 5px; 
                    padding: 8px 15px;
                    font-weight: bold;
                    min-width: 100px;
                }
                QMessageBox QPushButton:hover {
                    background: #4CAF50;
                    color: white;
                }
                QMessageBox QPushButton:pressed {
                    background: #45a049
                }
            """)

            continue_button = dialog.addButton("Продолжить просмотр", QMessageBox.ButtonRole.NoRole)
            exit_button = dialog.addButton("Закрыть приложение", QMessageBox.ButtonRole.YesRole)

            continue_button.setText("Продолжить просмотр")
            exit_button.setText("Закрыть приложение")

            dialog.exec()

            if dialog.clickedButton() == exit_button:
                event.accept()
            else:
                event.ignore()


def main():
    # Главная функция приложения
    app = QApplication(sys.argv)
    app.setStyle('Fusion') # Установка стиля

    # Создание и настройка палитры для темной палитры
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
    app.setPalette(palette)

    # Главное окно
    window = TankEncyclopediaApp()
    window.show() # Показ главного окна

    sys.exit(app.exec()) # Запуск глав цикла

if __name__ == '__main__':
    main()

