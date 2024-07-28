from rest_framework import serializers

from .models import SimpleUser, User, Account, History, HiddenHistory, PDFHistory, SavedLesson


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(max_length=16, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'password', 'first_name', 'last_name', 'username', 'used', 'status']

    # def create(self, validated_data):
    #     user = super().create(self.validated_data)
    #     user.set_password(validated_data.pop('password', None))
    #     user.save()
    #     return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.used = validated_data.get('used', instance.used)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'user', 'telegram_id']

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.telegram_id = validated_data.get('telegram_id', instance.telegram_id)
        instance.save()
        return instance


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleUser
        fields = ['id', 'first_name', 'last_name', 'username', 'telegram_id', 'used']

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.telegram_id = validated_data.get('telegram_id', instance.telegram_id)
        instance.used = validated_data.get('used', instance.used)
        instance.save()
        return instance


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['id', 'user', 'code']


class HiddenHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HiddenHistory
        fields = ['id', 'user', 'text']


class PDFHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFHistory
        fields = ['id', 'user', 'image', 'file']


class SavedLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedLesson
        fields = ['id', 'user', 'lesson']
    
    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.lesson = validated_data.get('lesson', instance.lesson)
        instance.save()
        return instance
