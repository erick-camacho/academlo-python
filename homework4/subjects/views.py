from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Subject
from .serializers import SubjectSerializer


# ------ CLASS BASED VIEWS ------



# ------ FUNCTION BASED VIEWS ------

@api_view(['GET', 'POST'])
def subject_list(request, format=None):
    if request.method == 'GET':
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def subject_detail(request, pk, format=None):
    try:
        subject = Subject.objects.get(pk=pk)
    except Subject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
