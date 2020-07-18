from rest_framework import serializers	
from .models import TrpgSession,SessionUsers,DiceRoll
 
 
class TrpgSessionSerializer(serializers.ModelSerializer):	
    class Meta:
        model = TrpgSession
        fields = ('trpg_session_id'
        ,'trpg_session_name'
        ,'trpg_session_outline'
        ,'trpg_session_image'
        )	

class SessionUserSerializer(serializers.ModelSerializer):	
    trpg_session_name = serializers.CharField(source = 'trpg_session.trpg_session_name')

    class Meta:
        model = SessionUsers
        fields = ('trpg_session'
        ,'trpg_session_name'
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
    