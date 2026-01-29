from rest_framework.serializers import ModelSerializer
from .models import TaskModel


class TaskSerializer(ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'
        read_only_field = ('owner', )
        extra_kwargs = {
            'owner': {'required': False}  
        }

    def create(self, validated_data):
        task = TaskModel.objects.create(
            owner = self.context['request'].user,
            task_title = validated_data['task_title'],
            task_desc = validated_data['task_desc'],
        )
        return task