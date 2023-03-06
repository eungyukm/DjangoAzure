from django.db import models

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