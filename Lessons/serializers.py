from rest_framework import serializers

from .models import Category, Language, Lesson


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name']
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'content', 'duration', 'quality', 'tags', 'language', 'views', 'category', 'video']
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.content = validated_data.get('content', instance.content)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.quality = validated_data.get('quality', instance.quality)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.language = validated_data.get('language', instance.language)
        instance.views = validated_data.get('views', instance.views)
        instance.category = validated_data.get('category', instance.category)
        instance.video = validated_data.get('video', instance.video)
        instance.save()
        return instance
