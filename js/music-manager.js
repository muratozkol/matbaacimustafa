/**
 * 🎵 KUSURSUZ MÜZİK SİSTEMİ v2.0
 * Sayfa geçişlerinde ASLA kapanmaz!
 * Tüm sitelerde çalışır: Ana sayfa, Davetiyeler, Hizmetler, İletişim
 */

(function() {
    'use strict';
    
    // Müzik manager zaten varsa çık
    if (window.MusicManager) {
        window.MusicManager.resume();
        return;
    }
    
    const MusicManager = {
        player: null,
        initialized: false,
        autoplayAttempted: false,
        
        // Config
        CONFIG: {
            VOLUME: 0.3,
            SAVE_INTERVAL: 300, // Her 300ms'de kaydet (daha sık)
            STORAGE_KEY_TIME: 'bgMusicTime',
            STORAGE_KEY_PLAYING: 'bgMusicPlaying',
            STORAGE_KEY_VOLUME: 'bgMusicVolume',
            MUSIC_PATH: null // Dinamik olarak ayarlanacak
        },
        
        init: function() {
            if (this.initialized) return;
            
            // Müzik yolunu belirle (hangi sayfada olduğumuza göre)
            const isSubPage = window.location.pathname.includes('/davetiyeler/') || 
                            window.location.pathname.includes('/hizmetler/') || 
                            window.location.pathname.includes('/iletisim/');
            
            this.CONFIG.MUSIC_PATH = isSubPage ? '../music.mp3' : 'music.mp3';
            
            // Player'ı oluştur veya bul
            this.player = document.getElementById('globalMusicPlayer');
            
            if (!this.player) {
                this.createPlayer();
            }
            
            this.setupEventListeners();
            this.restoreState();
            this.startAutoSave();
            this.initialized = true;
            
            console.log('🎵 Müzik Manager Initialize Edildi');
        },
        
        createPlayer: function() {
            this.player = document.createElement('audio');
            this.player.id = 'globalMusicPlayer';
            this.player.loop = true;
            this.player.volume = this.CONFIG.VOLUME;
            this.player.preload = 'auto';
            this.player.src = this.CONFIG.MUSIC_PATH;
            
            // Hidden player
            this.player.style.cssText = 'position:absolute;left:-9999px;';
            document.body.appendChild(this.player);
            
            console.log('🎵 Player oluşturuldu:', this.CONFIG.MUSIC_PATH);
        },
        
        setupEventListeners: function() {
            // Sayfa değişimi öncesi kaydet
            window.addEventListener('beforeunload', () => this.saveState());
            window.addEventListener('pagehide', () => this.saveState());
            
            // Visibility değişimi
            document.addEventListener('visibilitychange', () => {
                if (document.hidden) {
                    this.saveState();
                } else {
                    // Sayfa geri gelince devam ettir
                    this.resume();
                }
            });
            
            // Player events
            this.player.addEventListener('volumechange', () => {
                sessionStorage.setItem(this.CONFIG.STORAGE_KEY_VOLUME, this.player.volume);
            });
            
            this.player.addEventListener('ended', () => {
                // Loop olmasına rağmen bazen trigger olabilir
                this.player.currentTime = 0;
                this.player.play().catch(e => console.log('Play error:', e));
            });
            
            this.player.addEventListener('error', (e) => {
                console.error('🎵 Müzik yükleme hatası:', e);
                // 2 saniye sonra tekrar dene
                setTimeout(() => {
                    this.player.load();
                    if (this.isPlaying()) {
                        this.play();
                    }
                }, 2000);
            });
            
            // Canplay event - müzik yüklendiğinde
            this.player.addEventListener('canplaythrough', () => {
                if (!this.autoplayAttempted) {
                    this.autoplayAttempted = true;
                    this.attemptAutoplay();
                }
            }, { once: true });
        },
        
        restoreState: function() {
            // Saved volume
            const savedVolume = sessionStorage.getItem(this.CONFIG.STORAGE_KEY_VOLUME);
            if (savedVolume) {
                this.player.volume = parseFloat(savedVolume);
            }
            
            // Saved time
            const savedTime = parseFloat(sessionStorage.getItem(this.CONFIG.STORAGE_KEY_TIME) || 0);
            if (savedTime > 0) {
                this.player.currentTime = savedTime;
            }
            
            // Saved playing state
            const wasPlaying = sessionStorage.getItem(this.CONFIG.STORAGE_KEY_PLAYING) === 'true';
            if (wasPlaying) {
                this.play();
            }
        },
        
        attemptAutoplay: function() {
            const wasPlaying = sessionStorage.getItem(this.CONFIG.STORAGE_KEY_PLAYING) === 'true';
            
            if (!wasPlaying) {
                // İlk ziyaret - kullanıcı etkileşimi bekle
                this.setupUserInteractionTriggers();
            } else {
                // Daha önce çalıyordu - devam ettir
                this.play();
            }
        },
        
        setupUserInteractionTriggers: function() {
            const events = [
                'click', 'touchstart', 'touchmove', 'touchend',
                'mousedown', 'mousemove', 'mouseup',
                'keydown', 'keypress', 'scroll', 'wheel'
            ];
            
            const triggerPlay = () => {
                this.play();
                // Tüm listener'ları kaldır
                events.forEach(event => {
                    document.removeEventListener(event, triggerPlay);
                });
            };
            
            // Her event'e listener ekle
            events.forEach(event => {
                document.addEventListener(event, triggerPlay, { once: true, passive: true });
            });
            
            console.log('🎵 Kullanıcı etkileşimi bekleniyor...');
        },
        
        play: function() {
            if (!this.player) return;
            
            const playPromise = this.player.play();
            
            if (playPromise !== undefined) {
                playPromise.then(() => {
                    sessionStorage.setItem(this.CONFIG.STORAGE_KEY_PLAYING, 'true');
                    console.log('🎵 Müzik çalıyor');
                }).catch(err => {
                    console.log('🎵 Autoplay engellendi:', err.message);
                    if (err.name !== 'NotAllowedError') {
                        // Gerçek bir hata - tekrar dene
                        setTimeout(() => this.play(), 1000);
                    } else {
                        // Autoplay policy - kullanıcı etkileşimi gerekli
                        this.setupUserInteractionTriggers();
                    }
                });
            }
        },
        
        pause: function() {
            if (this.player && !this.player.paused) {
                this.player.pause();
                sessionStorage.setItem(this.CONFIG.STORAGE_KEY_PLAYING, 'false');
            }
        },
        
        resume: function() {
            const wasPlaying = sessionStorage.getItem(this.CONFIG.STORAGE_KEY_PLAYING) === 'true';
            const savedTime = parseFloat(sessionStorage.getItem(this.CONFIG.STORAGE_KEY_TIME) || 0);
            
            if (wasPlaying) {
                if (savedTime > 0 && this.player.currentTime < savedTime) {
                    this.player.currentTime = savedTime;
                }
                this.play();
            }
        },
        
        saveState: function() {
            if (!this.player) return;
            
            const isPlaying = !this.player.paused;
            const currentTime = this.player.currentTime;
            
            sessionStorage.setItem(this.CONFIG.STORAGE_KEY_PLAYING, isPlaying.toString());
            sessionStorage.setItem(this.CONFIG.STORAGE_KEY_TIME, currentTime.toString());
            
            console.log('🎵 State kaydedildi:', { isPlaying, currentTime: currentTime.toFixed(2) });
        },
        
        startAutoSave: function() {
            // Her 300ms'de bir otomatik kaydet
            setInterval(() => {
                if (this.player && !this.player.paused && this.player.currentTime > 0) {
                    sessionStorage.setItem(this.CONFIG.STORAGE_KEY_TIME, this.player.currentTime.toString());
                }
            }, this.CONFIG.SAVE_INTERVAL);
        },
        
        isPlaying: function() {
            return this.player && !this.player.paused;
        },
        
        getCurrentTime: function() {
            return this.player ? this.player.currentTime : 0;
        },
        
        setVolume: function(volume) {
            if (this.player) {
                this.player.volume = Math.max(0, Math.min(1, volume));
            }
        }
    };
    
    // Global erişim için
    window.MusicManager = MusicManager;
    
    // Sayfa yüklendikten sonra initialize et
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => MusicManager.init());
    } else {
        MusicManager.init();
    }
    
})();
