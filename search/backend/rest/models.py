from django.db import models

# Create your models here.
class Hospital(models.Model):
    hos_id = models.IntegerField(primary_key=True)
    hos_kname = models.TextField()
    hos_ename = models.TextField()

    class Meta:
        managed = False
        db_table = 'hospital'


class HospitalDoctor(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True,db_column='name')
    belong = models.CharField(max_length=20, blank=True, null=True,db_column='belong')
    major = models.TextField(blank=True, null=True,db_column='major')
    education = models.TextField(blank=True, null=True,db_column='education')
    career = models.TextField(blank=True, null=True,db_column='career')
    link = models.TextField(blank=True, null=True,db_column='link')
    hos_id = models.CharField(max_length=6,db_column='hos_id')
    doctor_id = models.CharField(max_length=10, primary_key=True,db_column='doctor_id') # doctor model의 primary_key

    class Meta:
        managed = False
        db_table = 'hospital_doctor'


class HospitalScholar(models.Model):
    id = models.IntegerField(primary_key=True,db_column='id')
    # id=models.AutoField(primary_key=True) # django model은 무조건 pk 필요. 자동 생성.
    name = models.TextField(db_collation='utf8mb4_0900_ai_ci', blank=True, null=True,db_column='name')
    belong = models.TextField(db_collation='utf8mb4_0900_ai_ci', blank=True, null=True,db_column='belong')
    pname = models.TextField(db_collation='utf8mb4_0900_ai_ci', blank=True, null=True,db_column='pname')
    jname = models.TextField(db_collation='utf8mb4_0900_ai_ci', blank=True, null=True,db_column='jname')
    jindex = models.TextField(db_collation='utf8mb4_0900_ai_ci', blank=True, null=True,db_column='jindex')
    year = models.TextField(db_collation='utf8mb4_0900_ai_ci', blank=True, null=True,db_column='year')
    citation = models.TextField(db_collation='utf8mb4_0900_ai_ci', blank=True, null=True,db_column='citation')
    coworker = models.TextField(db_collation='utf8mb4_0900_ai_ci', blank=True, null=True,db_column='coworker')
    hos_id = models.CharField(max_length=6, db_collation='utf8mb4_0900_ai_ci',db_column='hos_id')
    # hospital_doctor과 외래키로 join. manytoone relationships이고 hospitaldoctor의 외래키를 불러올 시
    # 자동으로 hospital_doctor의 pk와 연결된다. 그때, scholar의 doctor_id와 외래키를 join시킬것임을 따로 명시해줬다.
    doctor_id=models.ForeignKey("HospitalDoctor",related_name="scholar",on_delete=models.CASCADE,db_column="doctor_id")
    # related name: doctor와 연결될 scholar 이름 지정.

    class Meta:
        managed = False
        db_table = 'hospital_scholar'

# 최종 결과물: name, belong, major, education, career, link, hospital_scholar


