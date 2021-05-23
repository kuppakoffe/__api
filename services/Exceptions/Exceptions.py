from flask_restful import HTTPException, http_status_message



class APIExceptions:
    pass


api_exceptions = {
    404: {
        "error": http_status_message(404),
        "message": "resource requested is not found",
        "status_code": 404
    }
}