from rest_framework import serializers

from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'gender', 'citizenship_number', 'current_address', 'permanent_address', 'username')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}


    def create(self, validated_data):
        '''Create new user with encrypted data and returns it'''
        print(validated_data)
        return get_user_model().objects.create(**validated_data)

    def update(self, instance, validated_data):
        '''Update the user credentials
            Steps: `Remove password using pop
                    `call super for using default one along with the one we created
                    `set password of user
                    `sava the user
        '''
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user
