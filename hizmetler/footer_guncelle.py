import re

# Yeni footer HTML (tüm hizmetler için path'ler farklı)
yeni_footer = '''    <footer class="footer_component">
        <div class="padding-global">
            <div class="container-large">
                <div class="padding-vertical padding-xxlarge">
                    <div class="padding-bottom padding-xxlarge">
                        <div class="w-layout-grid footer_top-wrapper">
                            <div id="w-node-f0dfafb4-3a26-b6a3-fe71-34b55a052e27-5a052e0b" data-w-id="f0dfafb4-3a26-b6a3-fe71-34b55a052e27" class="footer_column">
                                <a href="../index.html" class="footer_logo-link w-nav-brand"><img width="100" loading="lazy" alt="Matbaacı Mustafa Logo" src="../images/68e691219eb65fad724321b3_Company%20Logo.png" class="navbar_logo"></a>
                                <p class="footer_logo-notes">Profesyonel matbaa hizmetleri ile sizlere hizmet vermekten gurur duyuyoruz. Kaliteli baskı çözümleri için yanınızdayız.</p>
                            </div>
                            <div blocks-name="footer5_link-list" blocks-slot-children="ST232" id="w-node-f0dfafb4-3a26-b6a3-fe71-34b55a052e2c-5a052e0b" data-w-id="f0dfafb4-3a26-b6a3-fe71-34b55a052e2c" class="footer_link-list">
                                <div class="margin-bottom margin-xsmall">
                                    <div blocks-name="block" class="text-weight-bold text-color-white">Hızlı Linkler</div>
                                </div>
                                <a href="../index.html" blocks-name="footer5_link" class="footer_link">Ana Sayfa</a>
                                <a href="../davetiye sayfası/index.html" blocks-name="footer5_link" class="footer_link">Davetiye Modelleri</a>
                                <a href="index.html" blocks-name="footer5_link" class="footer_link">Tüm Hizmetler</a>
                                <a href="../iletisim.html" blocks-name="footer5_link-7" class="footer_link">İletişim</a>
                            </div>
                            <div blocks-name="footer5_link-list" blocks-slot-children="ST232" data-w-id="f0dfafb4-3a26-b6a3-fe71-34b55a052e42" class="footer_link-list">
                                <div class="margin-bottom margin-xsmall">
                                    <div blocks-name="block" class="text-weight-bold text-color-white">Hizmetlerimiz</div>
                                </div>
                                <a href="../davetiye sayfası/index.html" blocks-name="footer5_link-2" class="footer_link">Davetiye Baskı</a>
                                <a href="index.html" blocks-name="footer5_link-2" class="footer_link">Kartvizit</a>
                                <a href="index.html" blocks-name="footer5_link-2" class="footer_link">Afiş & Broşür</a>
                                <a href="index.html" blocks-name="footer5_link-2" class="footer_link">Dijital Baskı</a>
                                <a href="index.html" blocks-name="footer5_link-2" class="footer_link">Özel Tasarım</a>
                            </div>
                            <div blocks-name="footer5_link-list-2" blocks-slot-children="ST232" data-w-id="f0dfafb4-3a26-b6a3-fe71-34b55a052e5a" class="footer_link-list">
                                <div class="margin-bottom margin-xsmall">
                                    <div blocks-name="block-2" class="text-weight-bold text-color-white">İletişim</div>
                                </div>
                                <p class="footer_link" style="opacity: 0.8; cursor: default;">Matbaacı Mustafa</p>
                                <p class="footer_link" style="opacity: 0.8; cursor: default;">Mustafa Kaya</p>
                                <a href="tel:+905459700041" class="footer_link">Tel: 0545 970 00 41</a>
                                <a href="mailto:musti_usta55@hotmail.com" class="footer_link">musti_usta55@hotmail.com</a>
                                <p class="footer_link" style="opacity: 0.8; cursor: default; font-size: 14px; margin-top: 10px;">Adres: [İşletme adresi buraya gelecek]</p>
                            </div>
                        </div>
                    </div>
                    <div class="line-divider"></div>
                    <div class="padding-top padding-medium">
                        <div data-w-id="f0dfafb4-3a26-b6a3-fe71-34b55a052e83" class="footer_bottom-wrapper">
                            <div blocks-name="footer5_legal-list" blocks-slot-children="ST232" class="w-layout-grid footer_legal-list">
                                <div blocks-name="footer5_credit-text" id="w-node-f0dfafb4-3a26-b6a3-fe71-34b55a052e85-5a052e0b" class="footer_credit-text">© 2024 Matbaacı Mustafa - Tüm hakları saklıdır.</div>
                            </div>
                            <div blocks-name="footer5_social-icons" blocks-slot-children="ST232" class="w-layout-grid footer_social-icons">
                                <a blocks-name="footer5_social-link" href="https://facebook.com" target="_blank" class="footer_social-link w-inline-block">
                                    <div class="icon-embed-xsmall w-embed"><svg width="100%" height="100%" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                          d="M22 12.0611C22 6.50451 17.5229 2 12 2C6.47715 2 2 6.50451 2 12.0611C2 17.0828 5.65684 21.2452 10.4375 22V14.9694H7.89844V12.0611H10.4375V9.84452C10.4375 7.32296 11.9305 5.93012 14.2146 5.93012C15.3088 5.93012 16.4531 6.12663 16.4531 6.12663V8.60261H15.1922C13.95 8.60261 13.5625 9.37822 13.5625 10.1739V12.0611H16.3359L15.8926 14.9694H13.5625V22C18.3432 21.2452 22 17.083 22 12.0611Z"
                          fill="CurrentColor"></path>
                      </svg></div>
                                </a>
                                <a blocks-name="footer5_social-link-2" href="https://instagram.com" target="_blank" class="footer_social-link w-inline-block">
                                    <div class="icon-embed-xsmall w-embed"><svg width="100%" height="100%" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd"
                          d="M16 3H8C5.23858 3 3 5.23858 3 8V16C3 18.7614 5.23858 21 8 21H16C18.7614 21 21 18.7614 21 16V8C21 5.23858 18.7614 3 16 3ZM19.25 16C19.2445 17.7926 17.7926 19.2445 16 19.25H8C6.20735 19.2445 4.75549 17.7926 4.75 16V8C4.75549 6.20735 6.20735 4.75549 8 4.75H16C17.7926 4.75549 19.2445 6.20735 19.25 8V16ZM16.75 8.25C17.3023 8.25 17.75 7.80228 17.75 7.25C17.75 6.69772 17.3023 6.25 16.75 6.25C16.1977 6.25 15.75 6.69772 15.75 7.25C15.75 7.80228 16.1977 8.25 16.75 8.25ZM12 7.5C9.51472 7.5 7.5 9.51472 7.5 12C7.5 14.4853 9.51472 16.5 12 16.5C14.4853 16.5 16.5 14.4853 16.5 12C16.5027 10.8057 16.0294 9.65957 15.1849 8.81508C14.3404 7.97059 13.1943 7.49734 12 7.5ZM9.25 12C9.25 13.5188 10.4812 14.75 12 14.75C13.5188 14.75 14.75 13.5188 14.75 12C14.75 10.4812 13.5188 9.25 12 9.25C10.4812 9.25 9.25 10.4812 9.25 12Z"
                          fill="CurrentColor"></path>
                      </svg></div>
                                </a>
                                <a blocks-name="footer5_social-link-3" href="https://x.com" target="_blank" class="footer_social-link w-inline-block">
                                    <div class="icon-embed-xsmall w-embed"><svg width="100%" height="100%" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                          d="M17.1761 4H19.9362L13.9061 10.7774L21 20H15.4456L11.0951 14.4066L6.11723 20H3.35544L9.80517 12.7508L3 4H8.69545L12.6279 9.11262L17.1761 4ZM16.2073 18.3754H17.7368L7.86441 5.53928H6.2232L16.2073 18.3754Z"
                          fill="CurrentColor"></path>
                      </svg></div>
                                </a>
                                <a blocks-name="footer5_social-link-4" href="https://wa.me/905459700041" target="_blank" class="footer_social-link w-inline-block">
                                    <div class="icon-embed-xsmall w-embed"><svg width="100%" height="100%" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z" fill="CurrentColor"/>
                      </svg></div>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </footer>'''

# Tüm hizmetler sayfası
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Footer varsa değiştir, yoksa body kapanışından önce ekle
if '<footer class="footer_component">' in content:
    pattern = r'<footer class="footer_component">.*?</footer>'
    content = re.sub(pattern, yeni_footer, content, flags=re.DOTALL)
    print('Tüm hizmetler sayfası footer güncellendi!')
else:
    # Footer yoksa body kapanışından önce ekle
    content = content.replace('</body>', yeni_footer + '\n    </div>\n</body>')
    print('Tüm hizmetler sayfasına footer eklendi!')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
