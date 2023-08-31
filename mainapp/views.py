
from django.shortcuts import render, HttpResponse
from google.cloud import texttospeech_v1beta1
import string
import random
import os
import shutil

from django.http import HttpResponse

def image_view(request):
    image_path = "/Users/vhmt.vn/Library/Mobile Documents/com~apple~CloudDocs/google/sound/tim.png"  # Thay đổi đường dẫn đến hình ảnh của bạn
    
    with open(image_path, 'rb') as f:
        return HttpResponse(f.read(), content_type='image/jpeg')

def index_page(request):
    client = texttospeech_v1beta1.TextToSpeechClient()
    if request.method == "POST":
        text = request.POST['text']
        tdl = request.POST['tdl']
        index_page.call_count = getattr(index_page, 'call_count', int(tdl)) + 1
        file_name = f"{index_page.call_count}.mp3"
        synthesis_input = texttospeech_v1beta1.SynthesisInput(text=text)
        voice = texttospeech_v1beta1.VoiceSelectionParams(
            language_code='vi-vn', name='vi-VN-Wavenet-C'
        )
        audio_config = texttospeech_v1beta1.AudioConfig(
            audio_encoding=texttospeech_v1beta1.AudioEncoding.MP3, speaking_rate=1.1,
        )
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        mp3_content = response.audio_content
        file_name = f"{index_page.call_count}.mp3"
        response = HttpResponse(mp3_content, content_type='audio/mpeg')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response
    return render(request, 'index.html')
