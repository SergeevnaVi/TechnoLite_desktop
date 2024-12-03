import sys
import os

# Добавляем путь к папке 'scr' в список путей поиска модулей
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scr.user_controller import User_controller
from scr.category_controller import Category_controller
from scr.navigation_controller import NavigationController
from scr.cart_controller import CartController

from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_MainWindow import Ui_Shop

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Shop()
        self.ui.setupUi(self)

        self.user_id = None

        # Создаём экземпляры контроллеров
        self.Category_controller = Category_controller(self.ui, self.user_id)
        self.Navigation = NavigationController(self.ui, self.Category_controller)  # Навигационный контроллер
        self.User_controller = User_controller(self.ui)

        # Устанавливаем начальный экран на страницу входа
        self.ui.stackedWidget.setCurrentIndex(0)

        # Настройка кнопок на странице входа (индекс 0)
        self.ui.btn_signin.clicked.connect(self.User_controller.handle_signin)
        self.ui.btn_signup_2.clicked.connect(self.Navigation.go_to_register_page)

        # Настройка кнопок на странице регистрации (индекс 1)
        self.ui.btn_signup.clicked.connect(self.User_controller.handle_signup)
        self.ui.btn_signin_2.clicked.connect(self.Navigation.go_to_login_page)

        # Настройка кнопок на странице магазина (индекс 2)
        self.ui.btn_cart.clicked.connect(self.Navigation.go_to_cart_page)
        self.ui.btn_pers_acc.clicked.connect(self.User_controller.handle_personal_account_button)

        # Кнопка "В магазин" на странице личного кабинета (индекс 5)
        self.ui.btn_pers_acc_shop.clicked.connect(self.Navigation.go_to_page_shop)

        # Переход в личный кабинет при нажатии кнопки
        self.ui.btn_pers_acc.clicked.connect(self.User_controller.handle_personal_account_button)

        # Настройка дерева категорий
        self.ui.treeWidget_category.itemClicked.connect(self.Category_controller.on_tree_item_selected)

        # Обновление интерфейса при смене страницы
        self.ui.stackedWidget.currentChanged.connect(self.Category_controller.on_page_changed)

        # Кнопки на странице товара (с индексом 6)
        self.ui.btn_shop.clicked.connect(self.Navigation.go_to_page_shop)
        self.Cart_controller = self.User_controller.cart_controller
        self.ui.btn_cart_2.clicked.connect(self.Cart_controller.on_add_to_cart_button_click)
        
        # Кнопки на странице коризны (с индексом 4)
        self.ui.btn_cart_go_shop.clicked.connect(self.Navigation.go_to_page_shop)
        self.ui.btn_clear_cart.clicked.connect(self.Cart_controller.clear_cart)

        # Настройка сигналов для изменения таблицы корзины
        self.ui.tableWidget_cart.itemChanged.connect(self.Cart_controller.on_quantity_changed)
        self.ui.tableWidget_cart.cellChanged.connect(self.Cart_controller.on_cart_cell_changed)

        # Кнопка для выгрузки данных из корзины в файл
        self.ui.btn_export_cart.clicked.connect(self.Cart_controller.update_cart_file)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())