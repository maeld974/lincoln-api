from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
with open(os.path.join("static", "data2.json")) as json_file:
    data = json.load(json_file)


candidates_list = {
"candidates": [
{
		"id_candidat" : "46135",
		"civilite": "Mr.",
		"nom": "MARTIN",
		"prenom": "Eric",
		"ville": "CELON",
		"previous_job": "BTP11 Sales Engineer|CONSTRUCTION/~EX03 Deputy Managing Director|EXECUTIF/~EX02 CEO SME|EXECUTIF/~IMM081 Development Director|IMM08 Property transaction//~SSM0211 Managing Director",
		"salary": 0,
		"linkedin":""
	},
	{
		"id_candidat" : "110696",
		"civilite": "Mr.",
		"nom": "REINACHTER",
		"prenom": "Jean-Baptiste",
		"ville": "PARIS",
		"previous_job" : "Chef de produit Tronçonneuses - Débroussailleuses - Taille-Haies - Souffleurs pour les marques Husqvarna et Jonsered",
		"salary": 0,
		"linkedin": ""
	},
	{
		"id_candidat" : "162642",
		"civilite": "Mr.",
		"nom": "TOULIS",
		"prenom": "Vincent",
		"ville": "",
		"previous_job": "",
		"salary": 0,
		"linkedin": ""
	},
	{
		"id_candidat" : "974694",
		"civilite": "Mr.",
		"nom": "WEISS",
		"prenom": "Lionel",
		"ville": "Evian-les-Bains,FI08 Business Controller|FINANCIAL SERVICES/~CORPORATE FINANCE|",
		"previous_job":"",
		"salary": 0,
		"linkedin": ""
	},
	{
		"id_candidat" : "1013739",
		"civilite": "Mr.",
		"nom": "DRUGMAN",
		"prenom": "John",
		"ville": "",
		"previous_job": "CS041 Training Consultant|CS04 Human Resources Consultancy//~CS041 Training Consultant|CS04 Human Resources Consultancy//",
		"salary": 0,
		"linkedin": ""
	},
	{
		"id_candidat" : "1047286",
		"civilite": "Mrs.",
		"nom": "BYRON",
		"prenom": "Isabelle",
		"ville": "",
		"previous_job": "SALES|",
		"salary": 0,
		"linkedin":""
	},
	{
		"id_candidat" : "1092260",
		"civilite": "Mr.",
		"nom": "GUENIFFEY",
		"prenom": "Thierry",
		"ville": "BRIMEUX",
		"previous_job": "IND21 Industrialization Manager/Engineer|INDUSTRY/~IND17 Maintenance Engineer/Manager|INDUSTRY/~IND02 Production Manager/Director|INDUSTRY/",
		"salary":0,
		"linkedin":""
	},
	{
		"id_candidat" : "1108933",
		"civilite": "Mrs.",
		"nom": "VITREY",
		"prenom": "Cécile",
		"ville": "Köln",
		"previous_job": "DI0111 Web Merchandiser|DI01 Marketing//~RESPONSBALE MARKETING",
		"salary": 0,
		"linkedin":""
	},
	{
		"id_candidat" : "1156041",
		"civilite": "Mr.",
		"nom": "TOURNIER",
		"prenom": "Matthieu",
		"ville": "PARIS",
		"previous_job": "Directeur Juridique Conformité Risques",
		"salary": 0,
		"linkedin": ""
	},
	{
		"id_candidat" : "1166550",
		"civilite": "Mrs.",
		"nom": "DA SILVA",
		"prenom": "Corinne",
		"ville": "Joinville le Pont",
		"previous_job": "Marketing - Communication",
		"salary": 0,
		"linkedin": ""
	},
	{
		"id_candidat" : "1175411",
		"civilite": "Mr.",
		"nom": "GUIDOUX",
		"prenom": "Franck",
		"ville": "Toulouse",
		"previous_job": "MARKETING~M053 Marketing Manager",
		"salary": 0,
		"linkedin": ""
	},
	{
		"id_candidat" : "1186731",
		"civilite": "Mrs.",
		"nom": "VAN EEKERT",
		"prenom": "Lucille",
		"ville": "Paris",
		"previous_job": "MARKETING|",
		"salary": 0,
		"linkedin": ""
	},
	{
		"id_candidat" : "1222760",
		"civilite": "Mr.",
		"nom": "MARIE",
		"prenom": "Arnaud",
		"ville": "",
		"previous_job": "Directeur Développement, Directeur Commercial",
		"salary": 0,
		"linkedin": ""
	},
	{
		"id_candidat" : "1275471",
		"civilite": "Mr.",
		"nom": "MONCHAMPS",
		"prenom": "Sébastien",
		"ville": "",
		"previous_job":"INFORMATION SYSTEM|",
		"salary":62000,
		"linkedin":""
	},
	{
		"id_candidat" : "1306893",
		"civilite": "",
		"nom": "PATRICK",
		"prenom": "Faugerolas",
		"ville": "",
		"previous_job": "REAL ESTATE|~HEALTHCARE|",
		"salary": 0,
		"linkedin": "https://www.linkedin.com/in/faugerolas-patrick-3048a253"
	},
	{
		"id_candidat" : "1310463",
		"civilite": "Mr.",
		"nom": "NORCA",
		"prenom": "Steeve",
		"ville": "",
		"previous_job" : "Management Commercial", 
		"salary":0,
		"linkedin":""
	},
	{
		"id_candidat" : "1324676",
		"civilite": "",
		"nom" : "VAN HOOL",
		"prenom": "Marie",
		"ville": "",
		"previous_job":"MARKETING|~M03 Brand Marketing|MARKETING/",
		"salary":0,
		"linkedin": "https://www.linkedin.com/in/marie-van-hool"
	},
	{
		"id_candidat" : "1331220",
		"civilite": "Mr.",
		"nom": "COLONIA",
		"prenom": "Olivier",
		"ville": "",
		"previous_job": "REAL ESTATE|",
		"salary":0,
		"linkedin":"https://www.linkedin.com/in/oliviercolonia"
	},
	{
		"id_candidat" : "1346932",
		"civilite": "Mr.",
		"nom": "JEAN PAUL FOURDRAINE",
		"prenom": "Frédéric",
		"ville": "",
		"previous_job": "SAFETY/SECURITY/GENERAL RESOURCES|",
		"salary":0,
		"linkedin": "https://www.linkedin.com/in/fr%C3%A9d%C3%A9ric-jean-paul-fourdraine-a353958a"
	},
	{
		"id_candidat" : "1350082",
		"civilite": "Mrs.",
		"nom": "DEFOSSEZ",
		"prenom": "Anne sophie",
		"ville": "",
		"previous_job":"HEALTHCARE|",
		"salary":0,
		"linkedin": "https://www.linkedin.com/in/anne-sophie-defossez-a448aa69"
	}
]
}


@app.route('/missions/list', methods=['GET', 'POST', 'OPTIONS'])
def list_missions():
    id_consultant = request.args.get('id_consultant')
    if id_consultant:
        missions_list=[]
        for mission in data["missions"]:
            if str(mission["id_consultant"]) == str(id_consultant):
                missions_list.append(mission)
        if missions_list:
            response = jsonify({
                "success": True,
                "missions": missions_list,
                "message": f"List of mission for id_consultant = {id_consultant} successfuly returned"
            })
        else:
            response = jsonify({
                "success": False,
                "missions": None,
                "message": f"No mission found for id_consultant = {id_consultant}"
            })
    else:
        response = jsonify({
                "success": True,
                "missions": data["missions"],
                "message": "List of all missions successfuly returned"
            })
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    return response


@app.route('/candidates', methods=['GET', 'POST', 'OPTIONS'])
def get_candidates():
    id_mission = request.args.get('id_mission')
    if id_mission:
        if id_mission == "19129":
            response = jsonify({
                "success": True,
                "id_mission": "19129",
                "candidates": candidates_list["candidates"],
                "message": f"List of candidates for id_mission = {id_mission} successfuly returned"
            })
        else:
            response = jsonify({
                "success": False,
                "id_mission": None,
                "candidates": None,
                "message": f"No mission found for id_mission = {id_mission}"
            })
    else:
        response = jsonify({
                "success": False,
                "id_mission": None,
                "candidates": None,
                "message": f"Please indicate an id_mission"
            })
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    return response


if __name__ == '__main__':
    app.run()
