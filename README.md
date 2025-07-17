# note-helper
streamlit app to help posting on note(SNS)

## ✨ Purpose / 目的
This project is a personal tool to support my weekly investment-related note-taking and content publishing.
I created it to help me reflect regularly on both financial results ("money economy") and long-term personal growth ("reputation economy").

このプロジェクトは、自分自身の投資学習や発信を補助するために作成した個人ツールです。
投資による成果（＝お金）と、活動の継続や発信による信頼の積み重ね（＝評価）の両面を意識しながら、定期的に振り返るために使っています。

More broadly, this app serves as a tool for self-education and weekly reflection, helping me observe and improve how I think—especially around finance and broader worldviews.
My internal framework looks like this:

より広い視点で言えば、このアプリは**自分自身の教育（self-education）や週間付け（weekly grounding）**を支援するためのツールでもあります。
私は日々のインプット・アウトプットを通じて、自分の思考や視点（特にお金や世界の捉え方）を見直し、整えていくことを意識しています。

週間・教育
├─ お金・評価
      ├─ 心理
      ├─ 思考
            ├─ マクロ観
                  ├─ ファンダメンタルズ
                  ├─ テクニカル
                        ├─ チャート
                        ├─ センチメント

This app does not aim to replace thinking, but to support the thinking process—especially in the repetitive, mechanical parts that can be delegated to code.
By reducing friction in the routine, I can focus more on reflection, learning, and honest expression.

このアプリは、思考そのものを代替するのではなく、思考を支えるための補助輪として設計しています。
特に繰り返しや機械的な作業はコードに任せ、自分は振り返り・学び・正直な言語化に集中できるようにしています。
---

## 🔍 Philosophy / 方針
I value the process itself, not only results.

This app is part of my journey to keep improving that process over time.

I'm not aiming for "virality", but for quiet continuity and deep connections.

As a cautious but sincere person, I believe in the power of honest efforts and long-term perspective.

私は、「成果」だけでなく、その過程そのものと、その改善の継続性を大切にしています。
このツールは、そうした考えを日々実践するための小さな助けです。
バズを狙うのではなく、濃いつながりと、地に足のついた継続を目指しています。
臆病でも、真面目に続けることが、遠回りに見えて一番強いと信じています。


## 🧭 Goals / 目標

- Make my investment thinking more structured and visible
- Automate small steps to reduce friction in regular reviews
- Accumulate public work that reflects how I think and grow
- If helpful to others, that's a bonus

このアプリは、自分の投資思考を構造化・可視化し、定期的な振り返りのハードルを下げることを目指しています。  
その過程と改善をオープンにすることで、自分の「思考の跡」や「成長の軌跡」を残したいと考えています。  
それがもし誰かの参考になれば、それはうれしい「副産物」です。

## Features / 機能概要
This app is designed to streamline the weekly content creation workflow for posting articles on note. It supports users by displaying routine steps and automating those that can be handled programmatically. The development prioritizes features that offer the greatest reduction in workload.

🧭 Routine Workflow Support
The app displays a sequence of routine tasks tailored to each day of the week. For steps that can be automated, an execution button is placed next to the instruction. This allows users to complete tasks through a simple, guided interface.

🧮 Automated Data Visualization
Based on data stored in Google Spreadsheets, the app generates relevant graphs, tables, and lists using Python. (A future transition to SQLite is also being considered.)

✏️ AI-Powered Review and Editing
The app connects with OpenAI's API and Google Drive. Users can select a target Google Document and send predefined prompts to ChatGPT to ensure compliance (e.g., avoiding financial advice) and request language polishing if approved.

🎨 Thumbnail Generation with Prompt Templates
Each weekday has a default prompt for thumbnail creation, which users slightly revise weekly. The app allows prompt selection and editing directly within the interface.

🏷️ Tagging Support for note Articles
Basic tags for each weekday can be selected and modified in the app, simplifying the tagging process when publishing to note.

📄 Document Templating
Users can choose a document template, and the app supports inserting generated graphs, tables, and lists into the appropriate locations in the file.

⚠️ Note: The step of retrieving raw data from external websites is intentionally kept manual to ensure compliance with usage policies and avoid potential violations.


このアプリは、noteでの記事投稿に関する週間ルーティン作業を効率化するために設計されています。作業手順を画面上に表示し、機械的に処理できる工程は自動化することで、ユーザーの負担を大きく軽減します。
開発は、作業負荷の高い工程から優先的に進めています。

🧭 ルーティン作業の手順表示と実行支援
曜日ごとの作業手順をアプリ上に一覧表示し、プログラムで実行可能な手順には同じ行に実行ボタンを配置しています。ユーザーは順を追って作業を進めることができ、操作も直感的です。

🧮 データの可視化処理の自動化
Googleスプレッドシートに蓄積されたデータをもとに、グラフ、表、リストをPythonで自動生成します。
（将来的にはSQLiteへの移行も検討しています）

✏️ AIによる内容確認と文章添削
OpenAIのAPIおよびGoogle Driveと連携し、指定したGoogleドキュメントの内容をChatGPTに送信します。事前に用意された定型プロンプトを使って、金融助言に該当しないかのチェックを行い、問題なければ文章の添削も依頼できます。

🎨 サムネイル画像の生成支援
各曜日に対応した基本プロンプトを選択でき、毎週微修正して使い回す形式を支援します。
画像生成に必要なプロンプトはアプリ内で選択・編集可能です。

🏷️ note記事のタグ付け補助
noteでの公開時に必要なタグについても、各曜日に対応する基本タグをアプリ内で選択・編集できるようになっています。

📄 ドキュメントへの図表挿入
作成した図や表、リストをGoogleドキュメントのテンプレートに挿入する機能を備えています。テンプレートはアプリ内で選択可能です。

⚠️ 注意：一次情報サイトからのデータ取得作業については、利用規約・ポリシーに抵触しないようにするため、あえて手動作業のままとしています。


## 📁 Project Directory tentative Structure / プロジェクトのディレクトリ構成イメージ

my_app/
├─ app_main.py ← Main UI entry point / 起点となるメインUI
├─ routines/ ← Modules for each day's process / 曜日ごとの処理モジュール
│ ├─ monday_politics.py ← Monday: Politics and Commodities / 月曜：政治・コモディティ
│ ├─ tuesday_agri.py ← Tuesday: Agricultural Markets / 火曜：農業市場
│ ├─ thursday_energy.py ← Thursday: Energy Markets / 木曜：エネルギー市場
│ ├─ friday_jpmarket.py ← Friday: Japanese Stock Market / 金曜：日本株
│ ├─ saturday_usmarket.py ← Saturday: US Stock Market / 土曜：米国株
│ └─ sunday_worldmarket.py ← Sunday: Global Market Overview / 日曜：世界市場
├─ common/ ← Shared utilities (graphs, sheets, etc.) / 共通処理（グラフ・後処理など）
│ ├─ sheet_utils.py ← GSpread and spreadsheet operations / GSpread接続など
│ ├─ graph_utils.py ← Plotting and chart functions / グラフ関連関数
│ ├─ doc_utils.py ← Text/document generation utilities / テキスト生成処理
│ └─ ui_components.py ← Custom UI parts for Streamlit / UIの共通部品
├─ assets/ ← Generated images and data files / 生成画像・CSVなど
│ ├─ cftc_futuresonly.csv ← CFTC base data (Futures Only) / CFTC元データ（FuturesOnly）
│ ├─ cftc_optionscombined.csv ← CFTC base data (Options Combined) / CFTC元データ（OptionsCombined）
│ └─ graph1.png ← Example of generated chart / 生成された画像の例
└─ .streamlit/
└─ secrets.toml ← API keys (OpenAI, GCP, etc.) / APIキーの格納（OpenAI/GCPなど）
