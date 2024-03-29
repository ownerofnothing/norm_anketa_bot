total_score = {"Флоренс Васси": 0, "Фредди Трампер": 0, "Анатолий Сергиевский": 0, "Товарищ Молоков": 0, "Арбитр": 0}
all_questions = {
    1: {
        "question": "Цель оправдывает средства?",
        "answers": {
            "Да": {"Анатолий Сергиевский": 5, "Товарищ Молоков": 5, "Фредди Трампер": 3, "Флоренс Васси": 0, "Арбитр": 0},
            "Нет": {"Анатолий Сергиевский": 0, "Товарищ Молоков": 0, "Фредди Трампер": 0, "Флоренс Васси": 3, "Арбитр": 0},
            "Смотря, какая цель и какие средства": {"Анатолий Сергиевский": 0, "Товарищ Молоков": 0, "Фредди Трампер": 0, "Флоренс Васси": 0, "Арбитр": 4}
        }
    },
    2: {
        "question": "Что может сделать Вас счастливым(-ой)?",
        "answers": {
            "Исполнение моих целей": {"Анатолий Сергиевский": 5, "Товарищ Молоков": 3, "Фредди Трампер": 3, "Флоренс Васси": 1, "Арбитр": 1},
            "Только я сам(-а)": {"Анатолий Сергиевский": 2, "Товарищ Молоков": 1, "Фредди Трампер": 2, "Флоренс Васси": 5, "Арбитр": 1},
            "Когда все играют по правилам": {"Анатолий Сергиевский": 1, "Товарищ Молоков": 0, "Фредди Трампер": 1, "Флоренс Васси": 2, "Арбитр": 4},
            "Тепло и забота": {"Анатолий Сергиевский": 1, "Товарищ Молоков": 0, "Фредди Трампер": 5, "Флоренс Васси": 2, "Арбитр": 2}
        }
    },
    3: {
        "question": "Вам легко в общении с окружающими?",
        "answers": {
            "Это окружающим нелегко со мной": {"Анатолий Сергиевский": 0, "Товарищ Молоков": 3, "Фредди Трампер": 5, "Флоренс Васси": 0, "Арбитр": 0},
            "Да, вполне": {"Анатолий Сергиевский": 1, "Товарищ Молоков": 3, "Фредди Трампер": 0, "Флоренс Васси": 4, "Арбитр": 5},
            "Достаточно сложно": {"Анатолий Сергиевский": 4, "Товарищ Молоков": 0, "Фредди Трампер": 3, "Флоренс Васси": 0, "Арбитр": 0},
        }
    },
    4: {
        "question": "Вы доверяете людям?",
        "answers": {
            "К сожалению, да": {"Анатолий Сергиевский": 0, "Товарищ Молоков": 0, "Фредди Трампер": 0, "Флоренс Васси": 4, "Арбитр": 0},
            "Нет": {"Анатолий Сергиевский": 5, "Товарищ Молоков": 3, "Фредди Трампер": 0, "Флоренс Васси": 0, "Арбитр": 0},
            "Зависит от человека": {"Анатолий Сергиевский": 0, "Товарищ Молоков": 0, "Фредди Трампер": 0, "Флоренс Васси": 0, "Арбитр": 4},
            "Нет, но хочу": {"Анатолий Сергиевский": 0, "Товарищ Молоков": 0, "Фредди Трампер": 4, "Флоренс Васси": 0, "Арбитр": 0}
        }
    }
}
start_text = "Если готовы приступить к тестированию, нажмите /go. Справку об использовании анкетой можно найти здесь /help"
help_text = ("/start - запуск бота\n"
             "/go - начало теста\n"
             "/help - сводка доступных команд\n"
             "/restart - начать проходить анкету заново\n")
freddie = ("Фредди Трампер\n"
           "Вы дерзки, немного эгоистичны и высоко цените свою работу.\n"
           "Возможно, несколько скандальны.\n"
           "В глубине души очень ранимые и чувственные, подсознательно ищете любви и заботы.")
tolya = ("Анатолий Сергиевский\n"
         "Вы холодны и рассудительны, привыкли продумывать всё наперёд.\n"
         "Всё время напряжены, идёте к своим целям, чего бы это не стоило.")
molokov = ("Товарищ Молоков\n"
           "Вы - образец. Вы являетесь частью крепкой системы, и ради неё готовы на многое (иногда слишком многое).\n"
           "Преданны своему делу, хитры и умеете договариваться.")
florence = ("Флоренс Васси\n"
            "Вы человек независимый и знающий себе цену, но умеющий любить")
arbitr = ("Арбитр\n"
          "Вы достаточно загадочная личность. Рассудительны и дисциплинированны.\n"
          "В Вашей жизни существуют чёткие правила, которым Вы сами решили следовать.")
