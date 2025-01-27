import pytest
import numpy as np
from EXAMPLE_chunking_embs import chunk_text, get_embeddings, process_courses


# Тест для функции chunk_text
def test_chunk_text():
    # Тестируем функцию чанкования для текста, который длиннее, чем размер чанка
    text = "This is a very long description that should be chunked into smaller parts."
    chunks = chunk_text(text, chunk_size=20)

    # Проверяем, что количество чанков верное
    assert len(chunks) == 3

    # Проверяем содержание первого и последнего чанка
    assert chunks[0] == "This is a very long"
    assert chunks[-1] == "into smaller parts."

    # Проверяем, что последний чанк не пустой
    assert chunks[-1] != ""

    # Проверяем, что все чанки меньше или равны по размеру 20 символов
    for chunk in chunks:
        assert len(chunk) <= 20


# Тест для функции get_embeddings
def test_get_embeddings():
    # Пример текста, который будет преобразован в эмбеддинги
    texts = ["This is a test sentence.", "This is another sentence."]

    # Получаем эмбеддинги
    embeddings = get_embeddings(texts)

    # Проверяем, что эмбеддинги возвращаются как массив numpy
    assert isinstance(embeddings, np.ndarray)

    # Проверяем размерность эмбеддингов
    assert embeddings.shape[0] == 2  # Мы передали 2 текста, должно быть 2 эмбеддинга
    assert embeddings.shape[1] == 384  # Проверяем размерность эмбеддинга, если используем 'all-MiniLM-L6-v2'


# Тест для функции process_courses
def test_process_courses():
    # Пример данных о курсах
    courses_data = [
        {"title": "Course 1", "description": "This is the description of course 1."},
        {"title": "Course 2", "description": "This is the description of course 2."}
    ]

    # Запускаем обработку курсов
    embeddings, titles = process_courses(courses_data)

    # Проверяем, что для каждого курса были созданы эмбеддинги
    assert len(embeddings) == 4  # 2 курса, каждый из которых был разделен на 2 чанка (по 2 эмбеддинга на курс)
    assert len(titles) == 4

    # Проверяем, что названия курсов корректно связаны с эмбеддингами
    assert titles[:2] == ["Course 1", "Course 1"]
    assert titles[2:] == ["Course 2", "Course 2"]

