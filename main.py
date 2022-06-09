from flask import Flask
from utils import load_candidtates

candidates_data = load_candidtates()

app = Flask(__name__)

@app.route("/")
def print_candidates_main():
    print_candidates_string = ""
    for person in candidates_data:
        candidate_string = str(person['name']) + " " + str(person['position']) + " " + str(person['skills'] + " ")
        print_candidates_string += candidate_string     #у меня не получается вставить \n в текст
    return print_candidates_string


@app.route("/candidates/<int:cand_id>") #не получается использовать <int:cand_id>
def print_candidates_uid(cand_id):
    print_candidates_string = ""
    for person in candidates_data:
        if int(person[id]) == cand_id:
            candidate_string = str(person['picture']) + " " + str(person['name']) + " " + str(person['position']) + " " + str(person['skills'] + " ")
            print_candidates_string += candidate_string
        else:
            pass
    return print_candidates_string


@app.route("/skills/<cand_skill>")  # не получается использовать <cand_skill>
def print_candidates_skill(cand_skill):
    print_candidates_string = ""
    for person in candidates_data:
        if cand_skill in person['skills']:
            candidate_string = str(person['name']) + " " + str(person['position']) + " " + str(person['skills'] + " ")
            print_candidates_string += candidate_string
        else:
            pass
    return print_candidates_string

/skills/<x>


@app.route("/feed/")
def test_print():
    return f"{candidates_data}"

app.run()
