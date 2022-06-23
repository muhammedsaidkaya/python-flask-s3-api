from flask import json, Response, Blueprint, request
from . import conn


s3_api = Blueprint('s3', __name__)

@s3_api.route('content/<bucket_uuid>', methods=['GET'])
def get_all(bucket_uuid: str) -> Response:
    return custom_response(conn.list_objects(Bucket=bucket_uuid)['Contents'], 200)

@s3_api.route('content/<bucket_uuid>/<object_uuid>', methods=['GET'])
def get_by_id(bucket_uuid: str, object_uuid: str) -> Response:
    try:
        x = conn.get_object(Bucket=bucket_uuid, Key=object_uuid)
        #FIX
        return custom_response({"data": x['Body'].read() }, 200)
    except:
        return custom_response({"data": None }, 404)




def custom_response(response_body: dict, status_code: int) -> Response:
    """
    Wrapper function creating a response with common parameters

    Parameters:
        response_body: the response body
        status_code: the status code of the response

    Returns:
        The Response object that Flask can return
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(response_body),
        status=status_code
    )
