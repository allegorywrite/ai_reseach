# PDF Processor: 論文PDFからマークダウンへの変換

## 1. 概要

PDF Processorは、学術論文などのPDFファイルからテキストを抽出し、マークダウン形式に変換するためのツールです。このツールは、研究プロセスにおいて論文の内容を効率的に整理・分析するために開発されました。

主な機能：
- PDFファイルからのテキスト抽出
- 抽出したテキストのクリーニング
- マークダウン形式への変換
- コマンドラインインターフェースの提供

## 2. 理論的背景

### 2.1 PDFテキスト抽出の課題

PDFは表示形式を保持するためのフォーマットであり、テキスト抽出には以下のような課題があります：

1. **レイアウト情報の喪失**: PDFはページレイアウトを保持するように設計されており、テキストの論理的な流れが必ずしも物理的な配置と一致しない
2. **特殊文字と数式**: 学術論文には数式や特殊文字が多く含まれ、これらの正確な抽出が困難
3. **複数列レイアウト**: 多くの論文は2列レイアウトで、テキスト抽出時に列が混ざることがある
4. **ヘッダー・フッター**: ページ番号やヘッダー情報がテキストの流れを中断する

### 2.2 マークダウン変換の利点

マークダウンは以下の理由から研究文書の整理に適しています：

1. **可読性**: プレーンテキストベースで人間が読みやすい
2. **構造化**: 見出し、リスト、強調などの基本的な構造化が可能
3. **Obsidianとの互換性**: 本研究プロジェクトで使用しているObsidianと完全に互換性がある
4. **バージョン管理**: テキストベースのため、Gitなどでの差分管理が容易

### 2.3 正規表現によるパターン認識

本ツールでは、学術論文の一般的な構造（セクション見出し、参考文献、図表キャプションなど）を正規表現パターンで認識し、適切なマークダウン要素に変換します。これにより、元の論文の構造をある程度保持したマークダウン文書を生成します。

## 3. 実装詳細

### 3.1 テキスト抽出方法

PDFからのテキスト抽出には、以下の2つの方法を実装しています：

1. **PyPDF2ライブラリ**: Pythonネイティブのライブラリを使用した抽出
   ```python
   def extract_text_from_pdf(self, pdf_path: str) -> str:
       try:
           import PyPDF2
           with open(pdf_path, 'rb') as file:
               reader = PyPDF2.PdfReader(file)
               text = ""
               for page_num in range(len(reader.pages)):
                   page = reader.pages[page_num]
                   text += page.extract_text()
               return text
       except ImportError:
           print("PyPDF2 is not installed. Trying pdftotext...")
           return self._extract_text_using_pdftotext(pdf_path)
   ```

2. **pdftotext外部コマンド**: PyPDF2が利用できない場合のフォールバック
   ```python
   def _extract_text_using_pdftotext(self, pdf_path: str) -> str:
       import subprocess
       import tempfile
       
       with tempfile.NamedTemporaryFile(suffix='.txt') as temp_file:
           try:
               subprocess.run(['pdftotext', pdf_path, temp_file.name], check=True)
               with open(temp_file.name, 'r') as f:
                   return f.read()
           except (subprocess.SubprocessError, FileNotFoundError):
               print("Error: pdftotext command failed. Make sure it's installed.")
               return ""
   ```

### 3.2 テキストクリーニング

抽出されたテキストには、余分な改行や空白、ハイフネーションなどの問題があります。これらを以下の処理で修正します：

```python
def clean_text(self, text: str) -> str:
    # 余分な改行を削除
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # 余分なスペースを削除
    text = re.sub(r' +', ' ', text)
    
    # ハイフネーションの修正（行末のハイフンで分割された単語を結合）
    text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', text)
    
    return text
```

### 3.3 マークダウン変換

クリーニングされたテキストを、正規表現パターンを使用して構造化されたマークダウンに変換します：

```python
def convert_to_markdown(self, text: str) -> str:
    # セクション見出しの変換
    text = re.sub(r'^([IVX]+\.\s+.+)$', r'## \1', text, flags=re.MULTILINE)
    text = re.sub(r'^([0-9]+\.\s+.+)$', r'### \1', text, flags=re.MULTILINE)
    
    # サブセクション見出しの変換
    text = re.sub(r'^([A-Z]\.\s+.+)$', r'#### \1', text, flags=re.MULTILINE)
    
    # 数式のフォーマット
    text = re.sub(r'\$(.+?)\$', r'$\1$', text)
    
    # 参考文献のフォーマット
    text = re.sub(r'^\[([0-9]+)\](.+)$', r'- [\1]\2', text, flags=re.MULTILINE)
    
    # 図表のフォーマット
    text = re.sub(r'^(Fig\.\s+[0-9]+:)(.+)$', r'**\1**\2', text, flags=re.MULTILINE)
    
    return text
```

## 4. 使用方法

### 4.1 コマンドラインからの使用

```bash
python src/experiment/pdf_processor.py input.pdf output.md
```

### 4.2 Pythonモジュールとしての使用

```python
from pdf_processor import PDFProcessor

processor = PDFProcessor()
markdown_text = processor.pdf_to_markdown('input.pdf')
with open('output.md', 'w') as f:
    f.write(markdown_text)
```

### 4.3 研究プロジェクトでの活用例

1. **論文サーベイの効率化**: 
   ```bash
   python src/experiment/pdf_processor.py doc/issue/material/paper.pdf doc/surveys/paper_summary.md
   ```

2. **複数論文の一括処理**:
   ```bash
   for pdf in doc/issue/material/*.pdf; do
     output="doc/surveys/summaries/$(basename "$pdf" .pdf).md"
     python src/experiment/pdf_processor.py "$pdf" "$output"
   done
   ```

## 5. 制限事項と今後の改善点

現在の実装には以下の制限があります：

1. **複雑なレイアウト**: 複数列レイアウトや複雑な表組みの処理が不完全
2. **数式の処理**: 複雑な数式の適切な変換が困難
3. **図表の処理**: 図表自体は抽出されず、キャプションのみが処理される
4. **言語依存性**: 英語論文を前提としたパターン認識を使用

今後の改善点：

1. **OCRの統合**: 画像ベースのPDFに対応するためのOCR機能の追加
2. **MathJax/LaTeX対応の強化**: 数式の適切な変換
3. **多言語対応**: 日本語論文などへの対応
4. **機械学習による構造認識**: パターンマッチングだけでなく、機械学習を用いた文書構造の認識

## 6. 結論

PDF Processorは、研究プロセスにおける論文の整理・分析を効率化するためのツールです。PDFからテキストを抽出し、マークダウン形式に変換することで、Obsidianなどのツールでの活用が容易になります。現在の実装には制限がありますが、基本的な論文構造の認識と変換が可能であり、研究プロジェクトの効率化に貢献します。
