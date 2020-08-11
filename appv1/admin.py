from django.contrib import admin
from .models import TrpgSession,SessionUsers,DiceRoll,SessionScene,Memo,ItemMaster,Item

# Register your models here.
class SessionAdmin(admin.ModelAdmin):
   list_display= ('trpg_session_id'
        ,'trpg_session_name'
        ,'trpg_session_outline'
        ,'trpg_session_image'
        ,'trpg_session_bgm'
        )	

class UserAdmin(admin.ModelAdmin):
   list_display=('trpg_session'
      ,'session_user_id'
      ,'name'
      ,'ticket_no'
      ,'character_image'
      ,'character_name'
      ,'character_profile'
      ,'tw_UID'
      ,'tw_name'
      ,'tw_photo'
   )

class DiceLogAdmin(admin.ModelAdmin):
   list_display=(
      'session_users'
      ,'twitter_users_photo'
      ,'twitter_users_name'
      ,'roll_dice_command'
      ,'roll_target'
      ,'roll_dice_result_split'
      ,'roll_dice_result_sum'
      ,'is_roll_daice_suees'
      ,'is_roll_dice_resultresul_fumble'
      ,'is_roll_dice_resultresul_critical'
      ,'insert_date'
  )

class DiceRollAdmin(admin.ModelAdmin):
   list_display=(
        'session_users'
        ,'roll_dice_command'
        ,'roll_target'
  )

class SessionSceneAdmin(admin.ModelAdmin):
   list_display=(
        'session_scene_id'
        ,'trpg_session'
        ,'scene_name'
        ,'scene_no'
        ,'scene_image'
        ,'scene_outline'
        ,'scene_bgm'
)

class MemoAdmin(admin.ModelAdmin):
   list_display=(
        'memo_id'
        ,'session_scene'
        ,'memo_title'
        ,'memo_value'
        ,'memo_image'

)

class ItemMasterAdmin(admin.ModelAdmin):
   list_display=(
        'item_master_id'
        ,'trpg_session'
        ,'item_name'
        ,'item_image'
        ,'item_explanation'
)

class ItemAdmin(admin.ModelAdmin):
   list_display=(
        'item_id'
        ,'item_master'
        ,'item_count'
        ,'item_owner'
)





admin.site.register(TrpgSession, SessionAdmin)
admin.site.register(SessionUsers, UserAdmin)
admin.site.register(DiceRoll, DiceLogAdmin)
admin.site.register(SessionScene, SessionSceneAdmin)
admin.site.register(Memo, MemoAdmin)
admin.site.register(ItemMaster, ItemMasterAdmin)
admin.site.register(Item, ItemAdmin)
