from rest_framework import serializers
# class Book(APIView):
#     title = serializers.CharField(max_length=100)
# 	photo = serializers.ImageField()
# 	genre = serializers.CharField()

class Book(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    photo = serializers.ImageField()
    genre = serializers.CharField()

class ProfileSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=30)
    email = serializers.EmailField()

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)

        instance.save()
        return instance
