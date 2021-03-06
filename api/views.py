from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSerializer
import user_app.models
from rest_framework.parsers import JSONParser
from django.utils import timezone
import json
import map_app.models


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
