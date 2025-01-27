import pytest
from unittest.mock import patch


# Тестируем функцию process_user_query
def test_process_user_query():
    query = "Какие курсы по аналитике существуют?"

    # Мокаем LLM API, чтобы избежать реальных запросов
    with patch('openai.Completion.create') as mock_openai:
        mock_openai.return_value = {
            'choices': [{'text': 'Рекомендуем курсы: Аналитика данных, Сложная аналитика'}]
        }
        response = process_user_query(query)
        assert "Рекомендуем курсы" in response
