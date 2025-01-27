import openai
import numpy as np
import json
from llm.embedder import get_query_embedding, search_courses, load_faiss_index, load_courses_data

# Настройка API OpenAI
openai.api_key = "YOUR_OPENAI_API_KEY"


def process_user_query(query, top_k=5):
    """
    Обработка запроса пользователя с использованием LLM API и FAISS индекса.
    Если доступ к LLM API отсутствует, возвращаем только результаты поиска.
    """
    # Получаем эмбеддинг запроса
    query_embedding = get_query_embedding(query)

    # Загружаем FAISS индекс и данные о курсах
    index = load_faiss_index("course_embeddings.index")
    courses_data = load_courses_data("courses_data.json")

    # Ищем похожие курсы по запросу
    recommended_courses = search_courses(query_embedding, index, courses_data, top_k=top_k)

    # Если API доступен, используем LLM для детального ответа
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Ответь на запрос: {query}. Рекомендуемые курсы: {', '.join(recommended_courses)}.",
            max_tokens=150
        )
        llm_answer = response.choices[0].text.strip()
        return llm_answer
    except openai.error.OpenAIError:
        # В случае ошибки (например, квота исчерпана) возвращаем результаты поиска
        return f"Рекомендуемые курсы по запросу: {', '.join(recommended_courses)}."


if __name__ == "__main__":
    query = "Как изучать машинное обучение?"
    answer = process_user_query(query)
    print(answer)
