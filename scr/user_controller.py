import re
from db.models import check_user, create_user, get_user_data, get_cart_items
from scr.category_controller import Category_controller
from scr.navigation_controller import NavigationController
from scr.cart_controller import CartController
from PyQt5.QtWidgets import QMessageBox

class User_controller:
    def __init__(self, ui):
        self.ui = ui  # Привязка UI к контроллеру
        self.current_user_id = None  # ID текущего пользователя
        self.category_controller = Category_controller(self.ui)  # Создание экземпляра Category_controller
        self.navigation = NavigationController(self.ui, self.category_controller)  # Создание экземпляра NavigationController
        self.cart_controller = CartController(self.ui)  # Добавляем CartController в User_controller
        self.cart_controller.set_user_controller(self)  # Связываем корзину с текущим пользователем

    def set_user(self, user_id):
        """Устанавливает идентификатор пользователя для всех контроллеров."""
        self.current_user_id = user_id  # Сохраняем user_id в главном классе
        self.cart_controller.user_id = user_id
        self.category_controller.user_id = user_id
    
        self.load_cart_for_user(user_id)  # Загружаем корзину для пользователя

    def handle_signin(self):
        """Обработчик кнопки входа"""
        phone = self.ui.lineEdit_phone.text()
        password = self.ui.lineEdit_psw.text()

        # Валидация телефона
        if not phone or not phone.isdigit() or len(phone) != 11:
            self.show_error("Неверный номер телефона!")
            return

        # Валидация пароля
        if not password or len(password) < 8:
            self.show_error("Пароль должен быть не менее 8 символов!")
            return

        # Проверка в базе данных
        user_id = check_user(phone, password)
        if user_id:
            self.set_user(user_id)  # Устанавливаем пользователя
            self.navigation.go_to_page_shop()  # Переключаемся на страницу магазина
        else:
            self.show_error("Такого пользователя не существует или неверный пароль!")

    def load_cart_for_user(self, user_id):
        """Загрузка сохраненной корзины пользователя."""
        try:
            if not user_id:
                self.show_error("Пользователь не авторизован!")
                return

            # Загрузка корзины из базы данных
            cart_items = get_cart_items(user_id)
            print(f"Загруженные товары: {cart_items}")
            self.cart_controller.load_cart(cart_items)  # Загружаем товары в корзину
        except Exception as e:
            self.show_error(f"Ошибка при загрузке корзины: {e}")


    def handle_signup(self):
        """Обработчик кнопки регистрации"""
        first_name = self.ui.lineEdit_name.text()
        password = self.ui.lineEdit_psw_2.text()
        email = self.ui.lineEdit_email.text()
        phone = self.ui.lineEdit_phone_2.text()

        # Валидация данных
        if not first_name or not phone or not email or not password:
            self.show_error("Пожалуйста, заполните все поля!")
            return

        if len(phone) != 11 or not phone.isdigit():
            self.show_error("Неверный формат номера телефона!")
            return

        if len(password) < 6:
            self.show_error("Пароль должен быть не менее 6 символов!")
            return

        # Валидация email
        email_regex = r'^[a-zA-Z0-9._%+-]+@(gmail\.com|mail\.ru)$'
        if not re.match(email_regex, email):
            self.show_error("Неверный формат email! Используйте gmail.com или mail.ru.")
            return

        # Создание нового пользователя
        success, message = create_user(first_name, password, email, phone)
        if success:
            self.show_success("Регистрация прошла успешно!")
        
            # Получаем user_id после регистрации
            self.current_user_id = check_user(phone, password)  # Проверяем пользователя по телефону и паролю
            if self.current_user_id:
                self.set_user(self.current_user_id)  # Устанавливаем user_id в главный файл
                self.show_success("Добро пожаловать!")
            else:
                self.show_error("Ошибка при получении ID пользователя!")
        else:
            self.show_error(message)

    def handle_personal_account_button(self):
        """Обработчик кнопки 'Личный кабинет'"""
        if self.current_user_id:
            self.update_personal_account()  # Обновляем данные личного кабинета
            self.navigation.go_to_personal_account()  # Переход на страницу личного кабинета
        else:
            self.show_error("Вы не авторизованы!")

    def update_personal_account(self):
        """Обновление информации в личном кабинете"""
        if self.current_user_id:
            user_data = get_user_data(self.current_user_id)
            if user_data:
                self.ui.lineEdit_name_2.setText(user_data.get("first_name", ""))
                self.ui.lineEdit_email_2.setText(user_data.get("email", ""))
                self.ui.lineEdit_phone_3.setText(user_data.get("phone", ""))

    def show_error(self, message):
        """Отображение окна с ошибкой"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Ошибка")
        msg.exec_()

    def show_success(self, message):
        """Отображение окна с успешным сообщением"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Успех")
        msg.exec_()
