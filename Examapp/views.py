from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Examapp.models import QuestionsDb
from OnlineExaminationSystem.serializer import QuestionSerializer


# Create your views here.
class QustionListCreateView(APIView):
    def get(self,request):
        qs=QuestionsDb.objects.all()
        serializer_instance=QuestionSerializer(qs,many=True)
        return Response(data=serializer_instance.data)
    def post(self,request):
        form_data=request.data
        serializer_instance=QuestionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            QuestionsDb.objects.create(**actual_data)
            return Response(data={"message":"duestion addded success"})
        else:
            return Response(data={"message":serializer_instance.errors})
class QestionRetriveUpdateDelete(APIView):
    def get(self,request,pk):
        qs=QuestionsDb.objects.get(id=pk)
        serializer_instance=QuestionSerializer(qs)
        return Response(data=serializer_instance.data)
    def put(self,request,pk):
        form_data=request.data
        serializer_instance=QuestionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual__data=serializer_instance.validated_data
            QuestionsDb.objects.filter(id=pk).update(**actual__data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
    def delete(self,request,pk):
        QuestionsDb.objects.filter(id=pk).delete()
        return Response({"messege":"dustion deleted   ..."})