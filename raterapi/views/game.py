"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from raterapi.models import Game
from raterapi.models import GameCategory


class Games(ViewSet):
    """Level up games"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """
        game = Game()
        game.title = request.data["title"]
        game.designer = request.data["designer"]
        game.number_of_players = request.data["number_of_players"]
        game.year_released = request.data["year_released"]
        game.description = request.data["description"]
        game.time_to_play = request.data["time_to_play"]
        game.age_recommendation = request.data["age_recommendation"]
        game.selected_categories = request.data["selected_categories"]
        

        try:
            game.save()
            serializer = GameSerializer(game, context={'request': request})

            #iterate selected categories and save to database
            for category in game.selected_categories:

                gamecategory = GameCategory()
                gamecategory.category_id = int(category["id"])
                gamecategory.game_id = int(serializer.data["id"])
                
                gamecategory.save()
                                
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)



    def retrieve(self, request, pk=None):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game instance
        """
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        gamer = Gamer.objects.get(user=request.auth.user)

        # Do mostly the same thing as POST, but instead of
        # creating a new instance of Game, get the game record
        # from the database whose primary key is `pk`
        game = Game.objects.get(pk=pk)
        ggame.title = request.data["title"]
        game.designer = request.data["designer"]
        game.number_of_players = request.data["number_of_players"]
        game.year_released = request.data["year_released"]
        game.description = request.data["description"]
        game.time_to_play = request.data["time_to_play"]
        game.age_recommendation = request.data["age_recommendation"]

        game.save()

        # 204 status code means everything worked but the
        # server is not sending back any data in the response
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            game = Game.objects.get(pk=pk)
            game.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to games resource

        Returns:
            Response -- JSON serialized list of games
        """
        games = Game.objects.all()

        serializer = GameSerializer(
            games, many=True, context={'request': request})
        return Response(serializer.data)



class GameSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for games

    Arguments:
        serializer type
    """
    class Meta:
        model = Game
        url = serializers.HyperlinkedIdentityField(
            view_name='game',
            lookup_field='id'
        )
        fields = ('id', 'url', 'title', 'description', 'designer', 'year_released', 'number_of_players', 'time_to_play', 'age_recommendation')
        depth = 1