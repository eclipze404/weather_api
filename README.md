# Запуск проекта

## Требования

Python 3.13.3
pip

---

## 1. Клонирование проекта

```bash
git clone <repo_url>
cd <project_folder>
```

---

## 2. Создание виртуального окружения

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

---

## 4. Запуск проекта

Точка входа приложения - `main.py`.

Команда запуска:

```bash
fastapi dev main.py
```

---

## 5. Доступ к API

После запуска сервер будет доступен по адресу:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```
