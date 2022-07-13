from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSerializer
import user_app.models


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
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api_login_result(request):
    # 사용자가 입력한 파라미터를 추출합니다.
    user_id = request.POST['user_id']
    user_pw = request.POST['user_pw']

    print(user_id)
    print(user_pw)

    # 데이터 베이스에서 사용자 데이터를 가져옵니다.
    # 데이터를 가져올 때 조건에 만족하는 것이 없으면 오류가 발생합니다.
    # 데이터가 없을 때의 처리르 해야 한다면 예외처리를 통해 처리합니다.
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
