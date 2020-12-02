from rest_framework import serializers

from django.contrib.auth import get_user_model, authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
        'first_name', 'last_name', 'email', 'password', 'gender', 'citizenship_number', 'current_address',
        'permanent_address', 'username', 'date_joined', 'pk', 'dob')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
            'date_joined': {'read_only': True, },
            'pk': {'read_only': True}
        }


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


class AuthTokenSerializer(serializers.Serializer):
    '''Serializer for user auth object'''
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False  # don't remove the whitespaces
    )

    def validate(self, attrs):
        '''Validate and auth user'''
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            username=email,
            password=password
        )
        if not user:
            msg = 'Unable to authenticate with provided credentials'
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs
