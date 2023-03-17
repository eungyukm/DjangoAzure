from unityprofile.models import GalaxyS10ProfileData
from django.shortcuts import render, HttpResponse
from django.template import loader
from unityprofile.models import GalaxyS10ProfileData, GalaxyS9ProfileData, GalaxyS8ProfileData, IPhone11ProfileData
from unityprofile.models import GalaxyS10ProfileDataTable
from unityprofile.models import DeviceInfoTable, ProjectInfoTable

# 테스트 시나리오 저장 테이블
from unityprofile.models import ScenarioDataTable, ProfileResultTable
from prettytable import PrettyTable

from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db.models import Q

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
def profiledata_all(requeset):
    device = requeset.GET['device']
    queryset = []
    if(device == 'GalaxyS10'):
        queryset = GalaxyS10ProfileData.objects.all()
    elif(device == 'GalaxyS9'):
        queryset = GalaxyS9ProfileData.objects.all()
    elif(device == 'GalaxyS8'):
        queryset = GalaxyS8ProfileData.objects.all()
    elif(device == 'IPhone11'):
        queryset = IPhone11ProfileData.objects.all()
    
    content_list =[]
    for q1 in queryset:
        # 리스트에 담는다.
        content_list.append(q1)

    render_data = {
        'device' : device,
        'content_list': queryset,
    }

    template = loader.get_template('profile_all.html')
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

# 시나리오 데이터를 추가하는 코드
@csrf_exempt
def scenario_write_result(request):
    project_name = request.POST['project_name']
    scenario_data_subject = request.POST['scenario_data_subject']
    scenario_data_text = request.POST['scenario_data_text']
    ordering_number = request.POST['ordering_number']

    scenario_model = ScenarioDataTable()
    scenario_model.project_name = project_name
    scenario_model.scenario_data_subject = scenario_data_subject
    scenario_model.scenario_data_text = scenario_data_text
    scenario_model.ordering_number = ordering_number

    # 업로드된 파일 명을 가져옵니다.
    scenario_model.scenario_data_file = request.FILES.get('scenario_data_file')

    scenario_model.save()

    message = f'''
            <script>
                alert('저장되었습니다')
                location.href = '/profile/project_scenario_main?project_name={project_name}'
            </script>
            '''
    return HttpResponse(message)

# --------------------------------------------------------------------------------------------------------------------------------------------- 
# SetPassCall, DrawCall, Tris
def scenario_main(request):
    device = request.GET['device']
    scenario_data_lit = ScenarioDataTable.objects.all()
    profile_data = []

    for scenario in scenario_data_lit:
        if(device == 'GalaxyS10'):
            data = GalaxyS10ProfileData.objects.filter(profile_idx=scenario.scenario_profile_idx).first()
            if(data):
                profile_data.append(data)
            else:
                data = GalaxyS10ProfileData()
                profile_data.append(data)
        elif(device == 'GalaxyS9'):
            data = GalaxyS9ProfileData.objects.filter(profile_idx=scenario.scenario_profile_idx).first()
            if(data):
                profile_data.append(data)
            else:
                data = GalaxyS9ProfileData()
                profile_data.append(data)
        elif(device == 'GalaxyS8'):
            data = GalaxyS8ProfileData.objects.filter(profile_idx=scenario.scenario_profile_idx).first()
            if(data):
                profile_data.append(data)
            else:
                data = GalaxyS8ProfileData()
                profile_data.append(data)

        elif(device == 'IPhone11'):
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
        'device' : device,
    }

    return HttpResponse(template.render(render_data, request))

# --------------------------------------------------------------------------------------------------------------------------------------------- 
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

# --------------------------------------------------------------------------------------------------------------------------------------------- 
def project_scenario_delete(request):
    project_name = request.GET['project_name']
    # 파라미터 데이터를 추출합니다.
    scenario_data_idx = request.GET['scenario_data_idx']

    query = ScenarioDataTable.objects.get(scenario_data_idx=scenario_data_idx)
    query.delete()
    message = f'''
        <script>
            alert('삭제되었습니다')
            location.href = '/profile/project_scenario_main?project_name={project_name}'
        </script>
         '''
    return HttpResponse(message)

# --------------------------------------------------------------------------------------------------------------------------------------------- 
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


# --------------------------------------------------------------------------------------------------------------------------------------------- 
def project_scenario_main(request):
    project_name = request.GET['project_name']
    scenario_list = ScenarioDataTable.objects.filter(project_name=project_name)

    template = loader.get_template('project_scenario_main.html')

    render_data = {
        'project' : project_name,
        'scenario_list' : scenario_list,
    }

    return HttpResponse(template.render(render_data, request))

# 프로젝트의 프로파일 결과를 출력하는 html response
def project_scenario_modify(request):
    project_name = request.GET['project_name']
    scenario_data_idx = request.GET['scenario_data_idx']

    # 파라미터 데이터를 추출합니다.
    scenario_list = ScenarioDataTable.objects.filter(scenario_data_idx = scenario_data_idx).first()


    template = loader.get_template('project_scenario_modify.html')

    render_data = {
        'project' : project_name,
        'scenario_list' : scenario_list,
    }
    return HttpResponse(template.render(render_data, request))

# --------------------------------------------------------------------------------------------------------------------------------------------- 
@csrf_exempt
def project_scenario_modify_result(request):
    scenario_data_idx = request.POST['scenario_data_idx']
    project_name = request.POST['project_name']
    scenario_data_subject = request.POST['scenario_data_subject']
    scenario_data_text = request.POST['scenario_data_text']
    scenario_data_file = request.POST['scenario_data_file']
    ordering_number = request.POST['ordering_number']

    scenario_model = ScenarioDataTable.objects.get(scenario_data_idx= int(scenario_data_idx))

    # 정보 설정
    scenario_model.project_name = project_name
    scenario_model.scenario_data_subject = scenario_data_subject
    scenario_model.scenario_data_text = scenario_data_text
    scenario_model.scenario_data_file = scenario_data_file
    scenario_model.ordering_number = ordering_number

    if scenario_data_file:
        scenario_model.scenario_data_file = scenario_data_file

    # 저장합니다.
    scenario_model.save()


    message = f'''
            <script>
                alert('수정되었습니다')
                location.href = '/profile/project_scenario_main?project_name={project_name}&&scenario_data_idx={scenario_data_idx}'
            </script>
            '''
    return HttpResponse(message)

# ---------------------------------------------------------------------------------------------------------------------------------------------
# 프로파일 결과 입력 관리
def profile_input_main(request):
    project_name = request.GET['project_name']
    scenario_list = ScenarioDataTable.objects.filter(project_name=project_name)

    template = loader.get_template('profile_input_main.html')

    render_data = {
        'project_name' : project_name,
        'scenario_list' : scenario_list,
    }

    return HttpResponse(template.render(render_data, request))

# 프로파일 결과 입력
def profile_input_write(request):
    project_name = request.GET['project_name']
    scenario_data_idx = request.GET['scenario_data_idx']
    scenario_list = ScenarioDataTable.objects.filter(scenario_data_idx=scenario_data_idx).first()
    template = loader.get_template('profile_input_write.html')
    device_info_lit = DeviceInfoTable.objects.all()

    render_data = {
        'project_name' : project_name,
        'scenario_list' : scenario_list,
        'device_info_lit' :device_info_lit,
    }

    return HttpResponse(template.render(render_data, request))

# 프로파일 결과 저장
def profile_input_write_result(request):
    target_fps = request.POST['target_fps']
    project_name = request.POST['project_name']
    scenario_data_idx = request.POST['scenario_data_idx'] 
    device_name = request.POST['device_name']
    scenario_profile_idx = request.POST['scenario_profile_idx']
    ordering_number = request.POST['ordering_number']
    device_temperature = request.POST['device_temperature']

    device_info = DeviceInfoTable.objects.filter(device_name=device_name).first()
    scenario_data = ScenarioDataTable.objects.get(scenario_data_idx=scenario_data_idx)

    profile_result_table = ProfileResultTable()
    profile_result_table.project_name = project_name
    profile_result_table.scenario_data = scenario_data
    profile_result_table.target_fps = target_fps

    profile_result_table.device = device_info
    
    profile_result_table.scenario_profile_idx = scenario_profile_idx
    profile_result_table.ordering_number = ordering_number
    profile_result_table.device_temperature = device_temperature
    profile_result_table.save()

    message = f'''
            <script>
                alert('저장되었습니다')
                location.href = '/profile/profile_input_main?device_id={device_info.device_info_idx}&&project_name={project_name}'
            </script>
            '''
    return HttpResponse(message)
# ---------------------------------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------------------------------
# 프로파일의 결과를 출력하는 화면
def profile_result_main(request):
    project_name = request.GET['project_name']
    device_id = request.GET['device_id']
    target_fps = request.GET['target_fps']

    query = Q(project_name=project_name) & Q(device_id=device_id) & Q(target_fps=target_fps)
    profile_reulst_list = ProfileResultTable.objects.filter(query)
    device_info_table = DeviceInfoTable.objects.filter(device_info_idx=device_id).first()
    device_name = device_info_table.device_name

    profile_performance_idx_list = []
    for profile_result in profile_reulst_list:
        profile_performance_idx_list.append(profile_result.scenario_profile_idx)


    print('device_id', device_id)
    print('profile_performance_idx_list ' ,profile_performance_idx_list)

    # 각 시나리오 별 프로파일 결과
    profile_performance_result_list = []

    for idx in profile_performance_idx_list:
        if device_id == '1':
            profile_performance_result_list.append(GalaxyS10ProfileData.objects.filter(profile_idx=idx).first())
        elif device_id == '2':
            profile_performance_result_list.append(GalaxyS9ProfileData.objects.filter(profile_idx=idx).first())
        elif device_id == '3':
            profile_performance_result_list.append(GalaxyS8ProfileData.objects.filter(profile_idx=idx).first())
        elif device_id == '4':
            print('IPhone' , IPhone11ProfileData.objects.filter(profile_idx=idx).first())
            profile_performance_result_list.append(IPhone11ProfileData.objects.filter(profile_idx=idx).first())

    print('profile_performance_result_list',profile_performance_result_list)

    data_list = zip(profile_reulst_list, profile_performance_result_list)

    template = loader.get_template('profile_result_main.html')

    render_data = {
        'project_name' : project_name,
        'device_name' : device_name,
        'profile_reulst_list' : profile_reulst_list,
        'profile_performance_result_list' : profile_performance_result_list,
        'data_list' : data_list,
    }

    return HttpResponse(template.render(render_data, request))

def profile_result_modify(request):
    # 파라미터 데이터를 추출합니다.
    profile_result_id = request.GET['profile_result_id']
    profile_result_list = ProfileResultTable.objects.filter(profile_result_id=profile_result_id).first()
    # 디바이스 정보를 가지고 있는 리스트
    device_info_list = DeviceInfoTable.objects.all()
    print('device_info_list', device_info_list)
    device_name = DeviceInfoTable.objects.filter(device_info_idx=profile_result_list.device.device_info_idx).first().device_name

    # 
    scenario_data = ScenarioDataTable.objects.filter(scenario_data_idx=profile_result_list.scenario_data.scenario_data_idx).first()

    template = loader.get_template('profile_result_modify.html')
    render_data = {
        'profile_result_list': profile_result_list,
        'device_info_list' : device_info_list,
        'device_name' : device_name,
        'scenario_data' : scenario_data,
    }
    return HttpResponse(template.render(render_data, request))

def profile_result_modify_result(request):
    profile_result_id = request.POST['profile_result_id']
    device_temperature = request.POST['device_temperature']
    ordering_number = request.POST['ordering_number'] 
    scenario_profile_idx = request.POST['scenario_profile_idx']
    device_name = request.POST['device_name']
    project_name = request.POST['project_name']
    target_fps = request.POST['target_fps']

    device_info = DeviceInfoTable.objects.filter(device_name=device_name).first()

    profile_result_table = ProfileResultTable.objects.filter(profile_result_id=profile_result_id).first()
    profile_result_table.target_fps = target_fps

    profile_result_table.device = device_info
    
    profile_result_table.scenario_profile_idx = scenario_profile_idx
    profile_result_table.ordering_number = ordering_number
    profile_result_table.device_temperature = device_temperature
    profile_result_table.save()

    message = f'''
            <script>
                alert('저장되었습니다')
                location.href = '/profile/profile_result_main?device_id={device_info.device_info_idx}&&project_name={project_name}&&target_fps={target_fps}'
            </script>
            '''
    return HttpResponse(message)