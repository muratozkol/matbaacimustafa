import re
import random

# Dosyayı oku
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 20 farklı davetiye görseli (indirdiğimiz görseller)
images = [
    'davetiye1.jpg', 'davetiye2.jpg', 'davetiye3.jpg', 'davetiye4.jpg', 
    'davetiye5.jpg', 'davetiye6.jpg', 'davetiye7.jpg', 'davetiye8.jpg',
    'davetiye9.jpg', 'davetiye10.jpg', 'davetiye11.jpg', 'davetiye12.jpg',
    'davetiye13.jpg', 'davetiye14.jpg', 'davetiye15.jpg', 'davetiye16.jpg',
    'davetiye17.jpg', 'davetiye18.jpg', 'davetiye19.jpg', 'davetiye20.jpg'
]

# Tüm mevcut davetiye görsellerini bul
pattern = r'src="images/(davetiye\d+\.jpg)"'
matches = list(re.finditer(pattern, content))

print(f'Bulunan gorsel sayisi: {len(matches)}')

# 37 görsel için rastgele sıra oluştur
random_sequence = []
for i in range(37):
    random_sequence.append(random.choice(images))

# Geriye doğru değiştir (index kaymalarını önlemek için)
for i, match in enumerate(reversed(matches)):
    if i < 37:
        old_img = match.group(1)
        new_img = random_sequence[i]
        start = match.start(1)
        end = match.end(1)
        content = content[:start] + new_img + content[end:]

# Dosyayı kaydet
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'{min(len(matches), 37)} adet gorsel 20 farkli davetiye arasından rastgele degistirildi!')
print('Kullanilan gorseller:', set(random_sequence[:min(len(matches), 37)]))
