from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
import csv





def insert_bank(self):
    with open('C:\\Users\\ajitm\\OneDrive\\Desktop\\Ajit\\DE2\\ajit\\Scripts\\CSV_DATA_to_DATABASE\\app\\bank.csv','r') as FO:
        IOD=csv.reader(FO)
        for i in IOD:
            BN=i[0].strip()
            BO=Bank(bank_name=BN)
            BO.save()
    return HttpResponse('Bank Data Is Inserted Successfully')




def insert_branch(self):
    with open('C:\\Users\\ajitm\\OneDrive\\Desktop\\Ajit\\DE2\\ajit\\Scripts\\CSV_DATA_to_DATABASE\\app\\branch1.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            bn=i[0]
            BO=Bank.objects.filter(bank_name=bn)
            if BO:
                ifs=i[1]
                br=i[2]
                ad=i[3]
                co=i[4]
                ci=i[5]
                di=i[6]
                st=i[7]


                BRO=Branch(bank_name=BO[0],ifsc=ifs,branch=br,address=ad,contact=co,city=ci,district=di,state=st)
                BRO.save()

    return HttpResponse('Branch Data Is Inserted Successfully')