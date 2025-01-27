import requests
from bs4 import BeautifulSoup
import json

# URL страницы с курсами
BASE_URLS = \
    ["https://karpov.courses/analytics",
"https://karpov.courses/analytics-hard",
"https://karpov.courses/ml-hard",
"https://karpov.courses/systemdesign",
"https://karpov.courses/data-driven",
"https://karpov.courses/dataengineer-start",
"https://karpov.courses/deep-learning",
"https://karpov.courses/dataengineer",
"https://karpov.courses/ml-start",
]


def fetch_course_data(url):
    """
    Функция для извлечения данных о курсе с конкретной страницы.
    """
    # Ждем ваше решение здесь!

    pass


def fetch_all_courses(BASE_URLS=BASE_URLS):
    """
    Функция для извлечения данных о курсах с нескольких страниц.
    """
    # Ждем ваше решение здесь!
    pass


def save_courses(courses, filename="courses_data.json"):
    """
    Сохраняет данные о курсах в файл JSON.
    """
    # Ждем ваше решение здесь!
    pass
def fetch_courses(BASE_URLS):
    # Ждем ваше решение здесь!
    pass


if __name__ == "__main__":
    # Собираем данные с нескольких сайтов
    courses = fetch_all_courses()
    if courses:
        save_courses(courses)
        print(f"Найдено {len(courses)} курсов. Данные сохранены.")
    else:
        print("Курсы не были найдены.")