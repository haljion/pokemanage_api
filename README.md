# pokemanage_api

```
tree
```

## API

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
