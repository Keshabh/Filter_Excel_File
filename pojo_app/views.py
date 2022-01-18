from django.shortcuts import render
from django.http import HttpResponse
from .models import Pojo_Data
from .resources import PojoResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
# Create your views here.

def simple_upload(request):
    header=header =['Id','Month','Company','No_of_stocks_above_200_EMA','percentage_of_stocks_above_200_EMA','No_of_stocks_above_100_EMA','percentage_of_stocks_above_100_EMA','No_of_stocks_above_50_EMA','percentage_of_stocks_above_50_EMA']
    d=[]
    c=[]
    if request.method=='POST':
        pojo_resource = PojoResource()
        dataset = Dataset()
        new_data =  request.FILES['myfile']

        if not new_data.name.endswith('xlsx'):
            messages.info(request,'wrong format')
        
        imported_data = dataset.load(new_data.read(),format='xlsx')
        for data in imported_data:
            value= Pojo_Data(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8])
            value.save()
            
        #get the data from Pojo_Data table
        d=[]
        try:
            d= Pojo_Data.objects.all()
            #get all unique company names from table
            c=Pojo_Data.objects.values_list('Company',flat=True).distinct('Company')
        except:
            d=[]
    else:
        
        try: 
          d=Pojo_Data.objects.filter(Company=request.GET['company'])
        except:
            d= Pojo_Data.objects.all()
            #get all unique company names from table
            c=Pojo_Data.objects.values_list('Company',flat=True).distinct('Company')
    return render(request,'index.html',{'data':d,'head':header,'choices':c})
