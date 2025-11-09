## Тестовое задание от Effective Mobile

#### Задача: покрыть UI тестами разделы главное страницы effective-mobile.ru.

#### Структура проекта
```angular2html
effective_mobile_aqa_task/
├─ configs/
│  └─ env_test_config.py        # загрузка переменных окружения для тестов
├─ pages/
│  ├─ base_page.py              # базовый класс Page
│  └─ main_page.py              # Page Object для главной страницы
├─ tests/
│  ├─ allure_report/            # папка для артефактов Allure (отчёты)
│  ├─ conftest.py               # фикстуры pytest
│  ├─ __init__.py
│  └─ ui_tests/
│     ├─ test_main_page.py      # тесты для main_page (UI тесты)
│     └─ __init__.py            
├─ .env                         # файл с переменными окружения
├─ Dockerfile                   # инструкция для сборки контейнера (для CI/запуска)
├─ README.md                    # описание проекта, инструкция по запуску
└─ requirements.txt             

```
Технологический стек проекта:
1. Python v3.10
2. pytest v8.4.2
3. Allure v2.15.0
4. selenium v4.38.0

Требования:
1. Установленый и настроенный Docker для запуска и выполнения тестов;
2. Минимум 4Gb свободной памяти на машине для сборки Docker образа 
3. Пользователю необходимо находится в корневой папке проекта.

Создание Docker образа через CLI:
```angular2html
docker build -t effective-mobile-tests .
```
Запуск контейнера на основе образа через CLI для выполнения тестов:
```angular2html
docker run -v "$(pwd)/tests/allure_report:/app/tests/allure_report" effective-mobile-tests --browser=chrome
```
где --browser - параметр для выбора браузера, в котором будут выполняться тесты. На выбор доступны:
* --browser=chrome (по умолчанию)
* --browser=firefox

После выполнения тестов в папке *tests/allure_report* будет загружен Allure отчёт.
Для просмотра отчета необходимо открыть файл index.html