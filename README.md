# jazzcafe注文サイト

このプログラムはjazzcafeの注文サイトです．

Python & Djangoで実装されています．

デプロイ先は[https://render.com](https://render.com)を想定しています．

デプロイ先を変更する場合は，[main/settings.py](https://github.com/t19cs008/jazzcafe/blob/main/main/settings.py)を見直してください．

## デプロイする方法

### ステップ1 render.comでユーザ作成

[https://render.com/](https://render.com/)にアクセスして，ユーザの作成を行います．

名前とかは別に本名を入れる必要はないです．

### ステップ2 データベースの作成

[https://dashboard.render.com/](https://dashboard.render.com/)にアクセスして，データベースの作成を行います．

PostgreSQLをクリックします．

以下のように設定してください．

1. Nameを「jazzcafe-postgresql」
2. Projectを「jazzcafe」
3. Databaseを「mysite」
4. Userを「mysite」
5. Plan optionsを「Free」

Create Databaseをクリックします．

Info内にある「Connections」の「Internal Database URL」をどこかにコピーしておいてください．

### ステップ3 Djangoのデプロイ

[https://dashboard.render.com/](https://dashboard.render.com/)にアクセスして，データベースのときに作成したプロジェクトをクリックし，Create New Serviseをクリックします．

Web Servicesをクリックします．

Public Git Repositryをクリックし，このgithubのリンクをコピペします．

以下のように設定してください．

1. Nameを「jazzcafe」
2. Build Commandを「./build.sh」
3. Start Commandを「python -m gunicorn main.asgi:application -k uvicorn.workers.UvicornWorker」
4. Instance Typeを「Free」
5. Environment VariablesのNAME_OF_VALIABLEに「DATABASE_URL」と書き，valueに「ステップ2でどこかにコピーしておいたInternal Database URLをペースト」する
6. Environment VariablesのNAME_OF_VALIABLEに「SECRET_KEY」と書き，Generateをクリックする
7. Environment VariablesのNAME_OF_VALIABLEに「WEB_CONCURRENCY」と書き，valueに「4」と書く
8. Environment VariablesのNAME_OF_VALIABLEに「DJANGO_SUPERUSER_USERNAME」と書き，valueに「maki」と書く
9. Environment VariablesのNAME_OF_VALIABLEに「DJANGO_SUPERUSER_EMAIL」と書き，valueに「maki@example.com」と書く
10. Environment VariablesのNAME_OF_VALIABLEに「DJANGO_SUPERUSER_PASSWORD」と書き，valueに「ordersystemforjazzclub」と書く

*手順8から10のvalueは適宜変えてください！*

Deploy Web Serviceをクリックします．

Logsを監視します．

jazzcafeのサイトにアクセスします．

ログインします．

## 注文方法

トップページのURLの後ろに「/jazzcafe/new_order/1」を付け加えてください．

例えば，トップページのURLが「[https://jazzcafe.onrender.com](https://jazzcafe.onrender.com)」のとき，「[https://jazzcafe.onrender.com/jazzcafe/new_order/1](https://jazzcafe.onrender.com/jazzcafe/new_order/1)」となります．

これは，テーブル番号1の注文受付画面になります．

「/jazzcafe/new_order/1」を「/jazzcafe/new_order/2」に変えると，テーブル番号2の注文受付画面になります．

これは．それぞれのテーブル番号に対応するURLをQRコードにして，紙に印刷し，テーブルの上に貼り付けることを想定しています．

お客様はテーブル上のQRコードを読み込んで注文するという想定です．

## スタッフページ

トップページのURLの後ろに「/jazzcafe/staff_main_page/」を付け加えてください．

例えば，トップページのURLが「[https://jazzcafe.onrender.com](https://jazzcafe.onrender.com)」のとき，「[https://jazzcafe.onrender.com/jazzcafe/staff_main_page/](https://jazzcafe.onrender.com/jazzcafe/staff_main_page/)」となります．

ここで，未完了オーダーリストや在庫確認を行うことができます．

色々触ってみてください．

## 開発環境で実行する方法

想定環境 : 「ubuntu 20.04以上」 もしくは 「raspberry pi os」

### ステップ1 コードのclone

このプログラムのコードをダウンロードします．その後，カレントディレクトリを変更します．

```bash
git clone https://github.com/t19cs008/jazzcafe.git
cd jazzcafe
```

### ステップ1.5 仮想環境の導入

仮想環境を導入済み，もしくは仮想環境を使わない場合は飛ばしてOKです．

[Getting Pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)と[Set up your shell environment for Pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#set-up-your-shell-environment-for-pyenv)をよく読んでpyenvのインストールを行います．

**pyenvのインストールのときは一度ホームディレクトリへ戻ることをお勧めします！！**

```bash
cd ~
```

その後python 3.11をインストールします．（必要に応じてpythonのバージョンは上げたり下げたりして構いません）

```bash
pyenv install 3.11
pyenv local 3.11
```

ホームディレクトリに戻っていた場合，再度jazzcafeに入りなおします．

```
cd jazzcafe
```

### ステップ2 モジュールのインストール

このコードを動かすためのモジュールをインストールします．

```bash
pip install -r requirements.txt
```

### ステップ3 スーパーユーザの作成

Djangoの管理者ユーザを作成します．

```bash
python manage.py createsuperuser
```

### ステップ4 開発用webサーバの立ち上げ

開発用webサーバを立ち上げます．

```bash
python manage.py runserver
```

### ステップ5 サイトにアクセスしてみる

実際にサイトにアクセスしてみます．

先ほど作成した管理ユーザのIDとパスワードでログインできるはずです．

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## コードの大体の説明

[main](https://github.com/t19cs008/jazzcafe/tree/main/main) - Djangoサーバの設定

[account](https://github.com/t19cs008/jazzcafe/tree/main/account) - ユーザ管理

[jazzcafe](https://github.com/t19cs008/jazzcafe/tree/main/jazzcafe) - jazzcafe注文サイト

[templates](https://github.com/t19cs008/jazzcafe/tree/main/templates) - html共通部分

[requirements.txt](https://github.com/t19cs008/jazzcafe/blob/main/requirements.txt) - Djangoサーバを動かすために必要なpythonモジュールのリスト

[build.sh](https://github.com/t19cs008/jazzcafe/blob/main/build.sh) & [render.yaml](https://github.com/t19cs008/jazzcafe/blob/main/render.yaml) - [render.com](https://render.com)のデプロイで必要なファイル

[create_superuser.py](https://github.com/t19cs008/jazzcafe/blob/main/create_superuser.py) - デプロイ時にスーパーユーザの作成を行うためのスクリプト


