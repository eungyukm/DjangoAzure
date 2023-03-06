from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSerializer
import user_app.models
from rest_framework.parsers import JSONParser
from django.utils import timezone
import json
import map_app.models
from django.http import JsonResponse


@api_view(['GET'])
def getData(request):
    person = {'name': 'Dennis', 'age': 28}
    return Response(person)


@api_view(['POST'])
def postData(request):
    print(request.data)
    return Response()


@api_view(['POST'])
def api_login_view(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api_login_result(request):
    # 사용자가 입력한 파라미터를 추출합니다.
    body = json.loads(request.body)
    print(body)
    print(request.data)
    user_id = body['user_id']
    user_pw = body['user_pw']
    print(user_id)
    print(user_pw)
    try:
        user_model = user_app.models.UserTable.objects.get(user_id=user_id)
        # print(user_model)

        # 로그인한 사용자와 데이터베이스에서 가져온 데이터의 비밀번호가 같을 경우
        if user_pw == user_model.user_pw:
            # 로그인에 성공할 경우 세셔에 로그인 여부값을 저장합니다.
            res_message = '200'
            return Response(res_message, status=status.HTTP_200_OK)
        # 비밀번호가 다를 경우
        else:
            res_message = '210'
            return Response(res_message, status=status.HTTP_200_OK)
    except:
        # 아이디가 없는 경우
        res_message = '220'
        return Response(res_message, status=status.HTTP_200_OK)


@api_view(['POST'])
def api_map_create(request):
    body = json.loads(request.body)

    map_data_subject = body['map_data_subject']
    print(map_data_subject)
    map_data_text = body['map_data_text']
    print(map_data_text)
    map_data_writer_idx = body['map_data_writer_idx']
    print(map_data_writer_idx)
    map_info_idx = body['map_info_idx']
    print(map_info_idx)
    map_data_date = timezone.localtime()

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
    # map_model.map_data_file = request.FILES.get('map_file')

    map_model.save()

    res_message = '200'
    return Response(res_message, status=status.HTTP_200_OK)


@api_view(['GET'])
def api_map_select(request):
    # 파라미터를 추출합니다.
    map_info_idx = request.GET['map_info_idx']

    page_num = request.GET.get('page_num')
    if page_num == None:
        page_num = '1'

    page_num = int(page_num)

    # 현재 게시판 정보를 가져옵니다.
    map_model = map_app.models.MapInfoTable.objects.get(
        map_info_idx=map_info_idx)

    print(map_model.map_info_idx)
    print(map_model.map_info_name)

    # 현재 게시판의 글 목록을 가져옵니다.
    map_data_list = map_app.models.MapDataTable.objects
    map_data_list = map_data_list.select_related(
        'map_data_writer_idx', 'map_info_idx')
    map_data_list = map_data_list.filter(map_info_idx=map_info_idx)
    map_data_list = map_data_list.order_by('-map_data_idx')

    for map in map_data_list:
        print(map.map_data_idx)

    # 전체 글의 개수를 가져옵니다.
    map_data_cnt = len(map_data_list)
    print(map_data_cnt)

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

    res_message = '200'
    return JsonResponse(res_message, status=status.HTTP_200_OK)

@api_view(['POST'])
def api_profile_result(request):
    # 사용자가 입력한 파라미터를 추출합니다.
    body = json.loads(request.body)
    print(body)
    print(request.data)
    user_date = body['date']
    user_fps = body['fps']
    print(user_date)
    print(user_fps)

    
    # try:
    #     user_model = user_app.models.UserTable.objects.get(user_id=user_id)
    #     # print(user_model)

    #     # 로그인한 사용자와 데이터베이스에서 가져온 데이터의 비밀번호가 같을 경우
    #     if user_pw == user_model.user_pw:
    #         # 로그인에 성공할 경우 세셔에 로그인 여부값을 저장합니다.
    #         res_message = '200'
    #         return Response(res_message, status=status.HTTP_200_OK)
    #     # 비밀번호가 다를 경우
    #     else:
    #         res_message = '210'
    #         return Response(res_message, status=status.HTTP_200_OK)
    # except:
    #     # 아이디가 없는 경우
    #     res_message = '220'
    #     return Response(res_message, status=status.HTTP_200_OK)
