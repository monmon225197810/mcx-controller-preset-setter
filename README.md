# MCXコントローラープリセット制御Webアプリケーション

## 概要

Black Box社のMCX-G2-CTRL-24マトリックスKVMスイッチャー（MCXコントローラー）のプリセットをブラウザから操作するためのWebアプリケーションです。

## 機能

- MCXコントローラーに対してHTTPリクエストを送信し、プリセットを呼び出し
- 1対1接続プリセットとN対1接続プリセットの切り替え
- 現在選択されているプリセットの表示
- エラーメッセージの表示
- レスポンシブデザイン対応

## セットアップ手順

1. 仮想環境の作成と有効化:
```bash
python -m venv venv
.\venv\Scripts\activate  # Windowsの場合
```

2. 依存関係のインストール:
```bash
pip install -r requirements.txt
```

3. 設定ファイルの編集:
`config.ini`ファイルを編集し、以下の情報を設定します：
- MCXコントローラーのIPアドレス
- ポート番号
- セキュリティキー
- プリセット情報

4. アプリケーションの実行:
```bash
python app.py
```

5. ブラウザで http://localhost:5000 にアクセス

## ファイル構成

```
.
├── app.py                 # メインアプリケーションファイル
├── config.ini            # 設定ファイル
├── mcx_controller.py     # MCXコントローラーとの通信モジュール
├── requirements.txt      # 依存関係ファイル
├── static/
│   ├── css/
│   │   └── style.css    # スタイルシート
│   └── js/
│       └── main.js      # JavaScriptファイル
└── templates/
    └── index.html       # メインテンプレート
```

## 設定ファイル（config.ini）の例

```ini
[MCX_CONTROLLER]
ip_address = 192.168.1.100
port = 6980
security_key = abc123
timeout = 5
polling_interval = 10

[ERROR_MESSAGES]
timeout = "MCXコントローラーとの通信がタイムアウトしました"
connection_error = "MCXコントローラーへの接続に失敗しました"
preset_error = "プリセット '{preset_name}' の設定に失敗しました"

[PRESETS]
# 1対1接続プリセット
one_to_one = preset1, preset2, preset3

# N対1接続プリセット
n_to_one = preset4, preset5, preset6

[PRESET_NAMES]
# プリセット名と表示名のマッピング
preset1 = 会議室A
preset2 = 会議室B
preset3 = 会議室C
preset4 = マルチディスプレイ1
preset5 = マルチディスプレイ2
preset6 = マルチディスプレイ3
```

## 依存関係

- Flask==3.0.2
- python-dotenv==1.0.1
- requests==2.31.0

## 注意事項

- 本アプリケーションは内部ネットワークでの利用を想定しています
- MCXコントローラーがネットワーク経由でAPIアクセス可能である必要があります
- プリセットの設定はMCXコントローラー側で事前に行われている必要があります 