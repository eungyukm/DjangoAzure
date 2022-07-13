from rest_framework import serializers
from user_app.models import UserTable


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
        instance.save()
        return instance

    class Meta:
        model = UserTable
        ordering = ['created']
        fields = '__all__'
