import re
import random

# Dosyayı oku
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Davetiye görselleri
images = ['davetiye1.jpg', 'davetiye2.jpg', 'davetiye3.jpg', 'davetiye4.jpg', 
          'davetiye5.jpg', 'davetiye6.jpg', 'davetiye7.jpg', 'davetiye8.jpg']

# Her davetiye4.jpg'yi rastgele bir görsel ile değiştir
count = 0
def replace_with_random(match):
    global count
    count += 1
    random_img = random.choice(images)
    return match.group(0).replace('davetiye4.jpg', random_img)

# Regex ile değiştir
content = re.sub(r'src="images/davetiye4\.jpg"', replace_with_random, content)

# Dosyayı kaydet
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'{count} adet gorsel rastgele degistirildi!')
