from unityprofile.models import GalaxyS10ProfileData
from django.shortcuts import render, HttpResponse
from django.template import loader
from unityprofile.models import GalaxyS10ProfileData, GalaxyS9ProfileData, GalaxyS8ProfileData, IPhone11ProfileData
from unityprofile.models import GalaxyS10ProfileDataTable
from unityprofile.models import DeviceInfoTable, ProjectInfoTable

# 테스트 시나리오 저장 테이블
from unityprofile.models import ScenarioDataTable
from prettytable import PrettyTable

from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

# Create your views here.
def index(request):
    # Mysql에서 데이터를 가져와서 객체 리스트로 생성
    queryset = GalaxyS10ProfileData.objects.all()

    # 컬럼별로 분류할 딕셔너리를 생성
    fps_dict = {}
    profile_count_dict = {}

    for model_data in queryset:
        fps_dict.setdefault(model_data.profile_count, model_data.fps)
    
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def galaxys10profiledatatable(requeset):
    queryset = GalaxyS10ProfileData.objects.order_by('-profile_idx')[:10]
    
    content_list =[]
    for q1 in queryset:
        # 리스트에 담는다.
        content_list.append(q1)

    render_data = {
        'device' : 'GalaxyS10',
        'content_list': content_list,
    }

    template = loader.get_template('profile.html')
    return HttpResponse(template.render(render_data, requeset))

def galaxys9profiledatatable(requeset):
    queryset = GalaxyS9ProfileData.objects.order_by('-profile_idx')[:10]
    
    content_list =[]
    for q1 in queryset:
        # 리스트에 담는다.
        content_list.append(q1)

    render_data = {
        'device' : 'GalaxyS9',
        'content_list': content_list,
    }

    template = loader.get_template('profile.html')
    return HttpResponse(template.render(render_data, requeset))

def galaxys8profiledatatable(requeset):
    queryset = GalaxyS8ProfileData.objects.order_by('-profile_idx')[:10]
    
    content_list =[]
    for q1 in queryset:
        # 리스트에 담는다.
        content_list.append(q1)

    render_data = {
        'device' : 'GalaxyS8',
        'content_list': content_list,
    }

    template = loader.get_template('profile.html')
    return HttpResponse(template.render(render_data, requeset))

# 아이폰
def iphone11profiledatatable(requeset):
    queryset = IPhone11ProfileData.objects.order_by('-profile_idx')[:10]
    
    content_list =[]
    for q1 in queryset:
        # 리스트에 담는다.
        content_list.append(q1)

    render_data = {
        'device' : 'IPhone11',
        'content_list': content_list,
    }

    template = loader.get_template('profile.html')
    return HttpResponse(template.render(render_data, requeset))

# 아이폰 11 테스트 결과 출력
def iphone11test(requeset):
    idx_list = [6784, 6789, 6812, 4734, 5734, 6728, 4772, 4836, 4857, 6711,
                6701, 5007, 5056, 5775, 6780, 5306, 5981, 6136, 5628, 6451, 6639, 6656]
    content_list =[]
    for idx in idx_list:
        queryset = IPhone11ProfileData.objects.get(profile_idx=idx)
        content_list.append(queryset)

    render_data = {
        'device' : 'IPhone11',
        'content_list': content_list,
    }

    template = loader.get_template('profile.html')
    return HttpResponse(template.render(render_data, requeset))

# 프로파일 데이터 전체 삭제
def remove_profiledatatable(requeset):
    device = requeset.GET['device']

    message = '''
            <script>
                alert('데이터가 삭제 되었습니다.')
                location.href = '/profile/galaxy10profiledatatable'
            </script>
            '''
    
    galaxys10_message = '''
            <script>
                alert('데이터가 삭제 되었습니다.')
                location.href = '/profile/galaxy10profiledatatable'
            </script>
            '''
    
    galaxys9_message = '''
            <script>
                alert('데이터가 삭제 되었습니다.')
                location.href = '/profile/galaxy9profiledatatable'
            </script>
            '''
    
    galaxys8_message = '''
            <script>
                alert('데이터가 삭제 되었습니다.')
                location.href = '/profile/galaxy8profiledatatable'
            </script>
            '''
    
    iPhone11_message = '''
            <script>
                alert('데이터가 삭제 되었습니다.')
                location.href = '/profile/iphone11profiledatatable'
            </script>
            '''

    if device == 'GalaxyS10':
        GalaxyS10ProfileData.objects.all().delete()
        return HttpResponse(galaxys10_message)
    elif device == 'GalaxyS9':
        GalaxyS9ProfileData.objects.all().delete()
        return HttpResponse(galaxys9_message)
    elif device == 'GalaxyS8':
        GalaxyS8ProfileData.objects.all().delete()
        return HttpResponse(galaxys8_message)
    elif device == 'IPhone11':
        IPhone11ProfileData.objects.all().delete()
        return HttpResponse(iPhone11_message)
    else:
        return HttpResponse(message)

# FPS Line Chart
def FPSLineChart(requeset):
    galaxys10 = GalaxyS10ProfileData.objects.order_by('-profile_idx')[:10]
    galaxys9 = GalaxyS9ProfileData.objects.order_by('-profile_idx')[:10]
    galaxys8 = GalaxyS8ProfileData.objects.order_by('-profile_idx')[:10]
    iphone11 = IPhone11ProfileData.objects.order_by('-profile_idx')[:10]

    render_data = {
        'galaxys10' : galaxys10,
        'galaxys9': galaxys9,
        'galaxys8': galaxys8,
        'iphone11': iphone11,
    }

    template = loader.get_template('profile.html')
    return HttpResponse(template.render(render_data, requeset))


# 시나리오 작성
def write_scenario(request):
    template = loader.get_template('scenario_form.html')
    return HttpResponse(template.render())


@csrf_exempt
def scenario_write_result(request):
    project_name = request.POST['project_name']
    scenario_data_subject = request.POST['scenario_data_subject']
    scenario_data_text = request.POST['scenario_data_text']

    scenario_model = ScenarioDataTable()
    scenario_model.project_name = project_name
    scenario_model.scenario_data_subject = scenario_data_subject
    scenario_model.scenario_data_text = scenario_data_text

    # 업로드된 파일 명을 가져옵니다.
    scenario_model.scenario_data_file = request.FILES.get('scenario_data_file')

    scenario_model.save()


    message = f'''
            <script>
                alert('저장되었습니다')
                location.href = '/profile/write_scenario'
            </script>
            '''
    return HttpResponse(message)


# SetPassCall, DrawCall, Tris
def scenario_main(request):
    scenario_data_lit = ScenarioDataTable.objects.all()
    profile_data = []

    for scenario in scenario_data_lit:
        data = IPhone11ProfileData.objects.filter(profile_idx=scenario.scenario_profile_idx).first()
        if(data):
            profile_data.append(data)
        else:
            data = IPhone11ProfileData()
            profile_data.append(data)

    data_list = zip(scenario_data_lit,profile_data)
    template = loader.get_template('scenario_main.html')

    render_data = {
        'data_list' : data_list,
    }

    return HttpResponse(template.render(render_data, request))

def scenario_modify(request):
    # 파라미터 데이터를 추출합니다.
    scenario_data_idx = request.GET['scenario_data_idx']
    scenario_data = ScenarioDataTable.objects.filter(scenario_data_idx = scenario_data_idx).first()
    # 디바이스 정보를 가지고 있는 리스트
    device_info_list = DeviceInfoTable.objects.all()


    template = loader.get_template('scenario_modify.html')
    render_data = {
        'scenario_data': scenario_data,
        'device_info_list' : device_info_list,
    }
    return HttpResponse(template.render(render_data, request))

@csrf_exempt
def scenario_modify_result(request):
    scenario_data_idx = request.POST['scenario_data_idx']
    project_name = request.POST['project_name']
    scenario_data_subject = request.POST['scenario_data_subject']
    scenario_data_text = request.POST['scenario_data_text']
    scenario_profile_idx = request.POST['scenario_profile_idx']
    scenario_data_file = request.POST['scenario_data_file']
    device_name = request.POST['device_name']

    scenario_model = ScenarioDataTable.objects.get(scenario_data_idx = scenario_data_idx)

    # 정보 설정
    scenario_model.project_name = project_name
    scenario_model.scenario_data_subject = scenario_data_subject
    scenario_model.scenario_data_text = scenario_data_text
    scenario_model.scenario_profile_idx = scenario_profile_idx
    scenario_model.scenario_data_file = scenario_data_file
    scenario_model.device_name = device_name

    if scenario_data_file:
        scenario_model.scenario_data_file = scenario_data_file

    # 저장합니다.
    scenario_model.save()


    message = f'''
            <script>
                alert('저장되었습니다')
                location.href = '/profile/scenario_modify?scenario_data_idx={scenario_data_idx}'
            </script>
            '''
    return HttpResponse(message)