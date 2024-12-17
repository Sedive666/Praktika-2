
class SportsStore:
    def __init__(self):
        self.users = []
        self.products = [
            {'name': 'Кроссовки Nike Air Max', 'brand': 'Nike', 'category': 'Кроссовки', 'price': 11990, 'quantity': 22},
            {'name': 'Кроссовки Adidas Ozelia', 'brand': 'Adidas', 'category': 'Кроссовки', 'price': 8990, 'quantity': 56},
            {'name': 'Кроссовки Nike Air Jordan 1 Low', 'brand': 'Nike', 'category': 'Кроссовки', 'price': 14990, 'quantity': 24},
            {'name': 'Кроссовки New Balance 9060', 'brand': 'New Balance', 'category': 'Кроссовки', 'price': 14990, 'quantity': 24},
            {'name': 'Кеды Adidas Stan Smith', 'brand': 'Adidas', 'category': 'Кеды', 'price': 9790, 'quantity': 36},
            {'name': 'Кеды Nike Court Vision Mid Next Nature', 'brand': 'Nike', 'category': 'Кеды', 'price': 10990, 'quantity': 13},
            {'name': 'Кеды утепленные Nike Lunar Force 1', 'brand': 'Nike', 'category': 'Кеды', 'price': 35990, 'quantity': 12},
            {'name': 'Кеды PUMA Caven 2.0 Wip', 'brand': 'Puma', 'category': 'Кеды', 'price': 4990, 'quantity': 20},
            {'name': 'Ботинки Columbia Landroamer Explorer WP', 'brand': 'Columbia', 'category': 'Ботинки', 'price': 13290, 'quantity': 2},
            {'name': 'Ботинки Outventure Cheget Mid', 'brand': 'Outventure', 'category': 'Ботинки', 'price': 6090, 'quantity': 15},
            {'name': 'Ботинки утепленные Northland Innsbruck 2', 'brand': 'Northland', 'category': 'Ботинки', 'price': 6590, 'quantity': 8},
            {'name': 'Ботинки утепленные Outventure Forester', 'brand': 'Outventure', 'category': 'Ботинки', 'price': 3590, 'quantity': 25}
        ]
        self.current_user = None

    def add_user(self, username, password, role='user'):
        user = {
            'username': username,
            'password': password,
            'role': role,
            'purchase_history': []
        }
        self.users.append(user)
        print(f"Пользователь '{username}' добавлен.")

    def add_product(self, name, brand, category, price, quantity):
        try:
            price = float(price)
            quantity = int(quantity)
            if price <= 0 or quantity <= 0:
                raise ValueError("Цена и количество должны быть положительными числами.")
            if not name or not brand or not category:
                raise ValueError("Название, бренд и категория товара не могут быть пустыми.")
            self.products.append({'name': name, 'brand': brand, 'category': category, 'price': price, 'quantity': quantity})
            print(f"Товар '{name}' добавлен.")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def login(self, username, password):
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                self.current_user = user
                return True
        return False

    def logout(self):
        self.current_user = None
        print("Вы вышли из системы.")

    def view_products(self):
        if self.products:
            print("Доступные товары:")
            for product in self.products:
                print(f"- {product['name']} ({product['brand']}), {product['category']}, цена: {product['price']} руб., в наличии: {product['quantity']}")
        else:
            print("Товаров нет.")

    def buy_product(self, product_name):
        if not self.current_user:
            print("Пожалуйста, войдите в систему.")
            return

        for product in self.products:
            if product['name'] == product_name and product['quantity'] > 0:
                self.current_user['purchase_history'].append(product)
                product['quantity'] -= 1
                print(f"Вы купили товар: {product_name}")
                return
        print("Товар не найден или закончился.")

    def search_products(self, search_term):
        results = [p for p in self.products if search_term.lower() in p['name'].lower()]
        if results:
            print("Результаты поиска:")
            for product in results:
                print(f"- {product['name']} ({product['brand']}), {product['category']}, цена: {product['price']} руб., в наличии: {product['quantity']}")
        else:
            print("Товары не найдены.")

    def filter_products(self, criterion, threshold):
        filtered_products = [p for p in self.products if p.get(criterion, 0) <= threshold] #Handle missing keys gracefully
        if filtered_products:
            print("Отфильтрованные товары:")
            for product in filtered_products:
                print(f"- {product['name']} ({product['brand']}), {product['category']}, цена: {product['price']} руб., в наличии: {product['quantity']}")
        else:
            print("Товары не соответствуют критериям фильтрации.")


    def view_purchase_history(self):
        if not self.current_user:
            print("Пожалуйста, войдите в систему.")
            return

        if self.current_user['purchase_history']:
            print("Ваша история покупок:")
            for product in self.current_user['purchase_history']:
                print(f"- {product['name']}")
        else:
            print("Вы еще ничего не купили.")

    def search_user(self, username):
        results = [u for u in self.users if username.lower() in u['username'].lower()]
        if results:
            print("Результаты поиска пользователей:")
            for user in results:
                print(f"- {user['username']} ({user['role']})")
        else:
            print("Пользователи не найдены.")

    def user_menu(self):
        while True:
            print("\nМеню пользователя:")
            print("1. Просмотреть товары")
            print("2. Купить товар")
            print("3. Просмотреть историю покупок")
            print("4. Фильтрация товаров")
            print("5. Поиск товара")
            print("0. Выйти")
            choice = input("Выберите действие: ")

            try:
                if choice == '1':
                    self.view_products()
                elif choice == '2':
                    self.view_products()
                    product_name = input("Введите название товара для покупки: ")
                    self.buy_product(product_name)
                elif choice == '3':
                    self.view_purchase_history()
                elif choice == '4':
                    criterion = input("Введите критерий фильтрации (price, quantity): ")
                    while True:
                        try:
                            threshold = float(input(f"Введите пороговое значение для {criterion}: "))
                            break
                        except ValueError:
                            print("Некорректное значение. Попробуйте снова.")
                    self.filter_products(criterion, threshold)
                elif choice == '5':
                    search_term = input("Введите поисковый запрос: ")
                    self.search_products(search_term)
                elif choice == '0':
                    break
                else:
                    print("Неверный выбор. Попробуйте снова.")
            except ValueError as e:
                print(f"Ошибка: {e}")
            except Exception as e:
                print(f"Произошла непредвиденная ошибка: {e}")


    def edit_product(self, product_name):
        if not self.current_user or self.current_user['role'] != 'admin':
            print("У вас нет прав для редактирования товаров.")
            return

        product_found = False
        for product in self.products:
            if product['name'] == product_name:
                while True:
                    try:
                        new_price = float(input("Введите новую цену: "))
                        if new_price <= 0:
                            raise ValueError("Цена должна быть положительным числом.")
                        break
                    except ValueError as e:
                        print(f"Ошибка: {e}")

                while True:
                    try:
                        new_quantity = int(input("Введите новое количество: "))
                        if new_quantity < 0:
                            raise ValueError("Количество не может быть отрицательным.")
                        break
                    except ValueError as e:
                        print(f"Ошибка: {e}")

                product['price'] = new_price
                product['quantity'] = new_quantity
                print(f"Товар '{product_name}' обновлен.")
                product_found = True
                break
        if not product_found:
            print("Товар не найден.")

    def admin_menu(self):
        if not self.current_user or self.current_user['role'] != 'admin':
            print("У вас нет доступа к администраторскому меню.")
            return

        while True:
            print("\nМеню администратора:")
            print("1. Добавить товар")
            print("2. Редактировать товар")
            print("3. Просмотреть список пользователей")
            print("0. Выйти в главное меню")
            choice = input("Выберите действие: ")
            try:
                if choice == '1':
                    name = input("Введите название товара: ")
                    brand = input("Введите бренд: ")
                    category = input("Введите категорию: ")
                    while True:
                        try:
                            price = float(input("Введите цену: "))
                            if price <= 0:
                                raise ValueError("Цена должна быть положительным числом.")
                            break
                        except ValueError as e:
                            print(f"Ошибка: {e}")
                    while True:
                        try:
                            quantity = int(input("Введите количество: "))
                            if quantity <= 0:
                                raise ValueError("Количество должно быть положительным числом.")
                            break
                        except ValueError as e:
                            print(f"Ошибка: {e}")
                    self.add_product(name, brand, category, price, quantity)
                elif choice == '2':
                    self.view_products()
                    product_name = input("Введите название товара для редактирования: ")
                    self.edit_product(product_name)
                elif choice == '3':
                    self.view_users()
                elif choice == '0':
                    break
                else:
                    print("Неверный выбор. Попробуйте снова.")
            except ValueError as e:
                print(f"Ошибка: {e}")
            except Exception as e:
                print(f"Произошла непредвиденная ошибка: {e}")


    def view_users(self):
        print("Список пользователей:")
        for user in self.users:
            print(f"- {user['username']} ({user['role']})")

    def search_user(self, username):
        found = False
        for user in self.users:
            if username.lower() in user['username'].lower():
                print(f"Найден пользователь: {user['username']} ({user['role']})")
                found = True
        if not found:
            print("Пользователь не найден.")


    def register_user(self):
        username = input("Введите логин для нового пользователя: ")
        password = input("Введите пароль для нового пользователя: ")
        self.add_user(username, password)
        print(f"Пользователь {username} успешно зарегистрирован!")

    def run(self):
        while True:
            print("\nДобро пожаловать в интернет-магазин спортивных товаров!")
            print("1. Войти в систему")
            print("2. Зарегистрироваться")
            print("0. Выйти")
            choice = input("Выберите действие: ")

            if choice == '1':
                username = input("Логин: ")
                password = input("Пароль: ")
                if self.login(username, password):
                    print(f"Добро пожаловать, {self.current_user['username']}!")
                    if self.current_user['role'] == 'admin':
                        self.admin_menu()
                    else:
                        self.user_menu()
                else:
                    print("Неправильный логин или пароль.")
            elif choice == '2':
                self.register_user()
            elif choice == '0':
                break
            else:
                print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    store = SportsStore()
    store.add_user('admin', 'admin123', role='admin')
    store.add_user('user', 'user123')
    store.run()
