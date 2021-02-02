import os
import csv
from config import MAX_CANDIDATES


def candidate_csv_to_dict_list(id_mission):
    file_name = f"mission_{id_mission}_person_score.csv"
    candidate_list = []
    try :
        with open(os.path.join("static", "mission_candidates", file_name)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            next(csv_reader, None)
            index = 0
            for row in csv_reader:
                candidate = {
                    "id_personne":row[0],
                    "id_societe":row[1],
                    "nom": row[2],
                    "prenom": row[3],
                    "ville": row[4],
                    "secteur": row[5],
                    "raison_sociale": row[6],
                    "intitule_poste": row[7],
                    "salaire": row[8],
                    "linkedin": row[9],
                    "coache": row[10],
                    "rank": row[11]
                }
                candidate_list.append(candidate)
                index += 1
                if index == MAX_CANDIDATES: # There's gotta be a better way.
                    break
            response = {'success' : True, 'message': f"CSV {file_name} succesfully parsed into candidate list", 'candidate_list': candidate_list}
    except FileNotFoundError:
        response = {'success' : False, 'message': f"No file found for {file_name}", 'candidate_list': candidate_list}
    return response


def mission_csv_to_dict_list(id_consultant):
    file_name = "consultant_mission_info.csv"
    mission_list = []
    try :
        with open(os.path.join("static", file_name)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            next(csv_reader, None)
            for row in csv_reader:
                if row[0] == id_consultant:
                    mission = {
                        "nom": row[1],
                        "prenom": row[2],
                        "id_mission": row[3],
                        "ref_interne": row[4],
                        "libelle": row[5],
                        "raison_sociale": row[6],
                        "salaire_min": row[7],
                        "salaire_max": row[8]
                    }
                    mission_list.append(mission)
            response = {'success' : True, 'message': f"CSV {file_name} succesfully parsed into mission list filtered with id_consultant = {id_consultant}", 'mission_list': mission_list}
    except FileNotFoundError:
        response = {'success' : False, 'message': f"No file found for {file_name}", 'mission_list': mission_list}
    return response


def mission_csv_to_dict_list_all():
    file_name = "consultant_mission_info.csv"
    mission_list = []
    try :
        with open(os.path.join("static", file_name)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            next(csv_reader, None)
            for row in csv_reader:
                mission = {
                    "nom": row[1],
                    "prenom": row[2],
                    "id_mission": row[3],
                    "ref_interne": row[4],
                    "libelle": row[5],
                    "raison_sociale": row[6],
                    "salaire_min": row[7],
                    "salaire_max": row[8]
                }
                mission_list.append(mission)
            response = {'success' : True, 'message': f"CSV {file_name} succesfully parsed into mission list", 'mission_list': mission_list}
    except FileNotFoundError:
        response = {'success' : False, 'message': f"No file found for {file_name}", 'mission_list': mission_list}
    return response