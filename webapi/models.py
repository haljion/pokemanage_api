from django.db import models
from django.core.validators import MinValueValidator #マイナス値を弾く
import uuid #idを連番にしない


class Pokemon(models.Model):
    """ポケモン"""
    id = models.AutoField(primary_key=True)
    name = models.CharField("種族名", max_length=50)
    image = models.CharField("画像", max_length=50)
    type1 = models.CharField("タイプ1", max_length=10)
    type2 = models.CharField("タイプ2", max_length=10, blank=True, null=True)
    ability1 = models.CharField("特性1", max_length=20)
    ability2 = models.CharField("特性2", max_length=20, blank=True, null=True)
    hidden_ability = models.CharField("隠れ特性", max_length=20, blank=True, null=True)
    # 0: 性別あり, 1: 性別なし
    gender_flag = models.IntegerField("性別有無", validators=[MinValueValidator(0)])
    varioustaH = models.IntegerField("種族値H", validators=[MinValueValidator(0)])
    varioustaA = models.IntegerField("種族値A", validators=[MinValueValidator(0)])
    varioustaB = models.IntegerField("種族値B", validators=[MinValueValidator(0)])
    varioustaC = models.IntegerField("種族値C", validators=[MinValueValidator(0)])
    varioustaD = models.IntegerField("種族値D", validators=[MinValueValidator(0)])
    varioustaS = models.IntegerField("種族値S", validators=[MinValueValidator(0)])
    
    def __str__(self):
        return self.name


class Item(models.Model):
    """持ち物"""
    id = models.AutoField(primary_key=True)
    name = models.CharField("アイテム名", max_length=50)
    image = models.CharField("画像", max_length=50)
    
    def __str__(self):
        return self.name


class Ball(models.Model):
    """ボール"""
    id = models.AutoField(primary_key=True)
    name = models.CharField("ボール名", max_length=50)
    image = models.CharField("画像", max_length=50)
    
    def __str__(self):
        return self.name


class Personality(models.Model):
    """性格"""
    id = models.AutoField(primary_key=True)
    name = models.CharField("性格名", max_length=10)
    # 0 :A, 1: B,... 4 :S, 5: なし
    up = models.IntegerField("上昇値")
    down = models.IntegerField("下降値")

    def __str__(self):
        return self.name


class Waza(models.Model):
    """技"""
    id = models.AutoField(primary_key=True)
    name = models.CharField("わざ名", max_length=10)
    waza_type = models.CharField("タイプ", max_length=10)
    # 0 :物理, 1: 特殊, 2 :変化
    various = models.IntegerField("種類")
    
    def __str__(self):
        return self.name


class UserPoke(models.Model):
    """育成個体"""
    id = models.AutoField(primary_key=True)
    user_id = models.CharField("ユーザーID", max_length=300)
    pokemon = models.ForeignKey(Pokemon, related_name='user_pokes', on_delete=models.CASCADE)
    nickname = models.CharField("ニックネーム", max_length=10, blank=True)
    gender = models.IntegerField(validators=[MinValueValidator(0)])
    ball = models.ForeignKey(Ball, related_name='user_pokes', on_delete=models.CASCADE)
    color = models.IntegerField(validators=[MinValueValidator(0)])
    ability = models.CharField("特性", max_length=20)
    personality = models.ForeignKey(Personality, related_name='user_pokes', on_delete=models.CASCADE)
    individual_value_h = models.IntegerField(validators=[MinValueValidator(0)])
    individual_value_a = models.IntegerField(validators=[MinValueValidator(0)])
    individual_value_b = models.IntegerField(validators=[MinValueValidator(0)])
    individual_value_c = models.IntegerField(validators=[MinValueValidator(0)])
    individual_value_d = models.IntegerField(validators=[MinValueValidator(0)])
    individual_value_s = models.IntegerField(validators=[MinValueValidator(0)])
    effort_value_h = models.IntegerField(validators=[MinValueValidator(0)])
    effort_value_a = models.IntegerField(validators=[MinValueValidator(0)])
    effort_value_b = models.IntegerField(validators=[MinValueValidator(0)])
    effort_value_c = models.IntegerField(validators=[MinValueValidator(0)])
    effort_value_d = models.IntegerField(validators=[MinValueValidator(0)])
    effort_value_s = models.IntegerField(validators=[MinValueValidator(0)])
    waza1 = models.ForeignKey(Waza, related_name='user_pokes_1', on_delete=models.CASCADE)
    waza2 = models.ForeignKey(Waza, related_name='user_pokes_2', blank=True, on_delete=models.CASCADE)
    waza3 = models.ForeignKey(Waza, related_name='user_pokes_3', blank=True, on_delete=models.CASCADE)
    waza4 = models.ForeignKey(Waza, related_name='user_pokes_4', blank=True, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='user_pokes', blank=True, on_delete=models.CASCADE)
    remarks = models.CharField("備考", max_length=300, blank=True)
    def __str__(self):
        return f'{self.pokemon}, {self.nickname}'
