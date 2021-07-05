@api_view(['GET','POST'])
def complete_slots_validator(request):
    if request.method == 'GET':
        return Response({"message": "Your slot validator"})

    data=request.data
    try:
        t=in_slot_validator(data)
    except:
        error ="Bad request!!"
        traceback.print_exc()
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    response = Response(t, status=status.HTTP_200_OK)
    return response