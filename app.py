from flask import Flask, request, jsonify
from parser import *
from blob_connection import *
import json
import os
import requests


app = Flask(__name__)


def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    return response


@app.route('/missions/list')
def list_mission():
    id_consultant = request.args.get('id_consultant')
    if id_consultant:
        response = mission_csv_to_dict_list(id_consultant)
    else:
        response = mission_csv_to_dict_list_all()
    return add_headers(jsonify(response))


@app.route('/refresh_csv')
def refresh():
    id_mission = request.args.get('id_mission')
    if id_mission:
        response = jsonify(refresh_csv(id_mission))
    else :
        response = jsonify({
            "success" : False,
            "message" : f"Please provide an id_mission"
        })
    return add_headers(response)


@app.route('/candidates/list')
def list_candidates():
    id_mission = request.args.get('id_mission')
    if id_mission:
        logger.info("There is an id_mission")
        if os.path.exists(os.path.join("static", "mission_candidates",f"mission_{id_mission}_person_score.csv")):
            logger.info("There is a file matching")
            response = jsonify(candidate_csv_to_dict_list(id_mission))
        else:
            logger.info("There no a file matching")
            refresh = refresh_csv(id_mission)
            logger.info("Refreshing the CSV")
            if refresh['success']:
                logger.info("Refresh successful")
                response = jsonify(candidate_csv_to_dict_list(id_mission))
                logger.info("Returning CSV")
            else:
                logger.info("Refresh unsuccessful")
                response = jsonify(refresh)
    else:
        logger.info("There is no id_mission")
        response = jsonify({
            "success" : False,
            "message" : f"Please provide an id_mission",
            "candidate_list": []
        })
    return add_headers(response)


if __name__ == '__main__':
	app.run()
