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
        verbose_name ="セッション名"
        verbose_name_plural = "セッション名"
 
    trpg_session_name = models.CharField("セッション名",max_length=255)
    trpg_session_outline = models.CharField("セッション概要",blank=True,max_length=1024)
    trpg_session_image = models.ImageField(upload_to='images',blank=True, null=True)

    def __str__(self):
        return self.trpg_session_name

class SessionUsers(models.Model):
    session_user_id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False)

    class Meta:
        verbose_name ="ユーザー"
        verbose_name_plural = "ユーザー"

    trpg_session = models.ForeignKey(TrpgSession, on_delete=models.CASCADE)	
    name = models.CharField("ユーザー名",max_length=255)
    ticket_no = models.CharField("チケットNO",max_length=8)
    character_image = models.ImageField(upload_to='images',blank=True, null=True)
    character_name = models.CharField("キャラ名",max_length=255)
    character_profile = models.CharField("キャラプロフィール",max_length=255)

    def __str__(self):
        return self.name

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
    roll_dice_command = models.CharField(max_length=255)
    roll_target= models.CharField(max_length=255,blank=True)
    roll_dice_result_split = models.CharField(blank=True,max_length=8)
    roll_dice_result_sum = models.CharField(blank=True,max_length=8)
    is_roll_daice_suees  =  models.BooleanField(default=False,blank=True)
    is_roll_dice_resultresul_fumble =  models.BooleanField(default=False,blank=True)
    is_roll_dice_resultresul_critical =  models.BooleanField(default=False,blank=True)
    insert_date    = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
     return self.roll_dice_command

    #
    def save(self, **kwargs):

        diceComand  =self.roll_dice_command.split(sep="d")
        if diceComand[0].isdecimal() and diceComand[0].isdecimal():
            num = int(diceComand[0])
            if num  < 0:num  = num *-1

            face  = int(diceComand[1])
            if face < 0:face = face *-1
            if face == 0:face = 1
            sum = 0    
            for i in range(0,num):
               sum = sum +random.randrange(1,face)

            self.roll_dice_result_sum = str(sum)
            logger.debug("debugメッセージ")
    
        super(DiceRoll, self).save(**kwargs)
