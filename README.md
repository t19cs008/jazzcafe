# jazzcafe注文サイト

このプログラムはjazzcafeの注文サイトです．

Python & Djangoで実装されています．

デプロイ先は[https://render.com](https://render.com)を想定しています．

デプロイ先を変更する場合は，[main/settings.py](https://github.com/t19cs008/jazzcafe/blob/main/main/settings.py)を見直してください．

## デプロイする方法

執筆中

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


