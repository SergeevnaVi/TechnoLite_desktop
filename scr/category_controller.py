from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QTreeWidgetItem, QLabel, QToolButton, QPushButton, QVBoxLayout, QMessageBox, QWidget, QGridLayout
from db.models import (get_categories, get_category_id_by_name, get_subcategories_by_category, get_products_by_subcategory, get_subcategory_id_by_name, 
get_product_characteristics, get_product_details)

class Category_controller():
    def __init__(self, ui, user_id=None):
        self.ui = ui  # Привязка UI к контроллеру
        self.user_id = user_id  # Сохранение user_id
        self.categories_data = {}  # Словарь для хранения категорий
        self.subcategories_data = {}  # Словарь для хранения подкатегорий
        self.item_to_buttons = {}  # Связь между элементами дерева и кнопками
        self.load_categories_and_subcategories()
        self.connect_tree_events()
        self.initialize_main_shop_page()

    ### Методы для работы с категориями и подкатегориями ###

    def load_categories_and_subcategories(self):
        """Загрузка категорий и подкатегорий в TreeWidget"""
        categories = get_categories()
        # Очищаем старые данные в TreeWidget перед добавлением новых
        self.ui.treeWidget_category.clear()
        self.item_to_buttons.clear()  # Очищаем предыдущую связь
        # Устанавливаем заголовки для TreeWidget
        self.ui.treeWidget_category.setHeaderLabels(["Каталог"])

        for category in categories:
            # Создаем основной элемент категории
            category_item = QTreeWidgetItem(self.ui.treeWidget_category)
            category_item.setText(0, category['name'])
            # Сохраняем категорию в словарь
            self.categories_data[category['id_category']] = category['name']

            # Получаем подкатегории и создаем уникальный словарь для них
            subcategories = get_subcategories_by_category(category['id_category'])
            unique_subcategories = {sub['id_subcategory']: sub for sub in subcategories}
            self.subcategories_data[category['id_category']] = unique_subcategories

            # Создаем дочерние элементы для подкатегорий (сначала скрытые)
            for sub_id, subcategory in unique_subcategories.items():
                subcategory_item = QTreeWidgetItem(category_item)
                subcategory_item.setText(0, subcategory['name'])
                subcategory_item.setHidden(True)  # Делаем скрытыми изначально

                # Используем subcategory_id как ключ в словаре item_to_buttons
                self.item_to_buttons[subcategory['id_subcategory']] = [
                    self.ui.btn_pr1,
                    self.ui.btn_pr2,
                    self.ui.btn_pr3,
                    self.ui.btn_pr4,
                ]

    def connect_tree_events(self):
        """Подключение обработчиков событий TreeWidget"""
        self.ui.treeWidget_category.itemClicked.connect(self.on_tree_item_selected)

    def on_tree_item_selected(self, item, column):
        """Обработчик нажатия на элемент дерева"""
        if item.childCount() > 0:  # Если это категория
            self.toggle_subcategories_visibility(item)
        else:  # Если это подкатегория
            self.on_subcategory_selected(item, column)

    def toggle_subcategories_visibility(self, category_item):
        """Скрывает/показывает подкатегории"""
        is_hidden = category_item.child(0).isHidden()
        for i in range(category_item.childCount()):
            category_item.child(i).setHidden(not is_hidden)

    ### Методы для работы с товарами ###

    def on_subcategory_selected(self, item, column):
        """Обработчик нажатия на подкатегорию."""
        subcategory_name = item.text(0)
        subcategory_id = get_subcategory_id_by_name(subcategory_name)

        if not subcategory_id:
            self.clear_product_buttons()
            return

        # Получаем товары из базы данных
        products = get_products_by_subcategory(subcategory_id)
        self.display_product_buttons(products)


    def display_product_buttons(self, products):
        """Обновляет кнопки с данными о товарах."""
        self.clear_product_buttons()

        if not products:
            return  # Если товаров нет, выходим

        buttons = self.item_to_buttons.get(products[0].get('id_subcategory'), [])  # Используем get для безопасного доступа

        for i, product in enumerate(products[:len(buttons)]):
            button = buttons[i]
            button.setVisible(True)  # Делаем кнопку видимой
            # Устанавливаем текст кнопки с моделью и ценой
            button.setText(f"{product['model_name']} - {product['price']} ₽")
            button.setToolTip(f"{product['manufacturer_name']}")
            button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # Устанавливаем текст под иконкой
            button.setEnabled(True)

            # Если изображение есть, устанавливаем иконку
            if product.get('image_url'):
                pixmap = QPixmap(product['image_url'])
                if not pixmap.isNull():  # Проверяем, что изображение корректное
                    icon = QIcon(pixmap)  # Преобразуем QPixmap в QIcon
                    button.setIcon(icon)  # Устанавливаем иконку
                    button.setIconSize(QtCore.QSize(150, 150))  # Размер иконки

            # Привязываем событие нажатия на кнопку
            button.clicked.connect(partial(self.show_product_details, product))

    def show_product_details(self, product):
        """Отображение деталей товара."""
        product_id = product['id_product']

        if not product_id:
            self.show_error("Не удалось определить товар.")
            return

        # Получаем основные данные о товаре
        details = get_product_details(product_id)
        if not details:
            self.show_error("Информация о товаре не найдена.")
            return

        # Переход на страницу деталей
        self.ui.stackedWidget.setCurrentIndex(6)

        # Заполнение данных
        self.ui.label_name_product.setText(f"{details['model_name']} ({details['manufacturer_name']})")
        self.ui.label_input_price.setText(f"{details['price']} ₽")
        self.ui.label_input_about.setText(details.get('description', 'Нет описания'))

        # Загрузка изображения
        if details.get('image_url'):
            pixmap = QPixmap(details['image_url'])
            self.ui.label_image.setPixmap(pixmap.scaled(341, 291))
        else:
            self.ui.label_image.setText("Изображение отсутствует")

        # Загрузка характеристик в таблицу
        characteristics = get_product_characteristics(product_id)
        self.fill_characteristics_table(characteristics)

    def fill_characteristics_table(self, characteristics):
        """Заполняет таблицу характеристик."""
        self.ui.tableWidget_characteristic.clearContents()
        self.ui.tableWidget_characteristic.setRowCount(len(characteristics))
        self.ui.tableWidget_characteristic.setColumnCount(2)  # Убедитесь, что 2 столбца

        self.ui.tableWidget_characteristic.setHorizontalHeaderLabels(["Характеристика", "Значение"])
        for row, (name, value) in enumerate(characteristics.items()):
            self.ui.tableWidget_characteristic.setItem(row, 0, QtWidgets.QTableWidgetItem(name))
            self.ui.tableWidget_characteristic.setItem(row, 1, QtWidgets.QTableWidgetItem(value))


    ### Вспомогательные методы ###

    def clear_product_buttons(self):
        """Очищает все кнопки и скрывает их."""
        for button in [self.ui.btn_pr1, self.ui.btn_pr2, self.ui.btn_pr3, self.ui.btn_pr4]:
            button.setText("")
            button.setIcon(QIcon())
            button.setEnabled(False)
            button.setVisible(False)

    def show_error(self, message):
        """Отображение окна с ошибкой"""
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle("Ошибка")
        error_dialog.setText(message)
        error_dialog.exec_()

    def initialize_main_shop_page(self):
        """Инициализация главной страницы магазина."""
        self.clear_product_buttons()  # Скрываем кнопки при загрузке страницы

    def on_page_changed(self, index):
        """Обработчик смены страницы в stackedWidget."""
        if index == 2:  # Индекс главной страницы магазина
            self.initialize_main_shop_page()


