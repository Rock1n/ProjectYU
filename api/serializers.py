from rest_framework import serializers
from .models import Student


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        # 指定的模型类
        model = Student
        # 需要序列化的属性
        fields = ('pk', 'name', 'sex', 'sid',)
