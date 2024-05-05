def get_cats_info(path):
            
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    id, name, age = line.strip().split(',')
                    cats_info.append({'id': id, 'name': name, 'age': age})
                except ValueError:
                    print("Неправильний формат даних.")
    except FileNotFoundError:
        print("Не вдалося знайти файл.")           
    except Exception as e:
        print(f"Помилка: {e}")
    return cats_info

print(get_cats_info('./cats.txt'))

