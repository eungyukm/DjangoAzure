from unityprofile.models import GalaxyS10ProfileData
from django.shortcuts import render, HttpResponse
from django.template import loader
from unityprofile.models import GalaxyS10ProfileData, GalaxyS9ProfileData, GalaxyS8ProfileData
from unityprofile.models import GalaxyS10ProfileDataTable
from prettytable import PrettyTable

# Create your views here.
def index(request):
    # Mysql에서 데이터를 가져와서 객체 리스트로 생성
    queryset = GalaxyS10ProfileData.objects.all()

    # 컬럼별로 분류할 딕셔너리를 생성
    fps_dict = {}
    profile_count_dict = {}

    for model_data in queryset:
        fps_dict.setdefault(model_data.profile_count, model_data.fps)
    
    print(fps_dict)

    
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def galaxys10profiledatatable(requeset):
    queryset = GalaxyS10ProfileData.objects.all()

    print(queryset)

    # table = GalaxyS10ProfileDataTable(queryset)
    

    table = PrettyTable()
    table.field_names = ['Name', 'Age', 'Gender']
    table.add_row(["John", 25, "M"])
    table.add_row(["Jane", 30, "F"])
    context = {'table' : queryset}
    print(table)
    template = loader.get_template('profile.html')
    return HttpResponse(template.render(context, requeset))