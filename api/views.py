from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    person = {'slackUsername': 'ayomisco', 'backend':True, 'age': 23, 'bio':"I'm a tech lover."}
    return Response(person)