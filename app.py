from flask import Flask, request
import json
import os

app = Flask(__name__)
with open(os.path.join("static", "data.json")) as json_file:
    data = json.load(json_file)


candidates_list = {
"candidates": [
    {
      "id_candidat": "177",
      "civilite": "M.",
      "nom": "MAGNIEN",
      "prenom": "Cyril",
      "ville": "Villiers sur Loir",
      "previous_job": "LEGAL|",
      "salary": 145000,
      "linkedin": "https://www.linkedin.com/in/cmagnien"
    },
    {
      "id_candidat": "178",
      "civilite": "Mme.",
      "nom": "BLENIAT",
      "prenom": "Christelle",
      "ville": "RUEIL MALMAISON",
      "previous_job": "SUPPORT/HELP DESK|~DIRECTEUR ADMINISTRAIF ET FINANCIER - DIRECTION DE PROJET IT",
      "salary": None,
      "linkedin": "https://www.linkedin.com/in/christelle-bleniat-36b91619"
    },
    {
      "id_candidat": "179",
      "civilite": "Mrs.",
      "nom": "NEUPLANCHE",
      "prenom": "Laure",
      "ville": "Paris",
      "previous_job": "FI13 External Auditor other firms",
      "salary": None,
      "linkedin": None
    },
    {
      "id_candidat": "180",
      "civilite": "Mr.",
      "nom": "OUNE-BIVE",
      "prenom": "Renaud",
      "ville": "Paris",
      "previous_job": "B22 Exploitation Banque Commercial",
      "salary": None,
      "linkedin": None
    }]
}


@app.route('/missions/list')
def list_missions():
    id_consultant = request.args.get('id_consultant')
    if id_consultant:
        missions_list=[]
        for mission in data["missions"]:
            if str(mission["id_consultant"]) == str(id_consultant):
                missions_list.append(mission)
        if missions_list:
            response = {
                "success": True,
                "missions": missions_list,
                "message": f"List of mission for id_consultant = {id_consultant} successfuly returned"
            }
        else:
            response = {
                "success": False,
                "missions": None,
                "message": f"No mission found for id_consultant = {id_consultant}"
            }
    else:
        response = {
                "success": True,
                "missions": data["missions"],
                "message": "List of all missions successfuly returned"
            }
    return response


@app.route('/candidates', methods=['GET', 'POST'])
def get_candidates():
    id_mission = request.args.get('id_mission')
    if id_mission:
        if id_mission == "10000":
            response = {
                "success": True,
                "id_mission": "10000",
                "candidates": candidates_list["candidates"],
                "message": f"List of candidates for id_mission = {id_mission} successfuly returned"
            }
            return response
        else:
            response = {
                "success": False,
                "id_mission": None,
                "candidates": None,
                "message": f"No mission found for id_mission = {id_mission}"
            }
            return response
    else:
        response = {
                "success": False,
                "id_mission": None,
                "candidates": None,
                "message": f"Please indicate an id_mission"
            }
        return response


if __name__ == '__main__':
    app.run()
