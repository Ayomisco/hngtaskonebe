from http.client import responses
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def getData(request):
    person = {'slackUsername': 'ayomisco', 'backend':True, 'age': 23, 'bio':"I'm a tech lover."}
    return Response(person)


@api_view(['POST'])
def addData(request):
        # serializer = ArithemeticSerializer(data=request.data)
        # if serializer.is_valid():
        #     # serializer.save()
        # return Response(serializer.data)
        x = int(request.data["x"])
        y = int(request.data["y"])
        operation_type = request.data["operation_type"]

        if operation_type in ['addition','add','+','subtraction','minus','subtract','-','multiply','x','*','multiplication']:
            if operation_type == 'addition' or operation_type == 'add' or operation_type == '+': 
                result = int(x) + int(y)
            if operation_type == 'subtraction' or operation_type == 'minus' or operation_type == 'subtract' or operation_type == 'subtract': 
                result = int(x) - int(y)
            if operation_type == 'multiply' or operation_type == 'x' or operation_type == 'multiplication' or operation_type == '*': 
                result = int(x) * int(y)

            user_response = {
                'slackUsername': 'ayomisco',
                'result': result,
                'operation_type':operation_type,
            }

            return Response(user_response, status.HTTP_200_OK)
        else:
            content= {"Invalid operation. I don't catch what '{}' means.".format(operation_type)}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)