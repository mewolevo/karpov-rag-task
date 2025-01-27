# Указываем переменные
VENV_NAME=venv
PYTHON=python3
PIP=pip
PYTEST=pytest

# Создание виртуального окружения
create-venv:
	$(PYTHON) -m venv $(VENV_NAME)
	$(VENV_NAME)/bin/$(PIP) install --upgrade pip

# Установка зависимостей
install-dependencies: create-venv
	$(VENV_NAME)/bin/$(PIP) install -r requirements.txt

# Удаление виртуального окружения
remove-venv:
	rm -rf $(VENV_NAME)

# Запуск тестов
run-tests:
	$(VENV_NAME)/bin/$(PYTEST) tests/

# Установка зависимостей и запуск тестов
test: install-dependencies run-tests

# Очистка окружения (удаляет виртуальное окружение и все временные файлы)
clean: remove-venv
