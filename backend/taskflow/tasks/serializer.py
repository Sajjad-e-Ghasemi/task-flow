from rest_framework.serializers import ModelSerializer
from .models import TaskModel


class TaskSerializer(ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'

    def create(self, validated_data):
        task = TaskModel.objects.create(
            task_title = validated_data['task_title'],
            task_desc = validated_data['task_desc'],
            task_author = validated_data['task_author']
        )
        return task