import pyxel
import PyxelUniversalFont as puf
from .utils import *

from pynput import keyboard
import pykakasi
import random

class Params:
    WINDOW_SIZE = (400,100)
    SOURCE = get_data_path("data/img.pyxres")
    FONT_SIZE = 16
    NAME = input("彼女の名前：")
    if NAME == "":
        NAME = "きみ"
    DICT = load_vocabulary_from_file(get_data_path("data/vocab.txt"), NAME)

class App:
    def __init__(self, params:Params) -> None:
        # initialize window
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = params.WINDOW_SIZE
        pyxel.init(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        
        # load data
        pyxel.load(params.SOURCE)
        
        # initialize variables
        self._reset(params)
        
        # run app
        pyxel.run(self._update, self._draw)
    
    # initialize variables
    def _reset(self, params:Params):
        self.params = params
        self.writer = puf.Writer("misaki_gothic2.ttf")
        self.text = " "
        self.position = 0
        
        self.current_key = None
        self.shift_pressed = False
        self.listener = keyboard.Listener(on_press=self._on_press, on_release=self._on_release)
        self.listener.start()
        
        self.kks = pykakasi.kakasi()
        self._get_new_target()
    
    def _on_press(self, key):
        if key == keyboard.Key.shift:
            self.shift_pressed = True
        elif hasattr(key, 'char') and key.char:
            self.current_key = key.char.upper() if self.shift_pressed else key.char

    def _on_release(self, key):
        if key == keyboard.Key.shift:
            self.shift_pressed = False
        
    def _add_text(self, character):
        if self.answer_text[self.position] == character:
            self.text = self.text[:-1] + character
            self.text += " "
            self.position += 1
    
    def _get_roma(self, text):
        result = ""
        text_converted = self.kks.convert(text)
        for word in text_converted:
            result += word['passport']
        return result
    
    def _get_new_target(self):
        message, answer = random.choice(self.params.DICT)
        self.message = message
        self.target_text = answer
        self.answer_text = self._get_roma(answer)
        self.text = " "
        self.position = 0
    
    def _correct(self):
        return self.answer_text == self.text[:-1]
    
    # process
    def _update(self):
        
        if pyxel.btnp(pyxel.KEY_SPACE):
            self._add_text(" ")
        if self.current_key:
            self._add_text(self.current_key)
            self.current_key = None
        
        if self.position == len(self.answer_text):
            self._get_new_target()
    
    # visualize
    def _draw(self):
        pyxel.cls(0)
        
        font_size = self.params.FONT_SIZE
        line_height = font_size + 2
        
        self.writer.draw(0, line_height*1, self.message, font_size, 7)
        self.writer.draw(0, line_height*3, self.target_text, font_size, 7)
        self.writer.draw(0, line_height*4, self.answer_text, font_size, 7)
        self.writer.draw(0, line_height*4, self.text, font_size, 5)