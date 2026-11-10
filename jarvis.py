import webbrowser
import os
import speech_recognition as sr

# 1. Buka website di Chrome
chrome = "C:/Users/EKA/AppData/Local/Google/Chrome/Application/chrome.exe %s"

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    while True:
        print("Bicara sekarang...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

        try:
            teks = recognizer.recognize_google(audio, language="id-ID").lower()
            print("Kamu bilang:", teks)
            if "youtube" in teks:
                webbrowser.get(chrome).open("https://www.youtube.com")
            elif "discord" in teks:
                webbrowser.get(chrome).open("https://discord.com/channels/@me")
            elif "minecraft" in teks:
                os.startfile("minecraft:")
            elif "wa" in teks:
                webbrowser.get(chrome).open("https://web.whatsapp.com/")
            elif "vs code" in teks:
                
            elif "cukup" in teks:
                break
        except sr.UnknownValueError:
            print("Suara tidak terdengar jelas")
        except sr.RequestError:
            print("Gagal konek ke internet")
            