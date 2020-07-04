from rest_framework import serializers	
from .models import TrpgSession,SessionUsers,DiceRoll
 
 
class TrpgSessionSerializer(serializers.ModelSerializer):	
    class Meta:
        model = TrpgSession
        fields = ('trpg_session_id','trpg_session_name')	

class SessionUserSerializer(serializers.ModelSerializer):	
    trpg_session_name = serializers.CharField(source = 'trpg_session.trpg_session_name')

    class Meta:
        model = SessionUsers
        fields = ('trpg_session','trpg_session_name','session_user_id','name', 'ticket_no')	


class DiceLogSerializer(serializers.ModelSerializer):	
    user_name = serializers.CharField(source = 'session_users.name')

    class Meta:
        model = DiceRoll
         #動的フィールドfields = ('value','rollUserTicketNo','rollDiceCommand', 'rollDiceResult','isRollDiceResultresulFumble','isRollDiceResultresulCritical','insertDate')	
        fields = ('dice_roll_id'
        ,'session_users'
        ,'twitter_users_photo'
        ,'twitter_users_name'
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
        ,'roll_dice_command'
        )	
    