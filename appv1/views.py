import django_filters
from rest_framework import viewsets
from .models import TrpgSession,SessionUsers,DiceRoll,SessionScene,Memo,ItemMaster,Item
from .serializer import TrpgSessionSerializer , SessionUserSerializer,DiceLogSerializer,DiceRollSerializer,SessionUserTWUpdateSerializer,SessionUserUpdateSerializer,SessionSceneSerializer,MemoSerializer,ItemMasterSerializer,ItemSerializer


class TrpgSessionFilter(django_filters.FilterSet):
 
    class Meta:
        model = TrpgSession
        fields = [ 'trpg_session_id'
        ,'trpg_session_name'
        ,'trpg_session_outline'
        	]

class TrpgSessionSet(viewsets.ModelViewSet):
    queryset = TrpgSession.objects.all()
    serializer_class = TrpgSessionSerializer
    filter_class = TrpgSessionFilter
    class META:
        lookup_field = 'trpg_session_id'

class SessionUserFilter(django_filters.FilterSet):
 
    class Meta:
        model = SessionUsers
        fields = [
            'name'
            ,'session_user_id'
            ,'ticket_no'
            ,'trpg_session'
            ,'trpg_session__trpg_session_id'
            ,'tw_UID'
        ]
        
class SessionUserSet(viewsets.ModelViewSet):
    queryset = SessionUsers.objects.all()
    serializer_class = SessionUserSerializer
    filter_class = SessionUserFilter

class SessionUserTWUpdateSet(viewsets.ModelViewSet):
    queryset = SessionUsers.objects.all()
    serializer_class = SessionUserTWUpdateSerializer


class SessionUserUpdateSet(viewsets.ModelViewSet):
    queryset = SessionUsers.objects.all()
    serializer_class = SessionUserUpdateSerializer

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


class SceneFilter(django_filters.FilterSet):
    class Meta:
        model = SessionScene
        fields = [
            'session_scene_id',
            'trpg_session'
        ]

class SessionSceneSet(viewsets.ModelViewSet):
    #queryset = SessionScene.objects.all()
    queryset = SessionScene.objects.order_by('scene_no')
    serializer_class = SessionSceneSerializer
    filter_class = SceneFilter

class memoFilter(django_filters.FilterSet):
    class Meta:
        model = Memo
        fields = [
            'session_scene',
            'session_scene__trpg_session',
        ]

class MemoSet(viewsets.ModelViewSet):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer
    filter_class = memoFilter

class ItemMasterSet(viewsets.ModelViewSet):
    queryset = ItemMaster.objects.all()
    serializer_class = ItemMasterSerializer

class itemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = [
            'item_owner'
        ]

class ItemSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_class = itemFilter

