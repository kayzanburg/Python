import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Müzik Çalar")
        self.root.geometry("400x280")

        self.current_directory = os.getcwd()
        self.playlist = []

        self.music_index = 0
        self.paused = False

        self.initialize_ui()
        self.load_music()

    def initialize_ui(self):
        # Butonlar
        self.btn_browse = tk.Button(self.root, text="Müzik Seç", command=self.browse_music)
        self.btn_play_pause = tk.Button(self.root, text="Oynat/Duraklat", command=self.play_pause_music)
        self.btn_previous = tk.Button(self.root, text="Önceki", command=self.play_previous)
        self.btn_next = tk.Button(self.root, text="Sonraki", command=self.play_next)

        # Etiket - Çalan Müzik
        self.lbl_current_music = tk.Label(self.root, text="")

        # Sürükleyici (Slider) - Ses düzeyi
        self.volume_slider = tk.Scale(self.root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, label="Ses Düzeyi", command=self.change_volume)

        # Widget'ları yerleştirme
        self.btn_browse.pack(pady=10)
        self.btn_play_pause.pack(pady=5)
        self.btn_previous.pack(pady=5)
        self.btn_next.pack(pady=5)
        self.lbl_current_music.pack(pady=5)
        self.volume_slider.pack(pady=5)

    def browse_music(self):
        file_path = filedialog.askopenfilename(initialdir=self.current_directory, title="Müzik Seç", filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            self.playlist.append(file_path)
            self.play_music()

    def load_music(self):
        pygame.mixer.init()

    def play_music(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.music_index])
            pygame.mixer.music.set_volume(self.volume_slider.get())  # Ses düzeyini ayarla
            pygame.mixer.music.play()
            self.lbl_current_music.config(text=os.path.basename(self.playlist[self.music_index]))  # Çalan müzik adını ekrana yazdır
        else:
            print("Oynatılacak müzik yok.")

    def play_pause_music(self):
        if self.playlist:
            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
            else:
                pygame.mixer.music.pause()
                self.paused = True
        else:
            print("Oynatılacak müzik yok.")

    def play_previous(self):
        if self.playlist:
            self.music_index = (self.music_index - 1) % len(self.playlist)
            self.play_music()

    def play_next(self):
        if self.playlist:
            self.music_index = (self.music_index + 1) % len(self.playlist)
            self.play_music()

    def change_volume(self, volume):
        if self.playlist:
            pygame.mixer.music.set_volume(float(volume))

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
