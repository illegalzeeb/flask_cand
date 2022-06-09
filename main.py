from flask import Flask
from utils import load_candidtates



app = Flask(__name__)

@app.route("/")
def print_candidates_main():
    candidates_data = load_candidtates()
    candidate_string = "<pre>"
    for person in candidates_data:
        candidate_string += f"""
        {person['name']}\n
        {person['position']}\n
        {person['skills']}\n
        """
    candidate_string += "</pre>"
    return candidate_string


@app.route("/candidates/<int:cand_id>")
def print_candidates_uid(cand_id):
    candidates_data = load_candidtates()
    candidate_string = "<pre>"
    for person in candidates_data:
        if int(person['id']) == int(cand_id):
            candidate_string += f"""
            <img src="{person['picture']}">\n
            {person['name']}\n
            {person['position']}\n
            {person['skills']}\n
            """
            candidate_string += "</pre>"
        else:
            pass
    return candidate_string


@app.route("/skills/<cand_skill>")
def print_candidates_skill(cand_skill):
    candidates_data = load_candidtates()
    candidate_string = "<pre>"
    for person in candidates_data:
        if cand_skill in person['skills'].lower().split(", "):
            candidate_string += f"""
            {person['name']}\n
            {person['position']}\n
            {person['skills']}\n
            """
        else:
            pass
    candidate_string += "</pre>"
    return candidate_string

app.run()
