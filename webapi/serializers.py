# todos/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Pokemon, Item, Ball, Personality, Waza, UserPoke


class PokemonSerializer(serializers.ModelSerializer):
    """ポケモン"""
    class Meta:
        model = Pokemon
        fields = (
            "id", 
            "name", 
            "image", 
            "type1", 
            "type2", 
            "ability1", 
            "ability2", 
            "hidden_ability", 
            "gender_flag", 
            "varioustaH", 
            "varioustaA", 
            "varioustaB", 
            "varioustaC", 
            "varioustaD", 
            "varioustaS", 
            )


class ItemSerializer(serializers.ModelSerializer):
    """持ち物"""
    class Meta:
        model = Item
        fields = (
            "id", 
            "name", 
            "image", 
            )


class BallSerializer(serializers.ModelSerializer):
    """ボール"""
    class Meta:
        model = Ball
        fields = (
            "id", 
            "name", 
            "image", 
            )


class PersonalitySerializer(serializers.ModelSerializer):
    """性格"""
    class Meta:
        model = Personality
        fields = (
            "id", 
            "name", 
            "up", 
            "down", 
            )


class WazaSerializer(serializers.ModelSerializer):
    """技"""
    class Meta:
        model = Waza
        fields = (
            "id", 
            "name", 
            "waza_type", 
            "various", 
            )


class UserPokeSerializer(serializers.ModelSerializer):
    """育成個体"""
    # GET
    pokemon = PokemonSerializer(read_only=True)
    ball = BallSerializer(read_only=True)
    personality = PersonalitySerializer(read_only=True)
    item = ItemSerializer(read_only=True)
    waza1 = WazaSerializer(read_only=True)
    waza2 = WazaSerializer(read_only=True)
    waza3 = WazaSerializer(read_only=True)
    waza4 = WazaSerializer(read_only=True)
    # POST
    pokemon_id = serializers.PrimaryKeyRelatedField(queryset=Pokemon.objects.all(), write_only=True)
    ball_id = serializers.PrimaryKeyRelatedField(queryset=Ball.objects.all(), write_only=True)
    personality_id = serializers.PrimaryKeyRelatedField(queryset=Personality.objects.all(), write_only=True)
    item_id = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), write_only=True)
    waza1_id = serializers.PrimaryKeyRelatedField(queryset=Waza.objects.all(), write_only=True)
    waza2_id = serializers.PrimaryKeyRelatedField(queryset=Waza.objects.all(), write_only=True)
    waza3_id = serializers.PrimaryKeyRelatedField(queryset=Waza.objects.all(), write_only=True)
    waza4_id = serializers.PrimaryKeyRelatedField(queryset=Waza.objects.all(), write_only=True)


    def create(self, validated_data):
        validated_data['pokemon'] = validated_data.get('pokemon_id', None)
        validated_data['ball'] = validated_data.get('ball_id', None)
        validated_data['personality'] = validated_data.get('personality_id', None)
        validated_data['item'] = validated_data.get('item_id', None)
        validated_data['waza1'] = validated_data.get('waza1_id', None)
        validated_data['waza2'] = validated_data.get('waza2_id', None)
        validated_data['waza3'] = validated_data.get('waza3_id', None)
        validated_data['waza4'] = validated_data.get('waza4_id', None)

        if validated_data['pokemon'] is None:
            raise serializers.ValidationError("pokemon not found.") 
        
        if validated_data['ball'] is None:
            raise serializers.ValidationError("ball not found.") 

        if validated_data['personality'] is None:
            raise serializers.ValidationError("personality not found.") 

        if validated_data['item'] is None:
            raise serializers.ValidationError("item not found.")

        if validated_data['waza1'] is None:
            raise serializers.ValidationError("waza1 not found.") 
        
        if validated_data['waza2'] is None:
            raise serializers.ValidationError("waza2 not found.") 

        if validated_data['waza3'] is None:
            raise serializers.ValidationError("waza3 not found.") 

        if validated_data['waza4'] is None:
            raise serializers.ValidationError("waza4 not found.") 

        del validated_data['pokemon_id']
        del validated_data['ball_id']
        del validated_data['personality_id']
        del validated_data['item_id']
        del validated_data['waza1_id']
        del validated_data['waza2_id']
        del validated_data['waza3_id']
        del validated_data['waza4_id']

        return UserPoke.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.ability = validated_data.get('ability', instance.ability)
        instance.personality = validated_data.get('personality_id', instance.personality_id)
        instance.individual_value_h = validated_data.get('individual_value_h', instance.individual_value_h)
        instance.individual_value_a = validated_data.get('individual_value_a', instance.individual_value_a)
        instance.individual_value_b = validated_data.get('individual_value_b', instance.individual_value_b)
        instance.individual_value_c = validated_data.get('individual_value_c', instance.individual_value_c)
        instance.individual_value_d = validated_data.get('individual_value_d', instance.individual_value_d)
        instance.individual_value_s = validated_data.get('individual_value_s', instance.individual_value_s)
        instance.effort_value_h = validated_data.get('effort_value_h', instance.effort_value_h)
        instance.effort_value_a = validated_data.get('effort_value_a', instance.effort_value_a)
        instance.effort_value_b = validated_data.get('effort_value_b', instance.effort_value_b)
        instance.effort_value_c = validated_data.get('effort_value_c', instance.effort_value_c)
        instance.effort_value_d = validated_data.get('effort_value_d', instance.effort_value_d)
        instance.effort_value_s = validated_data.get('effort_value_s', instance.effort_value_s)
        instance.item = validated_data.get('item_id', instance.item_id)
        instance.waza1 = validated_data.get('waza1_id', instance.waza1_id)
        instance.waza2 = validated_data.get('waza2_id', instance.waza2_id)
        instance.waza3 = validated_data.get('waza3_id', instance.waza3_id)
        instance.waza4 = validated_data.get('waza4_id', instance.waza4_id)
        instance.remarks = validated_data.get('remarks', instance.remarks)

        instance.save()

        return instance

    class Meta:
        model = UserPoke
        fields = (
            "id", 
            "user_id",
            "pokemon", 
            "pokemon_id",
            "nickname", 
            "gender", 
            "ball", 
            "ball_id", 
            "color", 
            "ability", 
            "personality", 
            "personality_id", 
            "individual_value_h", 
            "individual_value_a", 
            "individual_value_b", 
            "individual_value_c", 
            "individual_value_d", 
            "individual_value_s", 
            "effort_value_h", 
            "effort_value_a", 
            "effort_value_b", 
            "effort_value_c", 
            "effort_value_d", 
            "effort_value_s", 
            "waza1", 
            "waza1_id", 
            "waza2", 
            "waza2_id", 
            "waza3", 
            "waza3_id", 
            "waza4", 
            "waza4_id", 
            "item", 
            "item_id", 
            "remarks",
            )
