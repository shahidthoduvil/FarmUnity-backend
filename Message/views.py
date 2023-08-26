from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView,CreateAPIView,DestroyAPIView,ListAPIView,ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Question,Solution,Notification
from .serializer import QuestionSerializer, SolutionSerializer,CreateQuestionSerializer,createSolutionSerializer, NotificationSerializer,CreateNotificationSerializer


class QuestionListView(APIView):
    def get(self, request):
        questions = Question.objects.all().order_by('-id')
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

# class QuestionDetailView(APIView):
#     def get(self, request, question_id):
#         try:
#             question = Question.objects.get(pk=question_id)
#         except Question.DoesNotExist:
#             return Response({"error": "Question not found."}, status=status.HTTP_404_NOT_FOUND)

#         serializer = QuestionSerializer(question)
#         return Response(serializer.data, status=status.HTTP_200_OK)
class SolutionListView(APIView):
    def get(self, request, question_id):
        solutions = Solution.objects.filter(quest=question_id).order_by('-id')
        serializer = SolutionSerializer(solutions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class CreateQuestionView(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = CreateQuestionSerializer



class CreateAnswerView(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = createSolutionSerializer



class DeleteQuestionView(APIView):
    def delete(self, request, question_id):
        try:
            question = Question.objects.get(id=question_id)
            question.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Question.DoesNotExist:
            return Response({'error': 'Question not found'}, status=status.HTTP_404_NOT_FOUND)


class DeleteSolutionView(APIView):
    
    def delete(self, request,solution_id):
        try:
            solution = Solution.objects.get(id=solution_id)                             
            solution.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Solution.DoesNotExist:
                return Response({'error': 'Solution not found'}, status=status.HTTP_404_NOT_FOUND)

                                                
                                                    

class NotificationListView(ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
                user_id = self.kwargs['user_id']
                return Notification.objects.filter(user_id=user_id).order_by('-date')
    

class AdminNotificationCreateView(CreateAPIView):
    serializer_class = CreateNotificationSerializer
    queryset=Notification.objects.all()



class DeleteNotificationAPIView(DestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    lookup_field='id'




class UserNotificationListView(ListAPIView):
   queryset=Notification.objects.all().order_by('-date')
   serializer_class = NotificationSerializer


