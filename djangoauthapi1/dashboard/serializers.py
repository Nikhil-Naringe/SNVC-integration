
from rest_framework import serializers
from .models import TestSuite, TestSuiteName

class TestSuiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSuite
        fields = ['id', 'protocol', 'host_ip_address', 'share', 'user_name', 'password', 'log_level', 'sign', 'encrypt', 'trace', 'min_dialect', 'max_dialect']
        read_only_fields = ['id']
        

class TestSuiteNameSerializer(serializers.ModelSerializer):
    test_suite = serializers.SlugRelatedField(slug_field='id', queryset=TestSuite.objects.all())  

    class Meta:
        model = TestSuiteName
        fields = ['id', 'user_name', 'password', 'operating_system', 'suite_name', 'location', 'test_suite', 'ip_address']
        read_only_fields = ['id']



class TestSuiteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSuite
        fields = ['id', 'protocol', 'host_ip_address', 'share', 'user_name', 'password', 'log_level', 'sign', 'encrypt', 'trace', 'min_dialect', 'max_dialect']
        read_only_fields = ['id']


class SuiteNameSerializer(serializers.Serializer):
    suite_name = serializers.CharField(max_length=50, source='get_suite_name_display')


class TestSuiteNameDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSuiteName
        fields = ['suite_name', 'ip_address', 'user_name', 'password']



