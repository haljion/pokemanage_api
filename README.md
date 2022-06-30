# pokemanage_api

```
tree
```

## API

※token free  
→headerに key: Authorization, value: JWT [access token] が必要かどうか

| url |  | method | api | param | return | token free |
| - | - | - | - | - | - | - |
| /api | - | - | 自作API |  | - | - |
|  | /create | POST | ユーザー作成 | username, password | id,username | ○ |
|  | /loginuser | GET, POST | ログインユーザー情報 |  | - | × |
|  | /pokemons | GET | ポケモン一覧 | - | - | × |
|  | /pokemon/<int:pk> | GET | ポケモン情報(単体) | - | - | × |
|  | /items | GET | アイテム一覧 | - | - | × |
|  | /balls | GET | ボール一覧 | - | - | × |
|  | /personalities | GET | 性格一覧 | - | - | × |
|  | /wazas | GET | わざ一覧 | - | - | × |
|  | /userpoke | GET, POST, PUT, DELETE | 育成個体情報(一覧、検索、登録、更新、削除) |  |  | × |
| /admin | - | - | Django管理サイト | - | - | - |


## 開発環境構築
docker-composeの以下の行をコメントアウト
```
command: python manage.py runserver 0.0.0.0:8000
```
```
docker-compose up
```

### DBセットアップ
dbコンテナ内で作業する
```
docker container exec -it db psql -U postgres
```
DB作成
```
CREATE DATABASE pokemanage;
CREATE USER admin WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE pokemanage TO admin;
```

### Djangoセットアップ
webapiコンテナ内で作業する
```
docker container exec -it webapi bash
```

```
pip install -r requirements.txt
```

```
python manage.py migrate
python manage.py createsuperuser

ユーザー名 (leave blank to use 'root'): (blank)
メールアドレス: (blank)
Password:P@ssword
```
DBデータ投入
```
# /var/www/src
python -c "import scripts.csv_to_db; scripts.csv_to_db.insert_all_data()"
```