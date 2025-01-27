from sentence_transformers import SentenceTransformer
import numpy as np

# Загрузка модели для получения эмбеддингов
model = SentenceTransformer('all-MiniLM-L6-v2')

def chunk_text(text, chunk_size=200):
    """
    Функция для чанкования текста на более мелкие части.
    """
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks

def get_embeddings(texts):
    """
    Функция для получения эмбеддингов через Sentence Transformers.
    """
    embeddings = model.encode(texts)
    return embeddings

def process_courses(courses_data):
    """
    Процессинг курсов: чанкование, создание эмбеддингов.
    """
    all_embeddings = []
    all_titles = []

    for course in courses_data:
        title = course['title']
        description = course['description']

        # Чанкование текста
        chunks = chunk_text(description)

        # Генерация эмбеддингов для каждого чанка
        embeddings = get_embeddings(chunks)

        # Сохраняем эмбеддинги и название курса
        all_embeddings.extend(embeddings)
        all_titles.extend([title] * len(embeddings))  # Сохраняем название для каждого чанка

    return all_embeddings, all_titles
