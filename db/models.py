# Определение моделей БД (таблицы)

import bcrypt
import mysql.connector
from mysql.connector import IntegrityError, Error
from db.database import create_connection

# Функция для проверки пользователя
def check_user(phone, password):
    """Проверка наличия пользователя с таким номером телефона и паролем"""
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE phone = %s"
        cursor.execute(query, (phone,))
        user = cursor.fetchone()

        # Закрываем соединение с БД
        cursor.close()
        connection.close()

        if user:
            # Проверяем, соответствует ли пароль
            if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
                return user['id_user']
        return None
    return None

# Функция для создания нового пользователя
def create_user(first_name, password, email, phone):
    """Создание нового пользователя"""
    connection = create_connection()
    if connection:
        cursor = connection.cursor()

        # Хешируем пароль перед сохранением
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Запрос на добавление пользователя в базу данных
        query = "INSERT INTO users (first_name, password, email, phone) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(query, (first_name, hashed_password, email, phone))
            connection.commit()
            cursor.close()
            connection.close()
            return True, None  # Успешная регистрация
        except mysql.connector.errors.IntegrityError as e:
            # Проверяем, какая именно ошибка уникальности произошла
            if "Duplicate entry" in str(e):
                if "email" in str(e):
                    return False, "Этот email уже зарегистрирован."
                elif "phone" in str(e):
                    return False, "Этот номер телефона уже зарегистрирован."
            return False, "Произошла ошибка при регистрации пользователя."
        except Error as e:
            print(f"Ошибка при добавлении пользователя: {e}")
            return False, "Произошла ошибка при регистрации пользователя."
        finally:
            cursor.close()
            connection.close()
    return False, "Не удалось подключиться к базе данных."

def get_user_data(user_id):
    """Получить данные пользователя по его ID"""
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE id_user = %s"
        cursor.execute(query, (user_id,))
        user_data = cursor.fetchone()

        # Закрываем соединение с БД
        cursor.close()
        connection.close()

        if user_data:
            return user_data
        else:
            return None
    return None

# Функция для получения всех категорий
def get_categories():
    """Получить все категории из базы данных"""
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM categories"
        cursor.execute(query)
        categories = cursor.fetchall()

        cursor.close()
        connection.close()
        return categories
    return []

def get_category_id_by_name(category_name):
    """Получить ID категории по её названию"""
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT id_category FROM categories WHERE name = %s ORDER BY id_category"
        cursor.execute(query, (category_name,))
        category = cursor.fetchone()
        cursor.close()
        connection.close()
        if category:
            return category['id_category']
    return None

# Функция для получения подкатегорий по ID категории
def get_subcategories_by_category(category_id):
    """Получить все подкатегории для данной категории"""
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM subcategories WHERE id_category = %s"
        cursor.execute(query, (category_id,))
        subcategories = cursor.fetchall()

        cursor.close()
        connection.close()
        return subcategories
    return []

def get_products_by_subcategory(subcategory_id):
    """Получить товары для подкатегории с дополнительной информацией."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT 
                p.id_product,
                p.price,
                p.description,
                pm.name AS model_name,
                m.name AS manufacturer_name,
                pi.image_url,
                p.id_subcategory  -- Добавляем id_subcategory
            FROM 
                products p
            INNER JOIN 
                product_models pm ON p.id_model = pm.id_model
            INNER JOIN 
                manufacturers m ON pm.id_manufacturer = m.id_manufacturer
            LEFT JOIN 
                product_images pi ON p.id_product = pi.id_product
            WHERE 
                p.id_subcategory = %s
        """
        cursor.execute(query, (subcategory_id,))
        products = cursor.fetchall()

        cursor.close()
        connection.close()
        return products
    return []

def get_subcategory_id_by_name(subcategory_name):
    """Получить ID подкатегории по её названию"""
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT id_subcategory FROM subcategories WHERE name = %s"
        cursor.execute(query, (subcategory_name,))
        subcategory = cursor.fetchone()

        cursor.close()
        connection.close()
        if subcategory:
            return subcategory['id_subcategory']
    else:
        return None


def get_product_characteristics(product_id):
    """
    Получение характеристик товара по его ID.
    """
    connection = create_connection()  # Создаем подключение к базе данных
    if connection:
        cursor = connection.cursor(dictionary=True)  # Создаем курсор для выполнения запроса

        query = """
            SELECT characteristic_name, characteristic_value 
            FROM product_characteristics 
            WHERE id_product = %s
        """
        cursor.execute(query, (product_id,))
        result = cursor.fetchall()

        cursor.close()  # Закрываем курсор
        connection.close()  # Закрываем соединение с базой данных

        # Возвращаем результат в виде словаря
        return {row['characteristic_name']: row['characteristic_value'] for row in result}
    
    return {}  # Если не удалось подключиться к базе данных, возвращаем пустой словарь


def get_product_details(product_id):
    """
    Получение основных данных о товаре.
    """
    connection = create_connection()  # Создаем подключение к базе данных
    if connection:
        cursor = connection.cursor(dictionary=True)  # Создаем курсор для выполнения запроса

        query = """
            SELECT 
                products.id_product,
                product_models.name AS model_name,
                manufacturers.name AS manufacturer_name,
                products.price,
                products.description,
                product_images.image_url
            FROM products
            JOIN product_models ON products.id_model = product_models.id_model
            JOIN manufacturers ON product_models.id_manufacturer = manufacturers.id_manufacturer
            LEFT JOIN product_images ON products.id_product = product_images.id_product
            WHERE products.id_product = %s
        """
        cursor.execute(query, (product_id,))
        result = cursor.fetchone()

        cursor.close()  # Закрываем курсор
        connection.close()  # Закрываем соединение с базой данных
        return result  # Вернёт словарь с данными о товаре
    return None  # Если не удалось подключиться к базе данных


def get_product_id_by_name(product_name):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            # Разделим имя продукта на модель и производителя
            if '(' in product_name and ')' in product_name:
                # Разделяем модель и производителя
                model_name = product_name.split('(')[0].strip()
                manufacturer_name = product_name.split('(')[1].replace(')', '').strip()
                
                query = """
                    SELECT p.id_product
                    FROM products p
                    JOIN product_models pm ON p.id_model = pm.id_model
                    JOIN manufacturers m ON pm.id_manufacturer = m.id_manufacturer
                    WHERE pm.name = %s AND m.name = %s
                """
                cursor.execute(query, (model_name, manufacturer_name))  # Поиск по модели и производителю
                result = cursor.fetchone()

                if result:
                    print(f"Товар найден: {result['id_product']}")
                    return result["id_product"]
                else:
                    print(f"Товар с моделью '{model_name}' и производителем '{manufacturer_name}' не найден.")
            else:
                print(f"Неверный формат названия товара: {product_name}")
            return None
        except Exception as e:
            print(f"Ошибка при получении ID товара: {e}")
            return None
        finally:
            cursor.close()
            connection.close()
    return None


def get_product_by_id(product_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            query = """
                SELECT p.id_product, pm.name AS model_name, ma.name AS manufacturer_name,
                    p.price, p.description, p.stock_quantity, sc.name AS subcategory_name
                FROM products p
                JOIN product_models pm ON p.id_model = pm.id_model
                JOIN manufacturers ma ON pm.id_manufacturer = ma.id_manufacturer
                JOIN subcategories sc ON p.id_subcategory = sc.id_subcategory
                WHERE p.id_product = %s
            """
            cursor.execute(query, (product_id,))
            return cursor.fetchone()  # Возвращаем товар
        except Exception as e:
            print(f"Ошибка при получении данных о товаре: {e}")
            return None
        finally:
            cursor.close()
            connection.close()
    return None

# Функция для получения всех товаров в корзине пользователя
def get_cart_items(user_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            query = """
                SELECT 
                    ci.id_product,
                    CONCAT(pm.name, ' ', ma.name) AS model_name,
                    ci.quantity,
                    p.price,
                    (ci.quantity * p.price) AS total_price
                FROM cart_items ci
                JOIN products p ON ci.id_product = p.id_product
                JOIN product_models pm ON p.id_model = pm.id_model
                JOIN manufacturers ma ON pm.id_manufacturer = ma.id_manufacturer
                WHERE ci.id_user = %s
            """
            cursor.execute(query, (user_id,))
            return cursor.fetchall()  # Возвращаем все товары в корзине
        except Exception as e:
            print(f"Ошибка при получении корзины: {e}")
            return []
        finally:
            cursor.close()
            connection.close()
    return []

# Функция для добавления товара в корзину
def add_to_cart(user_id, product_id, quantity):
    connection = create_connection()  # Функция для подключения к базе
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            print("Начинаем транзакцию...")
            print(f"Параметры запроса: user_id={user_id}, product_id={product_id}, quantity={quantity}")

            # Начинаем транзакцию (необязательно)
            connection.start_transaction()

            query_check = "SELECT quantity FROM cart_items WHERE id_user = %s AND id_product = %s"
            cursor.execute(query_check, (user_id, product_id))
            result = cursor.fetchone()

            if result:
                print(f"Товар найден в корзине. Старое количество: {result['quantity']}, добавляем: {quantity}")
                new_quantity = result["quantity"] + quantity
                query_update = "UPDATE cart_items SET quantity = %s WHERE id_user = %s AND id_product = %s"
                cursor.execute(query_update, (new_quantity, user_id, product_id))
                print(f"Количество обновлено на {new_quantity}")
            else:
                print(f"Товара нет в корзине, добавляем новый товар с количеством {quantity}")
                query_insert = "INSERT INTO cart_items (id_user, id_product, quantity) VALUES (%s, %s, %s)"
                cursor.execute(query_insert, (user_id, product_id, quantity))

            # Подтверждаем транзакцию
            connection.commit()
            print("Транзакция успешно завершена.")
            return True
        except Exception as e:
            connection.rollback()  # Откатываем изменения в случае ошибки
            print(f"Ошибка при добавлении товара в корзину: {e}")
            return False
        finally:
            cursor.close()
            connection.close()
    else:
        print("Не удалось установить подключение к базе данных.")
        return False

# Функция для обновления количества товара в корзине
def update_cart_item_quantity(user_id, product_id, new_quantity):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            connection.start_transaction()

            query_stock = "SELECT stock_quantity FROM products WHERE id_product = %s"
            cursor.execute(query_stock, (product_id,))
            stock = cursor.fetchone()

            if stock and stock["stock_quantity"] >= new_quantity:
                query_update = "UPDATE cart_items SET quantity = %s WHERE id_user = %s AND id_product = %s"
                cursor.execute(query_update, (new_quantity, user_id, product_id))
                connection.commit()
                return True
            else:
                print(f"Недостаточно товара на складе. Доступно: {stock['stock_quantity']}, Запрошено: {new_quantity}")
                return False
        except Exception as e:
            connection.rollback()
            print(f"Ошибка при обновлении количества товара: {e}")
            return False
        finally:
            cursor.close()
            connection.close()
    return False

def load_cart_for_user(user_id):
    """
    Загружает корзину пользователя из базы данных.
    """
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            query = """
                SELECT 
                    ci.id_product,
                    CONCAT(pm.name, ' ', ma.name) AS product_name,
                    ci.quantity,
                    p.price,
                    (ci.quantity * p.price) AS total_price,
                    p.stock_quantity
                FROM cart_items ci
                JOIN products p ON ci.id_product = p.id_product
                JOIN product_models pm ON p.id_model = pm.id_model
                JOIN manufacturers ma ON pm.id_manufacturer = ma.id_manufacturer
                WHERE ci.id_user = %s
            """
            cursor.execute(query, (user_id,))
            cart_items = cursor.fetchall()
            return cart_items  # Список товаров в корзине
        except Exception as e:
            print(f"Ошибка при загрузке корзины: {e}")
            return []
        finally:
            cursor.close()
            connection.close()
    return []

def save_to_cart(user_id, product_id, quantity):
    """
    Сохраняет товар в корзину пользователя.
    """
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            connection.start_transaction()

            # Проверка доступности товара на складе
            query_stock = "SELECT stock_quantity FROM products WHERE id_product = %s"
            cursor.execute(query_stock, (product_id,))
            stock = cursor.fetchone()

            if not stock or stock["stock_quantity"] < quantity:
                print(f"Недостаточно товара на складе. Доступно: {stock['stock_quantity'] if stock else 0}")
                return False

            # Проверка наличия товара в корзине
            query_check = "SELECT quantity FROM cart_items WHERE id_user = %s AND id_product = %s"
            cursor.execute(query_check, (user_id, product_id))
            result = cursor.fetchone()

            if result:
                # Если товар уже в корзине, обновляем количество
                new_quantity = result["quantity"] + quantity
                query_update = "UPDATE cart_items SET quantity = %s WHERE id_user = %s AND id_product = %s"
                cursor.execute(query_update, (new_quantity, user_id, product_id))
            else:
                # Если товара нет в корзине, добавляем
                query_insert = "INSERT INTO cart_items (id_user, id_product, quantity) VALUES (%s, %s, %s)"
                cursor.execute(query_insert, (user_id, product_id, quantity))

            connection.commit()
            return True
        except Exception as e:
            connection.rollback()
            print(f"Ошибка при сохранении товара в корзину: {e}")
            return False
        finally:
            cursor.close()
            connection.close()
    return False

# Функция для очистки корзины пользователя
def clear_cart(user_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            query = "DELETE FROM cart_items WHERE id_user = %s"
            cursor.execute(query, (user_id,))
            connection.commit()
            print(f"Корзина пользователя {user_id} очищена.")
            return True
        except Exception as e:
            print(f"Ошибка при очистке корзины: {e}")
            return False
        finally:
            cursor.close()
            connection.close()
    return False