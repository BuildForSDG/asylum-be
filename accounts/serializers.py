from rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class UserSerializer(UserDetailsSerializer):
    avatar = serializers.ImageField(source='profile.avatar')
    gender = serializers.CharField(source='profile.gender')
    designation = serializers.CharField(source='profile.designation', write_only=True)
    managed_account = serializers.BooleanField(source='profile.managed_account')
    birth_year = serializers.IntegerField(source='profile.birth_year', write_only=True)
    age = serializers.IntegerField(source='profile.age', read_only=True)
    is_patient = serializers.BooleanField(source='profile.is_patient', read_only=True)

    class Meta(UserDetailsSerializer.Meta):
        """Serializer specification for fields etc."""
        fields = UserDetailsSerializer.Meta.fields + (
            'avatar',
            'gender',
            'designation',
            'managed_account',
            'birth_year',
            'age',
            'is_patient'
        )

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        instance = super(UserSerializer, self).update(instance, validated_data)

        profile = instance.profile
        if profile_data:
            if profile_data.get('avatar'):
                profile.avatar = profile_data.get('avatar')
            if profile_data.get('gender'):
                profile.gender = profile_data.get('gender')
            if profile_data.get('designation'):
                profile.designation = profile_data.get('designation')
            if profile_data.get('managed_account'):
                profile.managed_account = profile_data.get('managed_account')
            if profile_data.get('birth_year'):
                profile.birth_year = profile_data.get('birth_year')

            profile.save()

        return instance
