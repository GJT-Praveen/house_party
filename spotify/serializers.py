from rest_framework import serializers
from .models import Song

class QueueSongSerializer(serializers.ModelSerializer):
    # uri=serializers.CharField(validators=[])
    class Meta:
        model=Song
        fields=('uri','room_code')

