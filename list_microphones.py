# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 05:43:16 2026

@author: ProfGerald
"""


import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def list_microphones():
    mic_list = sr.Microphone.list_microphone_names()
    for index, name in enumerate(mic_list):
        print(f"Microphone {index}: {name}")
    return mic_list

list_microphones()

