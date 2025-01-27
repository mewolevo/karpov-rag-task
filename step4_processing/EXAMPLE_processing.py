import openai
import numpy as np
import json

# Настройка API OpenAI
openai.api_key = "YOUR_OPENAI_API_KEY"


def process_user_query(query, recommended_courses=['аналитика']):
    """
    Обработка запроса пользователя с использованием LLM API.
    Если доступ к LLM API отсутствует, возвращаем только результаты поиска.
    """

    # Если API доступен, используем LLM для детального ответа
    try:
        response = openai.chat.completions.create(
            model="text-davinci-003",
            prompt=f"Ответь на запрос: {query}. Рекомендуемые курсы: {', '.join(recommended_courses)}.",
            max_tokens=150
        )
        llm_answer = response['choices'][0]['text']
        return llm_answer
    except Exception:
        print(Exception)
        # В случае ошибки (например, квота исчерпана) возвращаем результаты поиска
        return f"Рекомендуемые курсы по запросу: {', '.join(recommended_courses)}."


if __name__ == "__main__":
    query = "Как изучать машинное обучение?"
    answer = process_user_query(query)
    print(answer)
