# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:19:17 2024

@author: kokol
"""

from transformers import pipeline
import gradio as gr

import os
from os.path import abspath, join


pipe = pipeline("translation_en_to_de", model='t5-base', device = 0)
#pipe.save_pretrained(pt_save_directory)

def translateText(text):
    return pipe(text)[0]['translation_text']


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            english = gr.Textbox(label='English text',
                                 lines = 5,
                                 info = 'Insert your english text here please.')
            translate_btn = gr.Button(value = 'Translate' )
            
                
        with gr.Column():
            german = gr.Textbox(label = 'German text',
                                lines = 5,
                                info = 'Here is your text in german.')
            clear_btn = gr.ClearButton( components=[english, german])
    
    translate_btn.click(translateText, inputs=english, outputs=german)
    
        
    examples = gr.Examples(['I went to the supermarket yesterday.', 'You are a good swimmer!'], inputs=english)
    
    
demo.launch(share=False)