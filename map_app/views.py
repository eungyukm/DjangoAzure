from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import map_app.models
import user_app.models
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
# Create your views here.


def map_main(request):
    # 파라미터를 추출합니다.
    map_info_idx = request.GET['map_info_idx']

    # 현재 게시판 정보를 가져옵니다.
    map_model = map_app.models.MapInfoTable.objects.get(
        map_info_idx=map_info_idx)

    template = loader.get_template('map_main.html')

    render_data = {
        'map_data': map_model,
        'map_info_idx': map_info_idx,

    }
    return HttpResponse(template.render(render_data, request))

# board/board_modify


def map_modify(request):
    template = loader.get_template('map_modify.html')
    render_data = {

    }
    return HttpResponse(template.render(render_data, request))

# board/board_read


def map_read(request):
    print('map read')

    # 파라미터 데티어를 추출
    map_info_idx = request.GET['map_info_idx']
    print(map_info_idx)
    map_data_idx = request.GET['map_data_idx']
    print(map_data_idx)
    page_num = request.GET['page_num']
    print(page_num)

    # 현재 글 정보를 가져옵니다.
    # 외래키 관계로 묶여 있으므로 select_related 함수를 사용합니다.
    map_model = map_app.models.MapDataTable.objects.select_related(
        'map_data_writer_idx', 'map_data_idx').get(map_data_idx=map_data_idx)
    print(map_model.map_data_writer_idx.user_name)

    template = loader.get_template('map_read.html')
    render_data = {
        'map_data_table': map_model,
        'map_info_idx': map_info_idx,
        'map_data_idx': map_data_idx,
        'page_num': page_num,
    }
    return HttpResponse(template.render(render_data, request))

# board/board_write


def map_write(request):
    map_info_idx = request.GET['map_info_idx']
    template = loader.get_template('map_write.html')
    render_data = {
        'map_info_idx': map_info_idx
    }
    return HttpResponse(template.render(render_data, request))


@csrf_exempt
def map_write_result(request):
    map_data_subject = request.POST['map_data_subject']
    map_data_text = request.POST['map_data_content']
    map_data_date = timezone.localtime()

    map_data_writer_idx = request.session['login_user_idx']
    # 외래키(BoardInfoTable의 PK 컬럼을 참조한다)
    map_info_idx = request.POST['map_info_idx']

    map_model = map_app.models.MapDataTable()
    map_model.map_data_subject = map_data_subject
    map_model.map_data_text = map_data_text
    map_model.map_data_date = map_data_date

    map_data_writer_model = user_app.models.UserTable.objects.get(
        user_idx=map_data_writer_idx)
    map_info_model = map_app.models.MapInfoTable.objects.get(
        map_info_idx=map_info_idx)

    map_model.map_data_writer_idx = map_data_writer_model
    map_model.map_info_idx = map_info_model

    # 업로드된 파일 명을 가져옵니다.
    map_model.map_data_file = request.FILES.get('map_file')

    map_model.save()

    map_model2 = map_app.models.MapDataTable.objects.all().order_by(
        '-map_data_idx')[0]
    print('my data', map_model2.map_data_idx)

    message = f'''
            <script>
                alert('저장되었습니다')
                locaiton.href = '/map/map_read'
            </script>
            '''
    print('실행!!')
    return HttpResponse(message)
