import pytest
import numpy as np
import os
import faiss
from index import create_and_save_index  # Импортировать вашу функцию

def test_create_and_save_index():
    # Мокаем эмбеддинги для теста
    embeddings = np.random.rand(10, 384).tolist()  # 10 эмбеддингов размерности 384
    create_and_save_index(embeddings, filename="test_index.index")

    # Проверяем, что файл был создан
    assert os.path.exists("test_index.index")

    # Загружаем индекс и проверяем его размеры
    index = faiss.read_index("test_index.index")
    assert index.ntotal == 10  # Проверка, что в индексе 10 векторов

def test_index_dimensions():
    # Проверяем, что размерность индекса совпадает с размерностью эмбеддингов
    embeddings = np.random.rand(5, 384).tolist()  # 5 эмбеддингов размерности 384
    create_and_save_index(embeddings, filename="test_dim_index.index")

    index = faiss.read_index("test_dim_index.index")
    assert index.d == 384  # Размерность индекса должна быть 384
