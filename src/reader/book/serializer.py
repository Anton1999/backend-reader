from rest_framework import serializers

class BookSerializer(serializers.Serializer):
	title = serializers.CharField(max_length=100)
	photo = serializers.ImageField()
	genre = serializers.CharField()

	def create(self, validated_data):
		return Book.objects.create(**validated_data)

class OpenBookSerializer(serializers.Serializer):
	title = serializers.CharField(max_length=100)
	paper_count = serializers.IntegerField()
	rating = serializers.CharField(max_length=50)
	rating_count = serializers.IntegerField()
	status = serializers.CharField(max_length=50)
	category = serializers.IntegerField()
	photo = serializers.ImageField()
	short_description = serializers.CharField()
	
class Rate(serializers.Serializer):
	text_rate = serializers.CharField()
	book = serializers.CharField()
	user = serializers.CharField()