# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# 				4XX 			 	#
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#


# ------# 400 #------#


def missing_query_parameter(query_name: str):
    return {
        "code": "MISSING_QUERY_PARAMETER",
        "message": "Missing mandatory query parameter '" + query_name + "'",
    }


def missing_field(field: str):
    return {
        "code": "MISSING_FIELD",
        "message": "Missing mandatory field '" + field + "'",
    }


def missing_path_parameter(field: str):
    return {
        "code": "MISSING_PATH_PARAMETER",
        "message": "Missing mandatory path parameter '" + field + "'",
    }


def missing_body():
    return {
        "code": "MISSING_BODY",
        "message": "Missing mandatory body",
    }


def missing_path_parameter(field: str):
    return {
        "code": "INVALID_BODY",
        "message": "Invalid body attribute '" + field + "'",
    }


def invalid_field(field_name: str, field_value: str, error_description: str):
    message = "Invalid value '{field_value}' for field '{field_name}'".format(
        field_value=field_value, field_name=field_name
    )
    if error_description is not None:
        message += f": {error_description}"
    return {"code": "INVALID_FIELD", "message": message}


# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# 				5XX 			 	#
# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#


# ------# 500 #------#
def server_error():
    return {
        "code": "INTERNAL_SERVER_ERROR",
        "message": "Internal server error",
    }
