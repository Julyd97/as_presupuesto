from rest_framework import serializers
from .models import School

class SchoolSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='auth_user', read_only = True)
    class Meta:
        model = School
        fields = '__all__'

# class ChangeSchoolAttributes(serializers.ModelSerializer):

#     class Meta:
#         model = School
#         fields = '__all__'

#     def update(self, instance, validated_data):
#         instance. update()