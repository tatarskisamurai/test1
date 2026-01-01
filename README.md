# CRM Система

Полнофункциональная CRM система на стеке Django + Vue.js

## Технологии

- **Backend**: Django 4.2, Django REST Framework
- **Frontend**: Vue 3, Vue Router, Pinia, Tailwind CSS
- **База данных**: SQLite (для разработки)

## Функциональность

- ✅ Управление компаниями
- ✅ Управление контактами
- ✅ Управление сделками (со статусами и вероятностями)
- ✅ Управление задачами (с приоритетами и сроками)
- ✅ Дашборд с аналитикой
- ✅ Поиск и фильтрация
- ✅ RESTful API

## Установка и запуск

### Backend (Django)

1. Перейдите в директорию backend:
```bash
cd backend
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
```

3. Активируйте виртуальное окружение:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Установите зависимости:
```bash
pip install -r requirements.txt
```

5. Примените миграции:
```bash
python manage.py migrate
```

6. Создайте суперпользователя (опционально):
```bash
python manage.py createsuperuser
```

7. Запустите сервер разработки:
```bash
python manage.py runserver
```

Backend будет доступен по адресу: http://localhost:8000

Админ панель: http://localhost:8000/admin
API: http://localhost:8000/api/

### Frontend (Vue)

1. Перейдите в директорию frontend:
```bash
cd frontend
```

2. Установите зависимости:
```bash
npm install
```

3. Запустите dev сервер:
```bash
npm run dev
```

Frontend будет доступен по адресу: http://localhost:5173

## Структура проекта

```
crm/
├── backend/              # Django backend
│   ├── crm/             # Основное приложение CRM
│   ├── crm_backend/     # Настройки Django
│   └── manage.py
├── frontend/            # Vue.js frontend
│   ├── src/
│   │   ├── views/       # Страницы приложения
│   │   ├── api/         # API клиент
│   │   └── router/      # Роутинг
│   └── package.json
└── README.md
```

## API Endpoints

- `GET /api/companies/` - Список компаний
- `POST /api/companies/` - Создать компанию
- `GET /api/companies/{id}/` - Детали компании
- `PATCH /api/companies/{id}/` - Обновить компанию
- `DELETE /api/companies/{id}/` - Удалить компанию

- `GET /api/contacts/` - Список контактов
- `POST /api/contacts/` - Создать контакт
- `GET /api/contacts/{id}/` - Детали контакта
- `PATCH /api/contacts/{id}/` - Обновить контакт
- `DELETE /api/contacts/{id}/` - Удалить контакт

- `GET /api/deals/` - Список сделок
- `POST /api/deals/` - Создать сделку
- `GET /api/deals/{id}/` - Детали сделки
- `PATCH /api/deals/{id}/` - Обновить сделку
- `DELETE /api/deals/{id}/` - Удалить сделку
- `GET /api/deals/statistics/` - Статистика по сделкам

- `GET /api/tasks/` - Список задач
- `POST /api/tasks/` - Создать задачу
- `GET /api/tasks/{id}/` - Детали задачи
- `PATCH /api/tasks/{id}/` - Обновить задачу
- `DELETE /api/tasks/{id}/` - Удалить задачу
- `GET /api/tasks/overdue/` - Просроченные задачи
- `GET /api/tasks/upcoming/` - Предстоящие задачи

- `GET /api/dashboard/stats/` - Общая статистика дашборда

## Особенности

- Современный и отзывчивый UI с Tailwind CSS
- Полнофункциональный REST API
- Поиск и фильтрация данных
- Статистика и аналитика на дашборде
- Связи между сущностями (компании-контакты-сделки-задачи)
- Статусы сделок и приоритеты задач
- Отслеживание просроченных задач

## Лицензия

MIT

