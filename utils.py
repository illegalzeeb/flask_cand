import json

def load_candidtates() -> list[dict]:
    """
    Читает файл candidates.json, возвращает как список словарей candidates_data
    """
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates_data = json.load(file)
    return candidates_data