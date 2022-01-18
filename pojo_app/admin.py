from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import Pojo_Data
# Register your models here.
@admin.register(Pojo_Data)
class Pojo_Admin(ImportExportModelAdmin):
     list_display =('Month','Company','No_of_stocks_above_200_EMA','percentage_of_stocks_above_200_EMA','No_of_stocks_above_100_EMA','percentage_of_stocks_above_100_EMA','No_of_stocks_above_50_EMA','percentage_of_stocks_above_50_EMA')