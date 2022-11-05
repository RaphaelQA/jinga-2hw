from flask import Flask, render_template

from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

path = "candidates.json"

file = load_candidates_from_json(path)

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('list.html', candidates=file)

@app.route('/candidate/<int:id>')
def candidate_page(id):
    candidate = get_candidate(id, file)
    if not candidate:
        return "Такого кандидата нет"
    return render_template('card.html', candidate=candidate)

@app.route('/search/<candidate_name>')
def candidate_by_name_page(candidate_name):
    candidates = get_candidates_by_name(candidate_name, file)
    return render_template('search.html', candidates=candidates)

@app.route('/skill/<skill_name>')
def candidate_by_skill_page(skill_name):
    candidates = get_candidates_by_skill(skill_name, file)
    return render_template('skill.html', skill=skill_name, candidates=candidates)

app.run()
