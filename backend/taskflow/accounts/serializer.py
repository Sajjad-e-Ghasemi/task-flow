from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

Account = get_user_model()

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Account.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password']
        )
        return user