def total_salary(path):
        
    total = 0
    developers = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    total += int(line.strip().split(',')[1])
                    developers += 1
                except ValueError:
                    print(f"Невірний формат даних: {line.strip()}")
                
    except FileNotFoundError:
        print("Не вдалося знайти файл.")
    # except ZeroDivisionError:
    #     print("Файл порожній.")
    except Exception as e:
        print(f"Помилка: {e}")
    if developers == 0:
        return 0, 0
    else:
        average = int(total / developers)
        return total, average

print(total_salary('./salary_file.txt'))


    
    