from rest_framework import serializers
from .models import TrpgSession,SessionUsers,DiceRoll,SessionScene,Memo,ItemMaster,Item
 
 
class TrpgSessionSerializer(serializers.ModelSerializer):	
    #trpg_session_image = serializers.ImageField(max_length=None,use_url=True)
    #trpg_session_bgm = serializers.FileField(max_length=None,use_url=True)

    class Meta:
        model = TrpgSession
        fields = ('trpg_session_id'
        ,'trpg_session_name'
        ,'trpg_session_outline'
        ,'trpg_session_now_scene'
        ,'firebase_message_key_id'
        ,'firebase_scean_key_id'
        )	


class SessionUserSerializer(serializers.ModelSerializer):	
    trpg_session_name = serializers.CharField(source = 'trpg_session.trpg_session_name')

    class Meta:
        model = SessionUsers
        fields = (
        'trpg_session'
        ,'trpg_session_name'
        ,'session_user_id'
        ,'name'
        ,'is_session_master'
        , 'ticket_no'
        ,'character_image'
        ,'character_name'
        ,'character_profile'
        ,'tw_UID'
        ,'tw_name'
        ,'tw_photo'
        )	

class SessionUserUpdateSerializer(serializers.ModelSerializer):	
     character_image = serializers.ImageField(max_length=None,use_url=True)
  
     class Meta:
        model = SessionUsers
        fields = (
        'trpg_session'
        ,'session_user_id'
        ,'name'
        , 'ticket_no'
        ,'character_image'
        ,'character_name'
        ,'character_profile'
        ,'tw_UID'
        ,'tw_name'
        ,'tw_photo'
        )	


class SessionUserTWUpdateSerializer(serializers.ModelSerializer):	
    class Meta:
        model = SessionUsers
        fields = (
        'session_user_id'
        ,'tw_UID'
        ,'tw_name'
        ,'tw_photo'
        )	


class DiceLogSerializer(serializers.ModelSerializer):	
    user_name = serializers.CharField(source = 'session_users.name')
    character_image = serializers.ImageField(source = 'session_users.character_image')
    character_name = serializers.CharField(source = 'session_users.character_name')
    character_profile = serializers.CharField(source = 'session_users.character_profile')

    class Meta:
        model = DiceRoll
         #動的フィールドfields = ('value','rollUserTicketNo','rollDiceCommand', 'rollDiceResult','isRollDiceResultresulFumble','isRollDiceResultresulCritical','insertDate')	
        fields = ('dice_roll_id'
        ,'session_users'
        ,'twitter_users_photo'
        ,'twitter_users_name'
        ,'character_image'
        ,'character_name'
        ,'character_profile'
        ,'user_name'
        ,'roll_dice_command'
        ,'roll_target'
        ,'roll_dice_result_split'
        ,'roll_dice_result_sum'
        ,'is_roll_daice_suees'
        ,'is_roll_dice_resultresul_fumble'
        ,'is_roll_dice_resultresul_critical'        
        ,'insert_date'
        )	
    
    #動的フィールドdef get_value(self, obj):
    #    return obj.hoge()

class DiceRollSerializer(serializers.ModelSerializer):	
    
    class Meta:
        model = DiceRoll
        fields = (
        'session_users'
        ,'twitter_users_photo'
        ,'twitter_users_name'
        ,'roll_dice_command'
        )	

class SessionSceneSerializer(serializers.ModelSerializer):	
    scene_image = serializers.ImageField(max_length=None,use_url=True)
    scene_bgm = serializers.FileField(max_length=None,use_url=True)

    class Meta:
        model = SessionScene
        fields = (
        'session_scene_id'
        ,'trpg_session'
        ,'scene_name'
        ,'scene_no'
        ,'scene_image'
        ,'scene_outline'
        ,'scene_bgm'
        )	


class MemoSerializer(serializers.ModelSerializer):	
    memo_image = serializers.ImageField(max_length=None,use_url=True)

    class Meta:
        model = Memo
        fields = (
        'memo_id'
        ,'session_scene'
        ,'memo_title'
        ,'memo_value'
        ,'memo_image'
        )	

        
class ItemMasterSerializer(serializers.ModelSerializer):
    item_image = serializers.ImageField(max_length=None,use_url=True)
	
    class Meta:
        model = ItemMaster
        fields = (
        'item_master_id'
        ,'trpg_session'
        ,'sessitem_name'
        ,'item_name'
        ,'item_image'
        ,'item_explanation'
        )	

        
class ItemSerializer(serializers.ModelSerializer):	
    item_name = serializers.CharField(source = 'item_master.item_name')
    item_image = serializers.ImageField(source = 'item_master.item_image')
    item_explanation = serializers.CharField(source = 'item_master.item_explanation')
 
    class Meta:
        model = Item
        fields = (
        'item_id'
        ,'item_count'
        ,'item_owner'
        ,'item_master'
        ,'item_name'
        ,'item_image'
        ,'item_explanation'
        )	




    