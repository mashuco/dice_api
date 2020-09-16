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
    character_name= serializers.CharField()
    character_profile= serializers.CharField()
  
    class Meta:
        model = SessionUsers
        fields = (
            'session_user_id'
            ,'character_image'
            ,'character_name'
            ,'character_profile'
        )

    def validate_character_name(self, character_name):
        if not(len(character_name) <=20):
            raise serializers.ValidationError('キャラクター名は20文字までです')
        return character_name

    def validate_character_profile(self, character_profile):
        if not(len(character_profile) <=201):
            raise serializers.ValidationError('プロフィールは名は200文字までです')
        return character_profile


class SessionUserTWUpdateSerializer(serializers.ModelSerializer):
    tw_UID= serializers.CharField(blank=True)	
    tw_name= serializers.CharField(blank=True)	
    class Meta:
        model = SessionUsers
        fields = (
        'session_user_id'
        ,'tw_UID'
        ,'tw_name'
        ,'tw_photo'
        )	

    def validate_tw_UID(self, tw_UID):
        if not(len(tw_UID) <=28):
            raise serializers.ValidationError('不正なTwitterIDです')
        return tw_UID

    def validate_tw_name(self, tw_name):
        if not(len(tw_name) <=15):
            raise serializers.ValidationError('不正なTwitterIDです')
        return tw_name


class DiceLogSerializer(serializers.ModelSerializer):	
    user_name = serializers.CharField(source = 'session_users.name')
    character_image = serializers.ImageField(source = 'session_users.character_image')
    character_name = serializers.CharField(source = 'session_users.character_name')
    character_profile = serializers.CharField(source = 'session_users.character_profile')

    class Meta:
        model = DiceRoll
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




    