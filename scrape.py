import requests
from time import sleep
import csv
from bs4 import BeautifulSoup


def data_extraction(img_name, bs):
    # 種族ごとの情報をまとめた辞書
    info_dict = {}
    # 名称
    name = bs.select_one("#title").text
    info_dict["name"] = name.split("-")[0]
    # 画像
    info_dict["image"] = img_name # 画像リンク
    # image_url = bs.select_one("#base_anchor").select_one("img").get("src")
    # image_url = "https:" + image_url
    # image = requests.get(image_url)
    
    # with open("webapi/static/webapi/img/pokemon/" + info_dict["image"], "wb") as f:
    #     f.write(image.content)

    # タイプ
    types = bs.select_one("ul.type").select("li a img")
    info_dict["type1"] = types[0].get("alt")
    info_dict["type2"] = ""

    if len(types) == 2:
        info_dict["type2"] = types[1].get("alt")
    
    # 特性
    detail_data = bs.select_one("table.center")
    abilitys = detail_data.select("td.c1 a")
    info_dict["ability1"] = abilitys[0].text # 特性1
    info_dict["ability2"] = "" # 特性2
    info_dict["hidden_ability"] = "" # 隠れ特性

    if len(abilitys) == 3:
        # 特性2つ、隠れ特性あり
        info_dict["ability2"] = abilitys[1].text
        info_dict["hidden_ability"] = abilitys[2].text[1:]

    elif len(abilitys) == 2:
        # 特性1つ、隠れ特性あり
        info_dict["hidden_ability"] = abilitys[1].text[1:]

    # 性別の有無
    gender = bs.select("td.left")[19].text
    
    if gender == "ふめい":
        info_dict["gender_flag"] = 1
    else:
        info_dict["gender_flag"] = 0

    # 種族値
    varioustaList = [int(s.text.split("(")[0]) for s in bs.select("td.left")[:6]]
    info_dict["varioustaH"] = varioustaList[0]
    info_dict["varioustaA"] = varioustaList[1]
    info_dict["varioustaB"] = varioustaList[2]
    info_dict["varioustaC"] = varioustaList[3]
    info_dict["varioustaD"] = varioustaList[4]
    info_dict["varioustaS"] = varioustaList[5]

    print("success:", info_dict["name"], info_dict["varioustaH"], \
        info_dict["varioustaA"], info_dict["varioustaB"], info_dict["varioustaC"], info_dict["varioustaD"], info_dict["varioustaS"], info_dict["gender_flag"])
    
    return info_dict

 
def get_pokedata():
    url_base = "https://yakkun.com/swsh/zukan/n"
    url_base_sm = "https://yakkun.com/sm/zukan/n"
    info_dicts = []

    # ポケモンの数
    for i in range(1, 899):
        img_name = f"n{str(i).zfill(3)}.png"
        url = url_base + str(i)
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        bs = BeautifulSoup(response.text, "html.parser")
        
        version = bs.select_one("#title").text.split("図鑑")[1]
        # アルセウス版だと正常に値が取得できない為サン/ムーン版から取得
        if version == "アルセウス":
            url = url_base_sm + str(i)
            
            print("アルセウス野郎だ～！！:", url)
            
            response = requests.get(url)
            response.encoding = response.apparent_encoding
            bs = BeautifulSoup(response.text, "html.parser")
        
        info_dicts.append(data_extraction(img_name, bs))
        sleep(10)
        form_check = bs.select_one(".select_list .select_label")

        if form_check is not None:
            forms = bs.select(".select_list")[1].select("li a")
            form_list = ["https://yakkun.com" + f.get("href") for f in forms]

            for form in form_list:
                img_name_f = f"n{str(i).zfill(3)}{form[-1]}.png"
                response = requests.get(form)
                response.encoding = response.apparent_encoding

                bs = BeautifulSoup(response.text, "html.parser")
                info_dicts.append(data_extraction(img_name_f, bs))
                sleep(10)
    

    with open("webapi/static/webapi/csv/pokedata.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, ["name", "image", "type1", "type2", "ability1", "ability2", "hidden_ability",\
            "gender_flag", "varioustaH", "varioustaA", "varioustaB", "varioustaC", "varioustaD", "varioustaS"])
        writer.writeheader()
        writer.writerows(info_dicts)


def get_wazadata():
    info_dicts = []

    url = "https://yakkun.com/swsh/move_list.htm"
    response = requests.get(url)
    response.encoding = response.apparent_encoding

    bs = BeautifulSoup(response.text, "html.parser")
    str_to_i = {"物理": 0, "特殊": 1, "変化": 2}

    for line in bs.select("tr.sort_tr"):
        info_dict = {}
        info_dict["name"] = line.select_one(".left.c1 a").text

        if "キョダイ" in info_dict["name"] or info_dict["name"][:2] == "ダイ":
            continue

        info_dict["waza_type"] = line.select_one("span.type").text
        various = line.select("td")[2].select_one("a").text
        info_dict["various"] = str_to_i[various]

        info_dicts.append(info_dict)
    

    with open("webapi/static/webapi/csv/wazadata.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, ["name", "waza_type", "various"])
        writer.writeheader()
        writer.writerows(info_dicts)


def get_itemdata():
    info_dicts = []

    url = "https://game8.jp/pokemon-sword-shield/299351"
    response = requests.get(url)
    response.encoding = response.apparent_encoding

    bs = BeautifulSoup(response.text, "html.parser")
    items = bs.select(".a-table")
    
    for item, s in zip([items[8], items[11], items[13], items[14]], ["b", "k", "o", "m"]):

        for i, line in enumerate(item.select("tr td a")):
            info_dict = {}
            info_dict["name"] = line.text
            info_dict["image"] = f"n{str(i).zfill(3)}{s}.png"
            image_url = line.select_one("img").get("data-src")
            image = requests.get(image_url)
            print(info_dict["name"], info_dict["image"])
    
            with open("webapi/static/webapi/img/item/" + info_dict["image"], "wb") as f:
                f.write(image.content)

            info_dicts.append(info_dict)

    
    with open("webapi/static/webapi/csv/item_data.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, ["name", "image"])
        writer.writeheader()
        writer.writerows(info_dicts)


def get_balldata():
    info_dicts = []

    url = "https://game8.jp/pokemon-sword-shield/299351"
    response = requests.get(url)
    response.encoding = response.apparent_encoding

    bs = BeautifulSoup(response.text, "html.parser")
    balls = bs.select(".a-table")[10]


    for i, line in enumerate(balls.select("tr td a")):
        info_dict = {}
        info_dict["name"] = line.text
        info_dict["image"] = f"n{str(i).zfill(2)}b.png"
        image_url = line.select_one("img").get("data-src")
        image = requests.get(image_url)
        print(info_dict["name"], info_dict["image"])
    
        with open("webapi/static/webapi/img/ball/" + info_dict["image"], "wb") as f:
            f.write(image.content)

        info_dicts.append(info_dict)

    
    with open("webapi/static/webapi/csv/ball_data.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, ["name", "image"])
        writer.writeheader()
        writer.writerows(info_dicts)
