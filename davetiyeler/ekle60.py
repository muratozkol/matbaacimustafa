import re

# Dosyayı oku
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Tek bir div bloğunun template'i (37. divden sonra eklenecek)
div_template = '''                                                <div role="listitem" class="w-dyn-item">
                                                    <div data-w-id="636551b3-2d62-a005-11db-491a410b5ac2" style="-webkit-transform:translate3d(0, 40px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-moz-transform:translate3d(0, 40px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-ms-transform:translate3d(0, 40px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);transform:translate3d(0, 40px, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);opacity:0"
                                                        class="blog_v1_item">
                                                        <a data-w-id="636551b3-2d62-a005-11db-491a410b5ac3" href="/post/smarter-database-testing-with-ai-automation" class="blog_v1_item-link w-inline-block">
                                                            <div class="margin-bottom margin-small">
                                                                <div class="blog_v1_image-wrapper"><img style="-webkit-transform:translate3d(0, 0, 0) scale3d(1, 1, 1) rotateX(null) rotateY(null) rotateZ(0deg) skew(0, 0);-moz-transform:translate3d(0, 0, 0) scale3d(1, 1, 1) rotateX(null) rotateY(null) rotateZ(0deg) skew(0, 0);-ms-transform:translate3d(0, 0, 0) scale3d(1, 1, 1) rotateX(null) rotateY(null) rotateZ(0deg) skew(0, 0);transform:translate3d(0, 0, 0) scale3d(1, 1, 1) rotateX(null) rotateY(null) rotateZ(0deg) skew(0, 0);transform-style:preserve-3d"
                                                                        loading="lazy" alt="Davetiye" src="images/davetiyeXXX.jpg"
                                                                        class="blog_image"></div>
                                                            </div>

                                                        </a>
                                                    </div>
                                                </div>
'''

# Son div'i bul ve ondan önce 23 tane daha ekle
# Son </div></div></div> bloğunu bul (576. satır civarı)
pattern = r'(.*<div role="listitem" class="w-dyn-item">.*?</div>\s*</div>\s*</div>)(.*?</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>)'

match = re.search(pattern, content, re.DOTALL)
if match:
    # Son div'den sonra ekle
    last_div_end = match.end(1)
    
    # 23 yeni div ekle
    new_divs = '\n'
    for i in range(38, 61):  # 38'den 60'a kadar
        new_div = div_template.replace('davetiyeXXX.jpg', f'davetiye{i}.jpg')
        new_divs += new_div
    
    # İçeriğe ekle
    content = content[:last_div_end] + new_divs + content[last_div_end:]
    print(f'23 yeni div eklendi (davetiye38.jpg - davetiye60.jpg)')
else:
    print('Ekleme noktası bulunamadı! Manuel ekleme yapılıyor...')
    # Basit ekleme: 576. satırdan önce ekle
    lines = content.split('\n')
    insert_line = 576
    new_divs_list = []
    for i in range(38, 61):
        new_div = div_template.replace('davetiyeXXX.jpg', f'davetiye{i}.jpg')
        new_divs_list.extend(new_div.split('\n'))
    
    lines = lines[:insert_line] + new_divs_list + lines[insert_line:]
    content = '\n'.join(lines)
    print(f'Manuel ekleme: 23 yeni div eklendi')

# Şimdi tüm görselleri 1'den 60'a kadar sırayla değiştir
count = 0
for i in range(1, 61):
    pattern = f'src="images/davetiye\\d+\\.jpg"'
    replacement = f'src="images/davetiye{i}.jpg"'
    content, n = re.subn(pattern, replacement, content, count=1)
    count += n

# Dosyayı kaydet
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Toplam {count} gorsel yerlestirildi!')
print('60 davetiye görseli başarıyla eklendi!')
