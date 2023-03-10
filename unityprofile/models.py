from django.db import models
import django_tables2 as tables

# Create your models here.
class ProfileData(models.Model):
    profile_idx = models.AutoField(primary_key=True)
    profile_count = models.IntegerField(default="-1")
    device_name = models.CharField(max_length=100, default="none")
    project_name = models.CharField(max_length=100, default="none")
    scene_name = models.CharField(max_length=100, default="none")
    date = models.CharField(max_length=500)
    
    fps = models.FloatField(default=0.0)
    min_fps = models.FloatField(default=0.0)
    avg_fps = models.FloatField(default=0.0)
    max_fps = models.FloatField(default=0.0)
    set_pass_call = models.FloatField(default=0.0)
    draw_call = models.FloatField(default=0.0)
    tris = models.FloatField(default=0.0)
    vertices = models.FloatField(default=0.0)

    total_memory = models.FloatField(default=0.0)
    system_memory = models.FloatField(default=0.0)
    texture_memory = models.FloatField(default=0.0)
    mesh_memory = models.FloatField(default=0.0)


class GalaxyS10ProfileData(models.Model):
    profile_idx = models.AutoField(primary_key=True)
    profile_count = models.IntegerField(default="-1")
    device_name = models.CharField(max_length=100, default="none")
    project_name = models.CharField(max_length=100, default="none")
    scene_name = models.CharField(max_length=100, default="none")
    date = models.CharField(max_length=500)
    
    fps = models.FloatField(default=0.0)
    min_fps = models.FloatField(default=0.0)
    avg_fps = models.FloatField(default=0.0)
    max_fps = models.FloatField(default=0.0)
    set_pass_call = models.FloatField(default=0.0)
    draw_call = models.FloatField(default=0.0)
    tris = models.FloatField(default=0.0)
    vertices = models.FloatField(default=0.0)

    total_memory = models.FloatField(default=0.0)
    system_memory = models.FloatField(default=0.0)
    texture_memory = models.FloatField(default=0.0)
    mesh_memory = models.FloatField(default=0.0)

class GalaxyS8ProfileData(models.Model):
    profile_idx = models.AutoField(primary_key=True)
    profile_count = models.IntegerField(default="-1")
    device_name = models.CharField(max_length=100, default="none")
    project_name = models.CharField(max_length=100, default="none")
    scene_name = models.CharField(max_length=100, default="none")
    date = models.CharField(max_length=500)
    
    fps = models.FloatField(default=0.0)
    min_fps = models.FloatField(default=0.0)
    avg_fps = models.FloatField(default=0.0)
    max_fps = models.FloatField(default=0.0)
    set_pass_call = models.FloatField(default=0.0)
    draw_call = models.FloatField(default=0.0)
    tris = models.FloatField(default=0.0)
    vertices = models.FloatField(default=0.0)

    total_memory = models.FloatField(default=0.0)
    system_memory = models.FloatField(default=0.0)
    texture_memory = models.FloatField(default=0.0)
    mesh_memory = models.FloatField(default=0.0)

class GalaxyS9ProfileData(models.Model):
    profile_idx = models.AutoField(primary_key=True)
    profile_count = models.IntegerField(default="-1")
    device_name = models.CharField(max_length=100, default="none")
    project_name = models.CharField(max_length=100, default="none")
    scene_name = models.CharField(max_length=100, default="none")
    date = models.CharField(max_length=500)
    
    fps = models.FloatField(default=0.0)
    min_fps = models.FloatField(default=0.0)
    avg_fps = models.FloatField(default=0.0)
    max_fps = models.FloatField(default=0.0)
    set_pass_call = models.FloatField(default=0.0)
    draw_call = models.FloatField(default=0.0)
    tris = models.FloatField(default=0.0)
    vertices = models.FloatField(default=0.0)

    total_memory = models.FloatField(default=0.0)
    system_memory = models.FloatField(default=0.0)
    texture_memory = models.FloatField(default=0.0)
    mesh_memory = models.FloatField(default=0.0)

class IPhone11ProfileData(models.Model):
    profile_idx = models.AutoField(primary_key=True)
    profile_count = models.IntegerField(default="-1")
    device_name = models.CharField(max_length=100, default="none")
    project_name = models.CharField(max_length=100, default="none")
    scene_name = models.CharField(max_length=100, default="none")
    date = models.CharField(max_length=500)
    
    fps = models.FloatField(default=0.0)
    min_fps = models.FloatField(default=0.0)
    avg_fps = models.FloatField(default=0.0)
    max_fps = models.FloatField(default=0.0)
    set_pass_call = models.FloatField(default=0.0)
    draw_call = models.FloatField(default=0.0)
    tris = models.FloatField(default=0.0)
    vertices = models.FloatField(default=0.0)

    total_memory = models.FloatField(default=0.0)
    system_memory = models.FloatField(default=0.0)
    texture_memory = models.FloatField(default=0.0)
    mesh_memory = models.FloatField(default=0.0)

class WarningProfileData(models.Model):
    profile_idx = models.AutoField(primary_key=True)
    profile_count = models.IntegerField(default="-1")
    device_name = models.CharField(max_length=100, default="none")
    project_name = models.CharField(max_length=100, default="none")
    scene_name = models.CharField(max_length=100, default="none")
    date = models.CharField(max_length=500)
    
    fps = models.FloatField(default=0.0)
    min_fps = models.FloatField(default=0.0)
    avg_fps = models.FloatField(default=0.0)
    max_fps = models.FloatField(default=0.0)
    set_pass_call = models.FloatField(default=0.0)
    draw_call = models.FloatField(default=0.0)
    tris = models.FloatField(default=0.0)
    vertices = models.FloatField(default=0.0)

    total_memory = models.FloatField(default=0.0)
    system_memory = models.FloatField(default=0.0)
    texture_memory = models.FloatField(default=0.0)
    mesh_memory = models.FloatField(default=0.0)


class GalaxyS10ProfileDataTable(tables.Table):
    profile_idx = tables.Column(verbose_name='profile_idx')
    profile_count = tables.Column(verbose_name='profile_count')
    device_name = tables.Column(verbose_name='device_name')
    project_name = tables.Column(verbose_name='project_name')
    scene_name = tables.Column(verbose_name='scene_name')
    date = tables.Column(verbose_name='date')
    fps = tables.Column(verbose_name='fps')
    min_fps = tables.Column(verbose_name='min_fps')
    avg_fps = tables.Column(verbose_name='avg_fps')
    max_fps = tables.Column(verbose_name='max_fps')
    set_pass_call = tables.Column(verbose_name='set_pass_call')
    draw_call = tables.Column(verbose_name='draw_call')
    tris = tables.Column(verbose_name='tris')
    vertices = tables.Column(verbose_name='vertices')
    total_memory = tables.Column(verbose_name='total_memory')
    system_memory = tables.Column(verbose_name='system_memory')
    texture_memory = tables.Column(verbose_name='texture_memory')
    mesh_memory = tables.Column(verbose_name='mesh_memory')

    class Meta:
        moel = GalaxyS10ProfileData
        # fields = ("profile_idx",)
        fields = ('profile_idx', 'profile_count', 'device_name', 'project_name', 'scene_name', 'date',
                  'fps', 'min_fps', 'avg_fps', 'max_fps', 'set_pass_call', 'draw_call', 'tris', 'vertices',
                  'total_memory', 'system_memory', 'texture_memory', 'mesh_memory')

        # fields = {'profile_count', 'device_name'}

        # attrs = {
        #     'thead': {
        #         'class': 'thead-dark', # thead에 Bootstrap의 스타일을 적용
        #         'style': 'color: white;', # 글자 색상 변경
        #     },
        #     'th': {
        #         'style': 'background-color: #337ab7; border-color: #2e6da4; font-weight: bold;', # th 요소에 스타일 적용
        #     },
        # }

        attrs = {
            'class': 'table table-hover table-striped',  # bootstrap 테마 적용
        }

class ScenarioDataTable(models.Model):
    scenario_data_idx = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)
    device_name = models.CharField(max_length=30, default='none')
    scenario_data_subject = models.CharField(max_length=500)
    scenario_data_text = models.TextField()
    scenario_profile_idx = models.IntegerField(default=0)
    scenario_data_file = models.FileField(upload_to='files/', null=True)