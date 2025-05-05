from docx import Document

def read_docx(file_path):
    rec=""
    try:
        doc = Document(file_path)
        for para in doc.paragraphs:
            rec+=" "+para.text

    except Exception as e:
        print(f"❌ Error reading file: {e}")
    return rec

