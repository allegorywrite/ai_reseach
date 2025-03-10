# 協調的Visual-Inertial SLAMにおけるActive Perception研究

## 研究概要

本研究プロジェクトでは、複数のUAVによる協調的なvisual-inertial SLAMシステムにおいて、視野錐台の交差を維持するためのactive perceptionアプローチを提案します。特に、Control Barrier Functions (CBF)を用いて、エージェント間の視野錐台の交差を保証しながら、安全性（衝突回避）も同時に確保する制御手法の開発を目指しています。

研究の新規性は、以下の要素を統合する点にあります：
1. 複数UAVによる協調的visual-inertial SLAM
2. 特徴量の共有視認性（feature co-visibility）を最大化するためのactive perception
3. CBFに基づく安全性保証と視野制約の統合

## ディレクトリ構造

```
research_ws/
├── README.md                 # 本ファイル
├── .gitignore                # Gitの管理対象外ファイル設定
├── doc/                      # ドキュメント（Obsidianワークスペース）
│   ├── 研究方針.md            # 研究の進め方に関する方針
│   ├── 研究進捗.md            # 研究の進捗状況
│   ├── issue/                # 研究課題（issue）
│   │   ├── file.md           # 課題ファイル
│   │   ├── file_solved.md    # 解決済み課題
│   │   ├── file_hold.md      # 保留中の課題
│   │   └── material/         # 課題関連資料
│   ├── theory/               # 理論研究のドキュメント
│   │   └── control_barrier_functions.md  # CBFの理論
│   ├── surveys/              # サーベイ関連
│   │   └── task_{i}/         # 各サーベイタスク
│   │       ├── request.md    # サーベイリクエスト
│   │       ├── answer.md     # サーベイ結果
│   │       └── materials/    # 参考資料（gitignore対象）
│   └── experiment/           # 実験に関するドキュメント
└── src/                      # ソースコード
    ├── experiment/           # 理論検証用Python実装
    └── implementation/       # 本番用C++実装
```

## 研究の進め方

研究は以下の流れで進めます：

1. **サーベイ** → 2. **理論研究** → 3. **実装（理論検証）** → 4. **実装（本番）**

理論研究や実装の過程で必要に応じて適宜サーベイに戻ることもあります。

研究作業は以下の手順で行います：

1. `doc/issue/` 内の未解決の課題を確認して取り組む
2. 課題の解決を試み、解決できたものは `file_solved.md`、保留にするものは `file_hold.md` とする
3. 研究進捗に基づいて研究を進める
4. 研究結果に基づいて適宜README.mdを修正する
5. 研究進捗を追記する

### サーベイ

- サーベイは `doc/surveys/task_{i}/request.md` を作成してサーベイ要件をまとめます
- サーベイはDeep Researchを使用するため、request.mdを作成した時点で停止し、answer.mdの作成を待ちます

### 理論研究

- 理論研究は `doc/theory/` 内でマークダウン資料を書きながら進めます
- 理論研究中にサーベイが必要な場合は、`surveys/task_{i}/request.md` を作成します
- 理論研究の検証として簡易的な数値検証を行う場合は、実装規則に基づいて理論検証を行います

### 実装

- **理論検証用実装**：Pythonで行います。`src/experiment/` に実装し、対応する理論的内容を `doc/experiment/` に同名のmdファイルでドキュメント化します
- **本番実装**：C++で行います。実装方針は未定です

## ツールの利用方法

### Clineの利用方法

Clineは研究プロジェクトの支援ツールとして使用します。

1. **Cursorエディタの起動**：ワークスペースディレクトリ（`research_ws/`）で Cursor エディタを開きます
2. **Clineの利用**：Cursor エディタ内で Cline を使用して以下のタスクを行います：
   - サーベイリクエストの作成支援
   - 理論研究の文書作成支援
   - コード実装の支援
   - デバッグの支援

### Obsidianの利用方法

Obsidianはドキュメント管理と閲覧のために使用します。

1. **Obsidianの設定**：
   - Obsidianを起動し、`doc/` ディレクトリをワークスペースとして開きます
   - 設定 → ファイルとリンク → 「新規リンクの相対パスを使用」をオンにします

2. **ドキュメントの閲覧**：
   - 研究方針、研究進捗、理論研究ドキュメントなどをObsidianで閲覧します
   - マークダウンの数式表示、グラフ表示などの機能を活用します

3. **リンクの活用**：
   - ドキュメント間のリンクを活用して、関連する内容を相互参照します
   - タグ機能を使って、関連するドキュメントを分類・整理します

## 研究進捗の管理

研究の進捗は `doc/研究進捗.md` に記録します。このファイルには以下の内容を含めます：

1. 現在の研究概要
2. 進捗
3. 次やるべきこと

研究の進行に合わせて、このファイルを定期的に更新していきます。

## 参考

- [研究方針](doc/研究方針.md)
- [研究進捗](doc/研究進捗.md)
- [Control Barrier Functions理論](doc/theory/control_barrier_functions.md)
