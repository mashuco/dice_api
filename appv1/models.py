from django.db import models
import uuid as uuid_lib
import random
from logging import getLogger, StreamHandler, DEBUG
import re

logger = getLogger(__name__)


# Create your models here.

class TrpgSession(models.Model):
    trpg_session_id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False)

    class Meta:
        verbose_name ="セッション"
        verbose_name_plural = "セッション"
 
    trpg_session_name = models.CharField("セッション名",max_length=255)
    trpg_session_outline = models.TextField("セッション概要",blank=True,max_length=5000)
    trpg_session_image = models.ImageField(upload_to='images',blank=True, null=True)
    trpg_session_bgm = models.FileField (upload_to='bgm',blank=True, null=True)

    def __str__(self):
        return self.trpg_session_name

class SessionScene(models.Model):
    session_scene_id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid_lib.uuid4,
        editable=True)

    class Meta:
        verbose_name ="シーン"
        verbose_name_plural = "シーン"

    trpg_session = models.ForeignKey(TrpgSession, on_delete=models.CASCADE)	
    scene_name = models.CharField("シーン名",max_length=255)
    scene_no = models.CharField("シーンNO",max_length=8)
    scene_image = models.ImageField(upload_to='images',blank=True, null=True)
    scene_outline = models.TextField("シーン概要",blank=True,max_length=5000)
    scene_bgm = models.FileField (upload_to='bgm',blank=True, null=True)

    def __str__(self):
        return self.scene_name


class SessionUsers(models.Model):
    session_user_id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid_lib.uuid4,
        editable=True)

    class Meta:
        verbose_name ="ユーザー"
        verbose_name_plural = "ユーザー"

    trpg_session = models.ForeignKey(TrpgSession, on_delete=models.CASCADE)	
    name = models.CharField("ユーザー名",max_length=255)
    ticket_no = models.CharField("チケットNO",max_length=12, unique=True)
    character_image = models.ImageField(upload_to='images',blank=True, null=True)
    character_name = models.CharField("キャラ名",max_length=255)
    character_profile = models.TextField("キャラプロフィール",max_length=2000)
    tw_UID   = models.CharField("twetter UID",blank=True,max_length=50)
    tw_name  = models.CharField("twetter Name",blank=True,max_length=50)
    tw_photo = models.CharField("twetter Photo",blank=True,max_length=255)

    def __str__(self):
        return self.name

class Memo(models.Model):
    memo_id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid_lib.uuid4,
        editable=True)

    class Meta:
        verbose_name ="メモ"
        verbose_name_plural = "メモ"

    session_scene = models.ForeignKey(SessionScene, on_delete=models.CASCADE)
    memo_title = models.CharField("メモタイトル",max_length=255)
    memo_value = models.TextField("メモ",max_length=2000)
    memo_image = models.ImageField(upload_to='images',blank=True, null=True)

    def __str__(self):
        return self.memo_title

class ItemMaster(models.Model):
    item_master_id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid_lib.uuid4,
        editable=True)

    class Meta:
        verbose_name ="アイテムマスタ"
        verbose_name_plural = "アイテムマスタ"

    trpg_session = models.ForeignKey(TrpgSession, on_delete=models.CASCADE)	
    item_name = models.CharField("アイテム名",blank=True,max_length=255)
    item_image = models.ImageField(upload_to='images',blank=True, null=True)
    item_explanation= models.TextField("アイテム説明",blank=True,max_length=5000)
 
    def __str__(self):
        return self.item_name

class Item(models.Model):
    item_id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid_lib.uuid4,
        editable=True)

    class Meta:
        verbose_name ="アイテム"
        verbose_name_plural = "アイテム"

    item_master = models.ForeignKey(ItemMaster, on_delete=models.CASCADE)	
    item_count = models.IntegerField("数")
    #owner = models.CharField("所有者",max_length=255)
    item_owner = models.ForeignKey(SessionUsers, blank=True,on_delete=models.CASCADE)	


    #def __str__(self):
        #return self.item_id


class DiceRoll(models.Model):
    dice_roll_id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False)

    class Meta:
        verbose_name ="ダイスログ"
        verbose_name_plural = "ダイスログ"
    session_users = models.ForeignKey(SessionUsers, on_delete=models.CASCADE)	
    twitter_users_photo = models.CharField(blank=True,max_length=255)
    twitter_users_name = models.CharField(blank=True,max_length=255)
    roll_dice_command = models.TextField(max_length=2000)
    roll_target= models.CharField(max_length=255,blank=True)
    roll_dice_result_split = models.CharField(blank=True,max_length=255)
    roll_dice_result_sum = models.CharField(blank=True,max_length=8)
    is_roll_daice_suees  =  models.BooleanField(blank=True,null=True)
    is_roll_dice_resultresul_fumble =  models.BooleanField(default=False,blank=True)
    is_roll_dice_resultresul_critical =  models.BooleanField(default=False,blank=True)
    insert_date    = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
     return self.roll_dice_command

    def save(self, **kwargs):
 
        pattern_dice_command  = '\d{1,2}(d|D)\d{1,3}'
        pattern_dice_command_with_judgment = '\d{1,2}(d|D)\d{1,3}(>|=>|>=|<|=<|<=)\d{1,3}'

        repatter_dice_command = re.compile(pattern_dice_command)
        repatter_dice_command_with_judgment = re.compile(pattern_dice_command_with_judgment)
        
        #non dice comannd############################
        if repatter_dice_command.fullmatch(self.roll_dice_command) is None:
            if repatter_dice_command_with_judgment.fullmatch(self.roll_dice_command) is None:
                super(DiceRoll, self).save(**kwargs)
                return

        #is_dice_command############################
        splitter=''
        inequality_sign = ''
        dice_face  = 4
        dice_count = 1
        target     = 1

        if repatter_dice_command.fullmatch(self.roll_dice_command):
            splitter = repatter_dice_command.split(self.roll_dice_command)[1]
            dice_face  = int(self.roll_dice_command.split(sep=splitter)[1])
            dice_count = int(self.roll_dice_command.split(sep=splitter)[0])

        if repatter_dice_command_with_judgment.fullmatch(self.roll_dice_command):
            splitter = repatter_dice_command_with_judgment.split(self.roll_dice_command)[1]
            inequality_sign = repatter_dice_command_with_judgment.split(self.roll_dice_command)[2]
            dice_count  = int(self.roll_dice_command.split(sep=splitter)[0])
            dice_face  = int(self.roll_dice_command.split(sep=inequality_sign)[0].split(sep=splitter)[1])
            target = int(self.roll_dice_command.split(sep=inequality_sign)[1])

        if dice_face < 0:dice_face = dice_face *-1
        if dice_face == 0:dice_face = 1

        sum = 0    
        result =''
        resultArr =[]
        for i in range(0,dice_count):
            result = random.randint(1,dice_face)
            sum = sum +result
            resultArr.append(result)

        self.roll_dice_result_sum = str(sum)
        self.roll_dice_result_split = resultArr

        #need judgment
        if inequality_sign == '':
            super(DiceRoll, self).save(**kwargs)
            return

        roll_daice_suees = True
        if inequality_sign == '<':
            roll_daice_suees = (sum < target)            
        elif inequality_sign == '=<' or inequality_sign == '<=' :
            roll_daice_suees = (sum <= target)            
        elif inequality_sign is '>':
            roll_daice_suees = (sum > target)            
        elif inequality_sign == '=>' or inequality_sign == '>='  :
            roll_daice_suees = (sum >= target)            

        self.is_roll_daice_suees = roll_daice_suees
        super(DiceRoll, self).save(**kwargs)
