import pytest
import requests_mock
from fetch_course_data import fetch_course_data, fetch_all_courses, save_courses, fetch_courses

# Мокируем URL для тестов
BASE_URLS = [
    "https://karpov.courses/analytics",
    "https://karpov.courses/analytics-hard"
]

@pytest.fixture
def mock_requests():
    with requests_mock.Mocker() as mock:
        # Мокируем ответы для каждого из URL
        mock.get("https://karpov.courses/analytics", text='<html><head><title>Analytics Course</title></head><body><div class="tn-atom">Description of the Analytics course</div></body></html>')
        mock.get("https://karpov.courses/analytics-hard", text='<html><head><title>Hard Analytics Course</title></head><body><div class="tn-atom">Description of the Hard Analytics course</div></body></html>')
        yield mock

def test_fetch_course_data(mock_requests):
    # Тестируем корректность парсинга одного курса
    course_data = fetch_course_data("https://karpov.courses/analytics")
    assert course_data is not None
    assert course_data['title'] == "Analytics Course"
    assert "Description of the Analytics course" in course_data['description']
    assert course_data['url'] == "https://karpov.courses/analytics"

def test_fetch_all_courses(mock_requests):
    # Тестируем извлечение данных о курсах с нескольких страниц
    courses = fetch_all_courses(BASE_URLS)
    assert len(courses) == 2
    assert courses[0]['title'] == "Analytics Course"
    assert courses[1]['title'] == "Hard Analytics Course"

def test_save_courses(mock_requests, tmpdir):
    # Тестируем сохранение данных о курсах в файл
    courses = fetch_all_courses(BASE_URLS)
    save_path = tmpdir.join("courses_data.json")
    save_courses(courses, str(save_path))

    # Проверяем, что файл существует и в нем есть данные
    assert save_path.exists()
    with open(save_path, 'r', encoding='utf-8') as f:
        data = f.read()
        assert '"title": "Analytics Course"' in data
        assert '"title": "Hard Analytics Course"' in data

def test_fetch_courses(mock_requests):
    # Тестируем основную функцию, которая сохраняет данные
    courses_count = fetch_courses(BASE_URLS)
    assert courses_count == 2
