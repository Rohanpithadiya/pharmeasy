import json

from flask_api import status
from flask import Response
import utils.constants as cn
from database.permissions_requests import permissions_requests
from database.permissions import permissions


def post(requester_id, patient_id, prescription_id, req_type, doc_type):
    if (req_type in [cn.DOCTOR, cn.PHARMA]) and \
            (doc_type in [cn.MR, cn.PRESCRIPTION]):
        if doc_type == cn.PRESCRIPTION:
            permissions().grant_request(requester_id = requester_id,
                                   patient_id = patient_id,
                                   prescription_id=prescription_id,
                                   req_type = req_type)
        else:
            pass # insert logic for medical records
        # permission_requests().remove_requests(requester_id=requester_id,
        #                                       patient_id=patient_id,
        #                                       req_type=req_type,
        #                                       doc_type=doc_type)
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

def delete(requester_id,patient_id,req_type, doc_type):
    permissions_requests().remove_requests(requester_id = requester_id,
                                           patient_id = patient_id,
                                           req_type = req_type,
                                           doc_type = doc_type)
    return Response(status=status.HTTP_201_CREATED)


def remove_permission(patient_id,requester_id,prescription_id ,req_type):
    permissions().remove_permission(requester_id=requester_id,
                                    patient_id=patient_id,
                                    prescription_id=prescription_id,
                                    req_type=req_type)

    return Response(status=status.HTTP_201_CREATED)
