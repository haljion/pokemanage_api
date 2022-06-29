import os
import django
import csv

# Djangoの設定をこのスクリプトに適用する
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pokemanage_api.settings')
django.setup()

from webapi.models import Pokemon, Waza, Personality, Item, Ball, UserPoke


def insert_all_data():
    insert_poke_data()
    insert_waza_data()
    insert_personality_data()
    insert_item_data()
    insert_ball_data()


def insert_poke_data():
    with open("webapi/static/webapi/csv/pokedata.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == "name":
                continue

            pokemon = Pokemon()
            print(row)
            pokemon.name = row[0]
            pokemon.image = row[1]
            pokemon.type1 = row[2]
            pokemon.type2 = row[3]
            pokemon.ability1 = row[4]
            pokemon.ability2 = row[5]
            pokemon.hidden_ability = row[6]
            pokemon.gender_flag = row[7]
            pokemon.varioustaH = row[8]
            pokemon.varioustaA = row[9]
            pokemon.varioustaB = row[10]
            pokemon.varioustaC = row[11]
            pokemon.varioustaD = row[12]
            pokemon.varioustaS = row[13]

            pokemon.save()


def insert_waza_data():
    with open("webapi/static/webapi/csv/wazadata.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == "name":
                continue

            waza = Waza()
            print(row)
            waza.name = row[0]
            waza.waza_type = row[1]
            waza.various = row[2]

            waza.save()


def insert_personality_data():
    with open("webapi/static/webapi/csv/personality_data.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            personality = Personality()
            to_s = {"0" :"A", "1": "B", "2" :"C", "3": "D", "4" :"S", "5": "-"}
            
            print(f"{row[0]} up: {to_s[row[1]]} down: {to_s[row[2]]}")
            
            personality.name = row[0]
            personality.up = row[1]
            personality.down = row[2]

            personality.save()


def insert_item_data():
    with open("webapi/static/webapi/csv/item_data.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            item = Item()
            print(row)
            
            item.name = row[0]
            item.image = row[1]

            item.save()


def insert_ball_data():
    with open("webapi/static/webapi/csv/ball_data.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            ball = Ball()
            print(row)
            
            ball.name = row[0]
            ball.image = row[1]

            ball.save()


def delete_database():
    userpoke = UserPoke.objects.all().order_by("id")
    print(userpoke)
    # userpoke.delete()

