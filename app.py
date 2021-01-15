from flask import Flask, request
import json
import os

app = Flask(__name__)
with open(os.path.join("static", "data.json")) as json_file:
    data = json.load(json_file)


@app.route('/')
def index():
    return data


@app.route('/hello')
def hello_world():
    return "Hello world !"


@app.route('/job/list')
def list_job():
    response = {
        "code" : 200,
        "missions" : []
    }
    for mission in data["missions_list"]:
        response["missions"].append({"mission_title": mission["mission_title"], "information": mission["information"]})
    return response


@app.route('/candidates', methods=['GET', 'POST'])
def get_candidates():
    id_mission = request.args.get('id_mission')
    if id_mission:
        for mission in data["missions_list"]:
            if mission['id_mission'] == id_mission:
                response = {
                    "code": 200,
                    "candidates": mission["candidate_list"]
                }
                return response
        return f"No mission found for id_mission = {id_mission}"
    else:
        return "Please provide an id_mission"


if __name__ == '__main__':
    app.run()
