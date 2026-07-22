habits = []

# Счётчик дней (один "день" — один запуск программы)
current_day = 1

# ============================================================
# 2. ПРИВЕТСТВИЕ
# ============================================================
print("=" * 40)
print("ТРЕКЕР ПРИВЫЧЕК")
print("=" * 40)
print("День " + str(current_day))
print()

# ============================================================
# 3. ГЛАВНЫЙ ЦИКЛ
# ============================================================
running = True

while running:

    # Ждём команду
    command = input("> ").strip().lower()

    if command == "":
        continue

    parts = command.split()
    action = parts[0]

    # ====================
    # ПОМОЩЬ
    # ====================
    if action in ["помощь", "пом", "?", "help"]:
        print()
        print("=== КОМАНДЫ ===")
        print("добавить [название]     — добавить новую привычку")
        print("удалить [название]      — удалить привычку")
        print("список / все            — показать все привычки")
        print("отметить [название]     — отметить привычку сегодня")
        print("сбросить [название]     — сбросить отметку сегодня")
        print("статистика              — показать статистику")
        print("новый_день              — начать новый день")
        print("помощь / ?              — показать команды")
        print("выход                   — выйти")
        print()

    # ====================
    # ВЫХОД
    # ====================
    elif action in ["выход", "выйти", "quit", "exit"]:
        print("До свидания!")
        running = False

    # ====================
    # ДОБАВИТЬ ПРИВЫЧКУ
    # ====================
    elif action in ["добавить", "add"]:
        if len(parts) < 2:
            print("Укажите название привычки.")
            continue

        # Собираем название (может быть из нескольких слов)
        name = ""
        for i in range(1, len(parts)):
            if i > 1:
                name += " "
            name += parts[i]

        # Проверяем, нет ли уже такой привычки
        already_exists = False
        for habit in habits:
            if habit["name"] == name:
                already_exists = True
                break

        if already_exists:
            print("Привычка '" + name + "' уже существует.")
        else:
            new_habit = {
                "name": name,
                "streak": 0,
                "total": 0,
                "done_today": False
            }
            habits.append(new_habit)
            print("Добавлена привычка: " + name)

    # ====================
    # УДАЛИТЬ ПРИВЫЧКУ
    # ====================
    elif action in ["удалить", "delete", "remove"]:
        if len(parts) < 2:
            print("Укажите название привычки.")
            continue

        # Собираем название
        name = ""
        for i in range(1, len(parts)):
            if i > 1:
                name += " "
            name += parts[i]

        found = False
        for i in range(len(habits)):
            if habits[i]["name"] == name:
                habits.pop(i)
                print("Удалена привычка: " + name)
                found = True
                break

        if not found:
            print("Привычка '" + name + "' не найдена.")

    # ====================
    # СПИСОК ПРИВЫЧЕК
    # ====================
    elif action in ["список", "все", "list", "all"]:
        if len(habits) == 0:
            print("У вас пока нет привычек. Добавьте первую: добавить [название]")
        else:

            print()

            print("=== ВАШИ ПРИВЫЧКИ (День " + str(current_day) + ") ===")

            count = 1
            for habit in habits:
                status = "✅" if habit["done_today"] else "❌"
                print(str(count) + ". " + status + " " + habit["name"])
                print("   Серия: " + str(habit["streak"]) + " дн. | Всего: " + str(habit["total"]) + " дн.")
                count += 1
            print()
    elif action in ["отметить", "done", "check", "+"]:
        if len(parts) < 2:
            print("Укажите название привычки.")
            continue
        name = ""
        for i in range(1, len(parts)):
            if i > 1:
                name += " "
            name += parts[i]
        found = False
        for habit in habits:
            if habit["name"] == name:
                found = True

                if habit["done_today"]:
                    print("Привычка '" + name + "' уже отмечена сегодня.")

                else:
                    habit["done_today"] = True


                    habit["total"] += 1


                    habit["streak"] += 1


                    print("✅ Привычка '" + name + "' отмечена!")
                    print("   Серия: " + str(habit["streak"]) + " дн.")


                break


        if not found:
            print("Привычка '" + name + "' не найдена.")
    elif action in ["сбросить", "undo", "uncheck", "-"]:
        if len(parts) < 2:
            print("Укажите название привычки.")
            continue
        name = ""
        for i in range(1, len(parts)):
            if i > 1:
                name += " "
            name += parts[i]
        found = False
        for habit in habits:
            if habit["name"] == name:
                found = True
            if not habit["done_today"]:
                print("Привычка '" + name + "' не была отмечена сегодня.")

            else:
                habit["done_today"] = False


                habit["total"] -= 1


                habit["streak"] -= 1

                print("❌ Отметка снята с привычки '" + name + "'.")

            break

            if not found:
                print("Привычка '" + name + "' не найдена.")
    elif action in ["статистика", "стат", "stats", "stat"]:
        if len(habits)==0:
            print("У вас пока нет привычек")
        else:
            print()
            print("=== СТАТИСТИКА ===")
            print("День: " + str(current_day))
            print()
            done_today_count = 0

            for habit in habits:
                if habit["done_today"]:
                    done_today_count += 1

            total_habits = len(habits)
            print("Выполнено сегодня: " + str(done_today_count) + "/" + str(total_habits))

            if total_habits > 0:
                percent = done_today_count * 100 // total_habits
            bar = " "
            filled = percent // 10
            for i in range(10):
                if i < filled:
                    bar += "█"
                else:
                    bar += "░"
            print("Прогресс: "+ bar + " " + str(percent) + "%")

            print()


            sorted_habits = []
            for habit in habits:
                sorted_habits.append(habit)
            for i in range(len(sorted_habits)):
                for j in range(len(sorted_habits) - 1 - i):
                    if sorted_habits[j]["streak"] < sorted_habits[j + 1]["streak"]:
                        temp = sorted_habits[j]
                        sorted_habits[j] = sorted_habits[j + 1]
                        sorted_habits[j + 1] = temp
            print("Топ по сериям")
            count = 1
            for habit in sorted_habits:
                if count < 3:

                    medal = " "
                    if count == 1:
                        medal = "🥇"
                    elif count == 2:
                        medal = "🥈"
                    elif count == 3:
                        medal = "🥉"
                    print("  " + medal + " " + habit["name"] + " — " + str(habit["streak"]) + " дн. подряд")
                    count += 1
            print()

            total_all = 0
            for habit in habits:
                total_all += habit["total"]
            print("Всего отметок за все время:"+ str(total_all))
            print()
    elif action in ["новый день","next_day","day"]:
        current_day += 1

        for habit in habits:
            if not habit["done_today"]:
                habit["done_today"] = False
    print()
    print("=" * 40)
    print("ДЕНЬ " + str(current_day))
    print("=" * 40)
    print("Серии сброшены для невыполненных привычек.")
    print()

else:
    print("Неизвестная команда.Введите 'помощь' для списка команд ")
print()
print("Всего дней: " + str(current_day))
total_habits = len(habits)
if total_habits > 0:


    print("Привычек создано: " + str(total_habits))

    total_done = 0
    for habit in habits:
        total_done += habit["total"]


    print("Всего отметок: " + str(total_done))





















