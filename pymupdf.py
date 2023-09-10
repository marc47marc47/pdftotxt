# -*- coding: utf-8 -*-
import fitz  # PyMuPDF

def extract_pdf_content(pdf_path):
    # 打開 PDF 文件
    doc = fitz.open(pdf_path)
    text = ""
    
    # 循環遍歷每一頁
    for page in doc:
        text += page.get_text("text")
    
    return text

pdf_content = extract_pdf_content(".\\P06J1001-20220214.pdf")
print(pdf_content[:])  # 印出前1000個字符來確認
