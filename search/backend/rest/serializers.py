# serializers는 models의 column값중 어떤 값을 전달하고 싶은지
# 우선 나는 다 전달할 생각이당
from rest_framework import serializers
from rest.models import HospitalScholar
from rest.models import HospitalDoctor

class ScholarSerializer(serializers.ModelSerializer):
    class Meta:
        model=HospitalScholar
        fields=("pname","jname","jindex","citation","year")

class DoctorSerializer(serializers.ModelSerializer):
    # 요렇게 하면 자동으로 해당 doctor의 scholar 정보들이 리스트로 들어간다.
    scholar=ScholarSerializer(many=True,read_only=True)
    class Meta:
        model=HospitalDoctor
        fields=("name","belong","major","education","career","link","hos_id","scholar")