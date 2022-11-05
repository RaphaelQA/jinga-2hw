import json


def load_candidates_from_json(path):
    with open(path, "r", encoding='utf-8') as file:
        data = json.load(file)

    return data


def get_candidate(candidate_id, file):
    for candidate in file:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name, file):
    result = []
    for candidate in file:
        if candidate_name in candidate['name']:
            result.append(candidate)
    return result



def get_candidates_by_skill(skill_name, file):
    lower_skill = skill_name.lower()
    candidates = []
    for candidate in file:
        if lower_skill in candidate["skills"].lower().split(", "):
            candidates.append(candidate)
    return candidates
