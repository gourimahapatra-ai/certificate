# 🧠 Python Libraries like `pytesseract` (GenAI Context)

## 📄 1. OCR (Optical Character Recognition)

### 🔍 `pytesseract`
- Wrapper for Tesseract OCR engine  
- Extracts text from images/PDFs  

### 🧾 `easyocr`
- Deep learning-based OCR  
- Works well for multilingual text  

### 🧠 `paddleocr`
- High accuracy OCR (good for complex layouts)  
- Supports tables and structured extraction  

### ⚡ `keras-ocr`
- OCR pipeline built with Keras/TensorFlow  

### 📘 `pdfminer`
- Extracts text from PDFs  
- More fine-grained control than `pypdf`  
- Useful for complex PDF parsing  

## 📑 2. PDF & Document Processing (Very Important for RAG)

### 📘 `pypdf` / `PyPDF2`
- Extract text from PDFs  

### 📄 `pdfplumber`
- Better for structured text (tables, layouts)  

### 📊 `camelot`
- Extract tables from PDFs  

### 🧾 `tabula-py`
- Java-based table extraction via Python  

---

## 🧩 3. Document Loaders (RAG Frameworks)

### 🔗 `langchain.document_loaders`
- Load data from:
  - PDFs  
  - Word files  
  - HTML  
  - APIs  

### 📚 `llama-index`
- Advanced document ingestion  
- Handles chunking and indexing  

---

## 🖼️ 4. Image Processing (Pre-OCR / Multimodal)

### 🎨 `Pillow (PIL)`
- Image preprocessing (resize, grayscale)  

### 📷 `opencv-python`
- Advanced image processing  
- Improves OCR accuracy  

---

## 🎧 5. Speech-to-Text (Multimodal GenAI)

### 🎤 `speechrecognition`
- Convert audio → text  

### 🔊 `whisper`
- High-accuracy speech-to-text model  

---

## 🧬 6. Text Processing (Post-OCR)

### ✂️ `nltk`
- Tokenization and text cleaning  

### ⚡ `spacy`
- Fast NLP processing  
- Named Entity Recognition (NER)  

---

## 🔎 7. Embeddings (Next Step After Extraction)

### 🧠 `sentence-transformers`
- Convert text → vector embeddings  

### 🤖 `openai`
- Embeddings + LLM APIs  

---

## 🔗 8. End-to-End Document AI (Highly Important)

### 📦 `unstructured`
- Handles:
  - PDFs  
  - Images  
  - Emails  
  - HTML  
- Outputs clean structured text  
- Widely used in RAG pipelines  

---

## 🧠 9. Layout-Aware Processing (Advanced)

### 📊 `layoutparser`
- Understands document structure  
- Useful for tables and sections  

---

# 🔥 Typical GenAI Pipeline

```text
Image / PDF
   ↓
OCR (pytesseract / paddleocr)
   ↓
Cleaning (nltk / spacy)
   ↓
Chunking (langchain / llama-index)
   ↓
Embedding (sentence-transformers / openai)
   ↓
Vector DB (Databricks Vector Search)
   ↓
LLM (RAG)
