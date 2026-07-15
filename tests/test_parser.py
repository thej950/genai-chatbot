from app.services.parser import extract_text_from_pdf

text = extract_text_from_pdf("sample.pdf")

print(text)