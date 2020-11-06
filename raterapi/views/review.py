"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from raterapi.models import Review, Game, Player


class Reviews(ViewSet):
    """Rater Reviews"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """
        player = Player.objects.get(user=request.auth.user)

        review = Review()
        review.game_id = request.data["game_id"]
        review.player = player
        review.review = request.data["review"]
        
        try:
            review.save()
            serializer = ReviewSerializer(review, context={'request': request})
                                
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)



    def retrieve(self, request, pk=None):
        """Handle GET requests for single review

        Returns:
            Response -- JSON serialized game instance
        """
        try:
            review = Review.objects.get(pk=pk)
            serializer = ReviewSerializer(review, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    # def update(self, request, pk=None):
    #     """Handle PUT requests for a game

    #     Returns:
    #         Response -- Empty body with 204 status code
    #     """
    #     gamer = Gamer.objects.get(user=request.auth.user)

    #     # Do mostly the same thing as POST, but instead of
    #     # creating a new instance of Game, get the game record
    #     # from the database whose primary key is `pk`
    #     game = Game.objects.get(pk=pk)
    #     ggame.title = request.data["title"]
    #     game.designer = request.data["designer"]
    #     game.number_of_players = request.data["number_of_players"]
    #     game.year_released = request.data["year_released"]
    #     game.description = request.data["description"]
    #     game.time_to_play = request.data["time_to_play"]
    #     game.age_recommendation = request.data["age_recommendation"]

    #     game.save()

    #     # 204 status code means everything worked but the
    #     # server is not sending back any data in the response
    #     return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single review

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            review = Review.objects.get(pk=pk)
            review.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Review.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to reviews resource

        Returns:
            Response -- JSON serialized list of reviews
        """
        reviews = Review.objects.all()

        serializer = ReviewSerializer(
            reviews, many=True, context={'request': request})
        return Response(serializer.data)

    

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for reviews

    Arguments:
        serializer type
    """
    class Meta:
        model = Review
        fields = ('id', 'url', 'player_id', 'game_id', 'review')
        depth = 1