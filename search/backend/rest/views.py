from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest.models import HospitalDoctor
from rest.models import HospitalScholar
from django.db.models import Q # 복수의 검색어로 search시 Q 객체 필수로 필요!
from django.shortcuts import get_object_or_404
from . import models,serializers

# Create your views here.
# 예시 api
@api_view(["GET","POST"])
def test(request):
    if request.method=="GET":
        return Response({"data":123})
    elif request.method=="POST":
        return Response({"data":123})
# 
class SearchAPI(APIView):
    def get(self,request):
        # 검색어 넘겨받기. rest의 url 형태 보기
        # name = request.GET.get('doctor_name')
        # hospital = request.GET.get('hospital')
        # major = request.GET.get('major')
        # disease = request.GET.get('disease')

        # 예시 검색
        name = "김"
        hospital = "삼성"
        major = "심장"
        disease=""

        # 만약 검색어가 존재하지 않는다면, 전체 set 보내주기
        if((name==None)&(hospital==None)&(major==None)&(disease==None)):
            queryset=HospitalDoctor.objects.all()
            serializer_class=serializers.DoctorSerializer(queryset, many=True)
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        else:
            # 만약 검색어가 존재한다면, 조건에 만족하는 것만 보내주기.
            queryset = HospitalDoctor.objects.filter(
                # name을 포함하거나, belong을 포함하거나, major을 포함하는 정보들 모두 출력
                # 단점: 다만, 더 정확하게 일치하는 데이터에 대해서는 차등적으로 출력. 
                Q(name__contains=name) & Q(belong__contains=hospital)& Q(major__contains=major)
            )
            # 이름, 병원(이름과 병원은 간단) major 검색은 어떻게 진행??
            serializer_class=serializers.DoctorSerializer(queryset, many=True)
            return Response(serializer_class.data, status=status.HTTP_200_OK)

