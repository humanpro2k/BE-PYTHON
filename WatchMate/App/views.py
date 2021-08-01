from django.shortcuts import get_object_or_404

from App.models import WatchList, StreamPlatForm, Review
from .serializers import WatchListSerializer, StreamPlatFormSerializer, ReviewSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, generics


class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        Review.objects.filter(watchlist=pk)


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        serializer.save(watchlist=watchlist)

# class ReviewList(generics.ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class StreamPlatFormAV(APIView):

    def get(self, request):
        movies = StreamPlatForm.objects.all()
        serializers = StreamPlatFormSerializer(movies, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = StreamPlatFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class StreamPlatFormDetailAV(APIView):

    def get(self, request, pk):
        try:
            platform = StreamPlatForm.objects.get(pk=pk)
        except StreamPlatForm.DoesNotExist:
            return Response({
                'error': 'Platform not found'
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(platform)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            platform = StreamPlatForm.objects.get(pk=pk)
            serializer = StreamPlatFormSerializer(platform, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except StreamPlatFormSerializer.DoesNotExist:
            return Response({
                'error': 'Movie not found'
            }, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            platform = StreamPlatForm.objects.get(pk=pk)
        except StreamPlatForm.DoesNotExist:
            return Response({
                'error': 'Movie not found'
            }, status=status.HTTP_404_NOT_FOUND)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serializers = WatchListSerializer(movies, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class WatchDetailAV(APIView):

    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({
                'error': 'Movie not found'
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
            serializer = WatchListSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except WatchList.DoesNotExist:
            return Response({
                'error': 'Movie not found'
            }, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({
                'error': 'Movie not found'
            }, status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatformVS(viewsets.ViewSet):

    def list(self, request):
        queryset = StreamPlatForm.objects.all()
        serializer = StreamPlatFormSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = StreamPlatForm.objects.all()
        stream = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatFormSerializer(stream)
        return Response(serializer.data)

    def create(self, request):
        serializer = StreamPlatFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)