from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import traceback

from Intentvalidation.ValidationLogic.logic import *

@api_view(['GET'])
def welcome(request):
    result="Hey Welcome !!"
    response=Response(result,status=status.HTTP_200_OK)
    return response

@api_view(['GET', 'POST'])
def validate_finite_values_entity(request):
    if request.method == 'GET':
        return Response({"message": "This is where validate_finite_values_entity api is hosted!"})

    data = request.data
    try:
        val= validate_finite_wrapper(data)
    except:
        error = "Bad Request made due to one or more of the following reasons" \
                "\n 1) Required keys are missing from the " \
                "2) payload "
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    response = Response(val, status=status.HTTP_200_OK)
    return response


@api_view(['GET', 'POST'])
def validate_numeric_entity(request):
    if request.method == 'GET':
        return Response({"message": "This is where validate_numeric_entity api is hosted!"})
    data = request.data
    try:
        val= validate_numeric_wrapper(data)
    except:
        error = "Bad Request made due to one or more of the following reasons:" \
                "\nRequired keys are missing from the " \
                "payload" \
                "\nData type is incorrect" \
                "\nConstraint provided is not a valid boolean expression"
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    response = Response(val, status=status.HTTP_200_OK)
    return response

