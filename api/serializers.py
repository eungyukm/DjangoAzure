from pkg_resources import require
from rest_framework import serializers
from user_app.models import UserTable
from map_app.models import MapDataTable
from unityprofile.models import ProfileData, WarningProfileData
from unityprofile.models import GalaxyS10ProfileData
from unityprofile.models import GalaxyS8ProfileData
from unityprofile.models import GalaxyS9ProfileData

class UserSerializer(serializers.ModelSerializer):
    # user_idx = serializers.IntegerField(read_only=True)
    user_name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    user_id = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    user_pw = serializers.CharField(
        required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        return UserTable.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.user_idx = validated_data.get('user_idx', instance.user_idx)
        instance.user_name = validated_data.get(
            'user_name', instance.user_name)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.user_pw = validated_data.get('user_pw', instance.user_pw)
        # instance.save()
        return instance

    class Meta:
        model = UserTable
        ordering = ['created']
        fields = '__all__'


class MapDataSerializer(serializers.ModelSerializer):
    map_data_subject = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    map_data_text = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    map_data_writer_idx = serializers.IntegerField(required=True)
    map_info_idx = serializers.IntegerField(required=True)
    map_data_date = serializers.CharField(
        required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        return MapDataTable.objects.create(**validated_data)

    class Meta:
        model = MapDataTable
        ordering = ['created']
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    profile_count = serializers.IntegerField(required=True)
    scene_name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    project_name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    
    date = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    fps = serializers.FloatField(required=True)
    min_fps = serializers.FloatField(required=True)
    avg_fps = serializers.FloatField(required=True)
    max_fps  = serializers.FloatField(required=True)
    set_pass_call = serializers.FloatField(required=True)
    draw_call = serializers.FloatField(required=True)
    tris = serializers.FloatField(required=True)
    vertices = serializers.FloatField(required=True)

    total_memory = serializers.FloatField(required=True)
    system_memory = serializers.FloatField(required=True)
    texture_memory = serializers.FloatField(required=True)
    mesh_memory = serializers.FloatField(required=True)

    def create(self, validated_data):
        return ProfileSerializer.objects.create(**validated_data)

    class Meta:
        model = ProfileData
        ordering = ['created']
        fields = '__all__'

class GalaxyS10ProfileSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    profile_count = serializers.IntegerField(required=True)
    scene_name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    project_name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    
    date = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    fps = serializers.FloatField(required=True)
    min_fps = serializers.FloatField(required=True)
    avg_fps = serializers.FloatField(required=True)
    max_fps  = serializers.FloatField(required=True)
    set_pass_call = serializers.FloatField(required=True)
    draw_call = serializers.FloatField(required=True)
    tris = serializers.FloatField(required=True)
    vertices = serializers.FloatField(required=True)

    total_memory = serializers.FloatField(required=True)
    system_memory = serializers.FloatField(required=True)
    texture_memory = serializers.FloatField(required=True)
    mesh_memory = serializers.FloatField(required=True)

    def create(self, validated_data):
        return ProfileSerializer.objects.create(**validated_data)

    class Meta:
        model = GalaxyS10ProfileData
        ordering = ['created']
        fields = '__all__'

class GalaxyS8ProfileSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    profile_count = serializers.IntegerField(required=True)
    scene_name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    project_name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    
    date = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    fps = serializers.FloatField(required=True)
    min_fps = serializers.FloatField(required=True)
    avg_fps = serializers.FloatField(required=True)
    max_fps  = serializers.FloatField(required=True)
    set_pass_call = serializers.FloatField(required=True)
    draw_call = serializers.FloatField(required=True)
    tris = serializers.FloatField(required=True)
    vertices = serializers.FloatField(required=True)

    total_memory = serializers.FloatField(required=True)
    system_memory = serializers.FloatField(required=True)
    texture_memory = serializers.FloatField(required=True)
    mesh_memory = serializers.FloatField(required=True)

    def create(self, validated_data):
        return ProfileSerializer.objects.create(**validated_data)

    class Meta:
        model = GalaxyS8ProfileData
        ordering = ['created']
        fields = '__all__'

class GalaxyS9ProfileSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    profile_count = serializers.IntegerField(required=True)
    scene_name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    project_name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    
    date = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    fps = serializers.FloatField(required=True)
    min_fps = serializers.FloatField(required=True)
    avg_fps = serializers.FloatField(required=True)
    max_fps  = serializers.FloatField(required=True)
    set_pass_call = serializers.FloatField(required=True)
    draw_call = serializers.FloatField(required=True)
    tris = serializers.FloatField(required=True)
    vertices = serializers.FloatField(required=True)

    total_memory = serializers.FloatField(required=True)
    system_memory = serializers.FloatField(required=True)
    texture_memory = serializers.FloatField(required=True)
    mesh_memory = serializers.FloatField(required=True)

    def create(self, validated_data):
        return ProfileSerializer.objects.create(**validated_data)

    class Meta:
        model = GalaxyS9ProfileData
        ordering = ['created']
        fields = '__all__'

class WarningProfileSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    profile_count = serializers.IntegerField(required=True)
    scene_name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    project_name = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    
    date = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    fps = serializers.FloatField(required=True)
    min_fps = serializers.FloatField(required=True)
    avg_fps = serializers.FloatField(required=True)
    max_fps  = serializers.FloatField(required=True)
    set_pass_call = serializers.FloatField(required=True)
    draw_call = serializers.FloatField(required=True)
    tris = serializers.FloatField(required=True)
    vertices = serializers.FloatField(required=True)

    total_memory = serializers.FloatField(required=True)
    system_memory = serializers.FloatField(required=True)
    texture_memory = serializers.FloatField(required=True)
    mesh_memory = serializers.FloatField(required=True)

    def create(self, validated_data):
        return ProfileSerializer.objects.create(**validated_data)

    class Meta:
        model = WarningProfileData
        ordering = ['created']
        fields = '__all__'