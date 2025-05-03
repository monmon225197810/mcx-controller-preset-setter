# MCX Controller Preset Setter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

マトリックスKVMスイッチャーのプリセットをブラウザから操作するためのWebアプリケーションです。

## 特徴

- モダンなダークテーマUI
- 1対1接続プリセットとN対1接続プリセットの切り替え
- リアルタイムなエラー表示
- レスポンシブデザイン
- シンプルな設定ファイル

## インストール

```bash
# リポジトリのクローン
git clone https://github.com/monmon225197810/mcx-controller-preset-setter.git
cd mcx-controller-preset-setter

# 仮想環境の作成と有効化
python -m venv venv
.\venv\Scripts\activate  # Windowsの場合

# 依存関係のインストール
pip install -r requirements.txt
```

## 使用方法

1. `config.ini`ファイルを編集して、MCXコントローラーの設定を行います
2. アプリケーションを起動します：
```bash
python app.py
```
3. ブラウザで http://<ipaddress>:5000 にアクセスします

## 貢献

プルリクエストやイシューは大歓迎です。以下の手順で貢献できます：

1. このリポジトリをフォーク
2. 新しいブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add some amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルを参照してください。

## 作者

- Hiroki Nakamura - [GitHub](https://github.com/monmon225197810)

