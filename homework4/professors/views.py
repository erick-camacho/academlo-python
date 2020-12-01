from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Professor
from .serializers import ProfessorSerializer


# ------ CLASS BASED VIEWS ------



# ------ FUNCTION BASED VIEWS ------

@api_view(['GET', 'POST'])
def professor_list(request, format=None):
    if request.method == 'GET':
        professors = Professor.objects.all()
        serializer = ProfessorSerializer(professors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def professor_detail(request, pk, format=None):
    try:
        professor = Professor.objects.get(pk=pk)
    except Professor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfessorSerializer(professor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProfessorSerializer(professor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        professor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
