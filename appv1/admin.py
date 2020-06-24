from django.contrib import admin
from .models import TrpgSession,SessionUsers,DiceRoll

# Register your models here.
class SessionAdmin(admin.ModelAdmin):
   #list_display=('pk','trpg_session_name', 'trpg_session_code','user_auth')
   list_display=('trpg_session_id','trpg_session_name')

class UserAdmin(admin.ModelAdmin):
   list_display=('trpg_session','session_user_id','name', 'ticket_no')

class DiceLogAdmin(admin.ModelAdmin):
   list_display=(
      'session_users',
      'roll_dice_command',
      'roll_target',
      'roll_dice_result_split',
      'roll_dice_result_sum',
      'is_roll_daice_suees',
      'is_roll_dice_resultresul_fumble',
      'is_roll_dice_resultresul_critical',
      'insert_date'
  )

class DiceRollAdmin(admin.ModelAdmin):
   list_display=(
        'session_users'
        ,'roll_dice_command'
        ,'roll_target'
  )


admin.site.register(TrpgSession, SessionAdmin)
admin.site.register(SessionUsers, UserAdmin)
admin.site.register(DiceRoll, DiceLogAdmin)
