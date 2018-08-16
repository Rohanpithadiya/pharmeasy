from flask import Flask
from flask import Response, request
from flask_api import status

from utils.config import config
from utils.logger import serviceLogger as logging
from routes import request_documents, prescriptions, grant_requests, documents

app = Flask(__name__)


@app.route('/requests/<requester_id>', methods=['POST'])
def create_requests(requester_id):
    try:
        logging.info("received request for document permission")
        patient_id = request.form["patient_id"]
        req_type = request.form["req_type"]
        doc_type = request.form["doc_type"]
        return request_documents.post(requester_id = requester_id,
                               patient_id = patient_id,
                               req_type = req_type,
                               doc_type = doc_type)
    except BaseException as bex:
        logging.error(bex.message)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.route('/requests/<patient_id>', methods=['GET'])
def all_requests(patient_id):
    try:
        logging.info("received request from patients for all pending requests")
        return request_documents.get(patient_id=patient_id)
    except BaseException as bex:
        logging.error(bex.message)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.route('/prescriptions/<patient_id>', methods=['GET'])
def get_all_prescriptions(patient_id):
    try:
        logging.info("received request from patients for all prescriptions")
        return prescriptions.get(patient_id=patient_id)
    except BaseException as bex:
        logging.error(bex.message)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.route('/grants/<patient_id>', methods=['POST'])
def grant_permissions(patient_id):
    try:
        logging.info("grant permission to requestee by patient")
        requester_id = request.form["requester_id"]
        prescription_id = request.form["prescription_id"]
        req_type = request.form["req_type"]
        doc_type = request.form["doc_type"]
        return grant_requests.post(requester_id = requester_id,
                               patient_id = patient_id,
                               prescription_id=prescription_id,
                               req_type = req_type,
                               doc_type = doc_type)
    except BaseException as bex:
        logging.error(bex.message)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.route('/remove_grants/<patient_id>', methods=['POST'])
def remove_grant_permissions(patient_id):
    try:
        logging.info("remove grant permission to requestee by patient")
        requester_id = request.form["requester_id"]
        prescription_id = request.form["prescription_id"]
        req_type = request.form["req_type"]
        return grant_requests.remove_permission(requester_id = requester_id,
                               patient_id = patient_id,
                               prescription_id=prescription_id,
                               req_type = req_type)
    except BaseException as bex:
        logging.error(bex.message)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.route('/grants/<patient_id>', methods=['DELETE'])
def reject_permissions(patient_id):
    try:
        logging.info("grant permission to requestee by patient")
        requester_id = request.form["requester_id"]
        req_type = request.form["req_type"]
        doc_type = request.form["doc_type"]
        return grant_requests.delete(requester_id = requester_id,
                               patient_id = patient_id,
                               req_type = req_type,
                               doc_type = doc_type)
    except BaseException as bex:
        logging.error(bex.message)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.route('/documents/<requester_id>', methods=['GET'])
def get_prescription_for_patient(requester_id):
    try:
        logging.info("received request from doctor for prescriptions of patient")
        patient_id = request.args.get("patient_id")
        req_type = request.args.get("req_type")
        return documents.get(requester_id =requester_id, patient_id=patient_id,req_type = req_type)
    except BaseException as bex:
        logging.error(bex.message)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.route('/meta/<prescription_id>', methods=['GET'])
def get_prescription_details(prescription_id):
    try:
        requester_id = request.args.get("requester_id")
        logging.info("received request from doctor for details prescription")
        return prescriptions.get_detail(prescription_id= prescription_id,requester_id=requester_id)
    except BaseException as bex:
        logging.error(bex.message)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


if __name__ == '__main__':
    app.run(host = config["server"]["host"],
            port = config["server"]["port"])