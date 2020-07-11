import django_filters

from rest_framework import viewsets
from .models import TrpgSession,SessionUsers,DiceRoll

from .serializer import TrpgSessionSerializer , SessionUserSerializer,DiceLogSerializer,DiceRollSerializer

class TrpgSessionSet(viewsets.ModelViewSet):
    queryset = TrpgSession.objects.all()
    serializer_class = TrpgSessionSerializer
    class META:
        lookup_field = 'trpg_session_id'

class SessionUserFilter(django_filters.FilterSet):
 
    class Meta:
        model = SessionUsers
        fields = ['name','session_user_id','ticket_no','trpg_session','trpg_session__trpg_session_id']
        
class SessionUserSet(viewsets.ModelViewSet):
    queryset = SessionUsers.objects.all()
    serializer_class = SessionUserSerializer
    filter_class = SessionUserFilter

class DiceRollFilter(django_filters.FilterSet):
    roll_dice_command = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = DiceRoll
        fields = [
            'roll_dice_command',
            'session_users',
            'session_users__trpg_session',
        ]

class DiceLogSet(viewsets.ModelViewSet):
    queryset = DiceRoll.objects.all().order_by('insert_date')
    serializer_class = DiceLogSerializer
    filter_class = DiceRollFilter


class DiceRollSet(viewsets.ModelViewSet):
    queryset = DiceRoll.objects.all()
    serializer_class = DiceRollSerializer

