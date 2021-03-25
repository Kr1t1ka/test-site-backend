from rest_framework import serializers

from .models import Question, Answer, User, Steps


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    # answer = AnswerSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = '__all__'


class StepsSerializer(serializers.ModelSerializer):
    # answer = AnswerSerializer(read_only=True, many=True)

    class Meta:
        model = Steps
        fields = '__all__'
