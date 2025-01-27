import faiss
import numpy as np

def create_and_save_index(embeddings, filename="course_embeddings.index"):
    """
    Функция для создания индекса FAISS и сохранения его в файл.
    """
    # 1. Размерность эмбеддингов
    dimension = len(embeddings[0])

    # 2. Создаем индекс с метрикой L2
    index = faiss.IndexFlatL2(dimension)

    # 3. Добавляем эмбеддинги в индекс
    embeddings_np = np.array(embeddings).astype('float32')  # Преобразуем в numpy array
    index.add(embeddings_np)

    # 4. Сохраняем индекс в файл
    faiss.write_index(index, filename)
    print(f"Индекс сохранен в {filename}")
    return index
