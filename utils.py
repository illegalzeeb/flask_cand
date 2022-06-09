import json

def load_candidtates():
    """
    Читает файл candidates.json, возвращает как список словарей candidates_data
    """
    with open("candidates.json") as file:
        candidates_data = json.loads(file.read())
    return candidates_data