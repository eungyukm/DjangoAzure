from django.db import models
from user_app.models import UserTable

# Create your models here.

# 게시판 정보 테이블


class MapInfoTable(models.Model):
    map_info_idx = models.AutoField(primary_key=True)
    map_info_name = models.CharField(max_length=500)

# 게시글 정보 테이들


class MapDataTable(models.Model):
    map_data_idx = models.AutoField(primary_key=True)
    map_data_subject = models.CharField(max_length=500)
    map_data_text = models.TextField()
    map_data_file = models.FileField(upload_to='files/', null=True)
    # 외래키(UserTable의 PK 컬럼을 참조합니다.
    # 만약 참조하는 테이블의 PK 컬럼이 아닌 다른 컬럼을 참조하겠다면
    # related_name='컬럼명'을 설정해 줍니다.
    map_data_writer_idx = models.ForeignKey(
        UserTable, on_delete=models.CASCADE)
    # 외래키(BoardInfoTable의 PK 컬럼을 참조한다)
    map_info_idx = models.ForeignKey(
        MapInfoTable, on_delete=models.CASCADE)
    map_data_date = models.DateTimeField()
