# from curses import def_prog_mode
from tempfile import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import map_app.models
import user_app.models
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.


def map_main(request):
    # 파라미터를 추출합니다.
    map_info_idx = request.GET['map_info_idx']

    page_num = request.GET.get('page_num')
    if page_num == None:
        page_num = '1'

    page_num = int(page_num)

    # 현재 게시판 정보를 가져옵니다.
    map_model = map_app.models.MapInfoTable.objects.get(
        map_info_idx=map_info_idx)

    # 현재 게시판의 글 목록을 가져옵니다.
    map_data_list = map_app.models.MapDataTable.objects
    map_data_list = map_data_list.select_related(
        'map_data_writer_idx', 'map_info_idx')
    map_data_list = map_data_list.filter(map_info_idx=map_info_idx)
    map_data_list = map_data_list.order_by('-map_data_idx')

    # 전체 글의 개수를 가져옵니다.
    map_data_cnt = len(map_data_list)
    # print(map_data_cnt)

    # 페이징을 위한 객체를 생성합니다.
    # 첫 번째 : 전체 데이터 목록,
    # 두 번째 : 한 페이지당 보여줄 데이터의 개수
    paginator = Paginator(map_data_list, 10)
    map_data_list = paginator.get_page(page_num)

    # 하단 페이지네이션의 최소와 최대값 구하는 식
    a1 = int((page_num - 1) / 10)
    a2 = a1 * 10
    page_min = a2 + 1
    page_max = page_min + 9

    # 전체 페이지 수를 구합니다.
    page_cnt = map_data_cnt // 10
    if map_data_cnt % 10 > 0:
        page_cnt = page_cnt + 1
    print(page_cnt)

    # 이전
    page_prev = page_min - 1
    # 다음
    page_next = page_max + 1
    print(page_next)

    # page_next가 page_cnt보다 크면 전체 페이지수로 세팅한다.
    if page_next > page_cnt:
        page_next = page_cnt

    # 만약 page_max가 전체 페이지 수 보다 크면 전체 페이지수로 세팅합니다.
    if page_max > page_cnt:
        page_max = page_cnt

    pagenation_list = list(range(page_min, page_max + 1))

    template = loader.get_template('map_main.html')

    # print(page_next)

    render_data = {
        'map_data': map_model,
        'map_info_idx': map_info_idx,
        'map_data_list': map_data_list,
        'pagenation_data': pagenation_list,
        'page_num': page_num,
        'page_prev': page_prev,
        'page_next': page_next,
        'page_cnt': page_cnt,
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

    # 현재 글 정보를 가져옵니다.
    # 외래키 관계로 묶여 있으므로 select_related 함수를 사용합니다.
    map_model = map_app.models.MapDataTable.objects.select_related(
        'map_data_writer_idx', 'map_info_idx').get(map_data_idx=map_data_idx)
    print(map_model.map_data_writer_idx.user_name)

    template = loader.get_template('map_read.html')
    render_data = {
        'map_data': map_model,
        'map_info_idx': map_info_idx,
        'map_data_idx': map_data_idx,
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
                alert('수정되었습니다')
                location.href = '/map/map_read?map_info_idx={map_info_idx}&map_data_idx={map_model2.map_data_idx}'
            </script>
            '''
    print('실행!!')
    return HttpResponse(message)
