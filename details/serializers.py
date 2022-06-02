from rest_framework import serializers
from .models import Student, Teacher


class StudentSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField(many=False, read_only=True)
    course = serializers.StringRelatedField(many=False, read_only=True)
    class_room = serializers.StringRelatedField(many=False, read_only=True)

    # marks = ResultStringField(many=False, read_only=True)

    class Meta:
        model = Student
        fields = ['name', 'age', 'marks', 'course', 'class_room', 'teacher']


class TeacherSerializer(serializers.ModelSerializer):
    # students = StudentSerializer(many=True, read_only=True)
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ['name', 'age', 'students']


class StudentListSerializer(serializers.Serializer):
    name = serializers.CharField()


class TeacherListSerializer(serializers.Serializer):
    name = serializers.CharField()

# class ResultStringField(serializers.RelatedField):
#     def to_representation(self, value):
#         if value >= 35:
#             return 'pass'
#         else:
#             return 'fail'
