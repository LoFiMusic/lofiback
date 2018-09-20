from rest_framework import serializers
from api.models import Music

#Проверка данных постов
class MusicSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=False)
        title = serializers.CharField(required=False)
        artist = serializers.CharField(required=False)
        src = serializers.FileField(required=False)
        pic = serializers.ImageField(required=False)
        likes = serializers.IntegerField(required=False)
        duration = serializers.IntegerField(required=False)


        def update(self, instance, validated_data):
            instance.id = validated_data.get('id', instance.id)
            instance.name = validated_data.get('title', instance.head)
            instance.author = validated_data.get('artist', instance.body)
            instance.dateCreate = validated_data.get('dateCreate', instance.url)
            instance.category = validated_data.get('music_file', instance.enable_passwd)
            instance.music_file = validated_data.get('src', instance.password)
            instance.cover  = validated_data.get('pic', instance.category)
            instance.likes = validated_data.get('likes', instance.likes)
            instance.duration = validated_data.get('duration', instance.duration)
            instance.save()
            return instance
