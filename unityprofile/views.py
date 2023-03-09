from unityprofile.models import GalaxyS10ProfileData
from django.shortcuts import render, HttpResponse
from django.template import loader
from unityprofile.models import GalaxyS10ProfileData, GalaxyS9ProfileData, GalaxyS8ProfileData, IPhone11ProfileData
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