import re

# Dosyayı oku
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Tüm davetiye görselleri sırayla değiştir
# Her bir src="images/davetiye*.jpg" yi sırayla 1'den 60'a değiştir

# Önce tüm davetiye görsellerini bul
matches = list(re.finditer(r'src="images/davetiye\d+\.jpg"', content))
print(f'Toplam {len(matches)} görsel bulundu')

# Şimdi geriye doğru değiştir (index kayması olmasın diye)
for i, match in enumerate(reversed(matches)):
    image_num = len(matches) - i
    old_text = match.group(0)
    new_text = f'src="images/davetiye{image_num}.jpg"'
    
    # Bu match'i değiştir
    start = match.start()
    end = match.end()
    content = content[:start] + new_text + content[end:]
    
    if image_num % 10 == 0:
        print(f'{image_num}. görsel güncellendi')

# Dosyayı kaydet
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Toplam {len(matches)} görsel sırayla yerleştirildi (1-{len(matches)})')
