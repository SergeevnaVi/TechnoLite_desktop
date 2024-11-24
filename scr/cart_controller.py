from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QSpinBox
from db.models import get_product_id_by_name, get_product_by_id, get_cart_items, add_to_cart, update_cart_item_quantity, load_cart_for_user, clear_cart

class CartController:
    def __init__(self, ui):
        self.ui = ui
        self.user_controller = None  # Получаем доступ к User_controller
        self.user_id = None  # Идентификатор пользователя из User_controller
        self.cart_items = []

    def set_user_controller(self, user_controller):
        """Метод для установки user_controller после создания CartController"""
        self.user_controller = user_controller
        self.user_id = self.user_controller.current_user_id

    def show_cart_page(self):
        """Отображение страницы корзины с данными о товарах."""
        if not self.user_id:
            self.show_message("Пользователь не авторизован!")
            return

        cart_items = get_cart_items(self.user_id)  # Получаем данные корзины
        self.cart_items = cart_items  # Обновляем данные корзины
        self.update_cart_ui()  # Обновляем интерфейс

    def update_cart_ui(self):
        """Обновляет интерфейс корзины."""
        self.ui.tableWidget_cart.setRowCount(0)

        for row, item in enumerate(self.cart_items):
            self.ui.tableWidget_cart.insertRow(row)
            id_item = QTableWidgetItem(str(item["id_product"]))
            id_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  
            self.ui.tableWidget_cart.setItem(row, 0, id_item)

            name_item = QTableWidgetItem(item["model_name"])
            name_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.ui.tableWidget_cart.setItem(row, 1, name_item)

            price_item = QTableWidgetItem(f"{item['price']:.2f}")
            price_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.ui.tableWidget_cart.setItem(row, 2, price_item)

            # Создаём редактируемую ячейку для количества
            quantity_item = QTableWidgetItem(str(item["quantity"]))
            quantity_item.setFlags(quantity_item.flags() | Qt.ItemIsEditable)
            self.ui.tableWidget_cart.setItem(row, 3, quantity_item)

            # Итоговая стоимость
            total_price = item["quantity"] * item["price"]
            total_price_item = QTableWidgetItem(f"{total_price:.2f}")
            total_price_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.ui.tableWidget_cart.setItem(row, 4, total_price_item)

        # Подключаем обработчик для изменения количества
        self.ui.tableWidget_cart.itemChanged.disconnect(self.on_quantity_changed)
        self.ui.tableWidget_cart.itemChanged.connect(self.on_quantity_changed)

    def handle_quantity_change(self, row, quantity):
        """Обрабатывает изменение количества в корзине."""
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError("Количество должно быть положительным")

            # Обновляем количество в данных корзины
            self.cart_items[row]["quantity"] = quantity

            # Пересчитываем итоговую стоимость
            total_price = quantity * self.cart_items[row]["price"]

            # Обновляем значение итоговой стоимости
            total_price_item = QTableWidgetItem(f"{total_price:.2f}")
            total_price_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.ui.tableWidget_cart.setItem(row, 4, total_price_item)

        except ValueError:
            QMessageBox.warning(self.ui, "Ошибка", "Введите корректное количество.")

    def on_quantity_changed(self, item):
        """Обработчик изменения ячейки количества."""
        if not self.user_id:
            self.show_message("Пользователь не авторизован!")
            return

        row = item.row()
        column = item.column()

        if column == 3:
            try:
                quantity = int(item.text())
                if quantity < 1:
                    raise ValueError("Количество должно быть больше 0.")

                # Обновляем итоговую стоимость
                product_id = int(self.ui.tableWidget_cart.item(row, 0).text())
                product = get_product_by_id(product_id)

                if quantity > product["stock_quantity"]:
                    self.show_message(f"Недостаточно товара на складе! В наличии только {product['stock_quantity']} шт.")
                    # Восстановление предыдущего значения
                    item.setText(str(self.cart_items[row]["quantity"]))
                    return

                price = float(self.ui.tableWidget_cart.item(row, 2).text())
                total_price = quantity * price
                self.ui.tableWidget_cart.setItem(row, 4, QTableWidgetItem(f"{total_price:.2f}"))

                # Обновляем данные в базе
                success = update_cart_item_quantity(self.user_id, product_id, quantity)
                if not success:
                    self.show_message("Ошибка обновления данных в базе!")
            except ValueError:
                self.show_message("Введите корректное количество (целое число больше 0).")
                # Восстанавливаем старое значение
                previous_quantity = self.ui.tableWidget_cart.item(item.row(), 3).text()
                item.setText(previous_quantity)

    def on_cart_cell_changed(self, row, column):
        """Обрабатывает изменения в таблице корзины."""
        if column == 3:
            quantity = self.ui.tableWidget_cart.item(row, column).text()
            self.handle_quantity_change(row, quantity)

    def add_product_to_cart(self, product_id, quantity=1):
        """Добавление товара в корзину."""
        if not self.user_id:
            self.show_message("Пользователь не авторизован!")
            return

        product = get_product_by_id(product_id)
        if not product:
            self.show_message("Товар не найден!")
            return

        if product["stock_quantity"] < quantity:
            self.show_message(f"Недостаточно товара на складе! В наличии только {product['stock_quantity']} шт.")
        return

        success = add_to_cart(self.user_id, product_id, quantity)

        if success:
            self.show_message(f"Товар добавлен в корзину! Количество: {quantity}")
            self.ui.stackedWidget.setCurrentIndex(4)
            self.show_cart_page()  # Обновление корзины
        else:
            self.show_message("Ошибка добавления товара в корзину.")

    def load_product_data(self, product_id):
        """Загружает информацию о товаре на страницу."""
        product = get_product_by_id(product_id)
        if product:
            self.ui.label_name_product.setText(f"{product['model_name']} ({product['manufacturer_name']})")
            self.ui.label_price_product.setText(f"{product['price']:.2f} ₽")
            self.ui.label_stock_quantity.setText(f"В наличии: {product['stock_quantity']} шт")

            # Устанавливаем дефолтное значение в поле для количества
            self.ui.quantity_input.setText("1")
        else:
            self.show_message("Товар не найден!")


    def on_add_to_cart_button_click(self):
        """Добавление товара в корзину."""
        if not self.user_id:
            self.show_message("Пользователь не авторизован!")
            return

        # Получаем название товара
        product_name = self.ui.label_name_product.text()

        # Получаем ID товара из базы данных по его точному названию
        product_id = get_product_id_by_name(product_name)

        if not product_id:
            self.show_message("Товар не найден!")
            return

        # Количество товара, которое добавляется в корзину
        quantity = 1

        # Добавляем товар в корзину с полученным ID
        success = add_to_cart(self.user_id, product_id, quantity)

        if success:
            self.show_message(f"Товар '{product_name}' добавлен в корзину!")
        else:
            self.show_message("Ошибка добавления товара в корзину.")

        # Переключаемся на страницу корзины (индекс 4) и обновляем её
        self.ui.stackedWidget.setCurrentIndex(4)
        self.show_cart_page()

    def load_cart(self, cart_items):
        """Загружает корзину пользователя в интерфейс."""
        self.cart_items = cart_items
        self.update_cart_ui()

    def show_product_page(self, product_id):
        """Отображение страницы товара с заполнением данных."""
        self.load_product_data(product_id)
        self.ui.stackedWidget.setCurrentIndex(6)

    def show_message(self, message):
        """Отображение сообщения пользователю и отложенное переключение на корзину."""
        msg = QMessageBox(self.ui.stackedWidget)
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Информация")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    # Используем QTimer для отложенного выполнения переключения страницы
    def on_msg_closed():
        """Переключает интерфейс на страницу корзины после закрытия сообщения."""
        self.ui.stackedWidget.setCurrentIndex(4)
        msg.finished.connect(on_msg_closed)
        msg.exec_()

    def clear_cart(self):
        """Очищает корзину пользователя."""
        clear_cart(self.user_id)
        self.ui.tableWidget_cart.setRowCount(0)
        self.show_message("Корзина очищена!")