import moviepy.editor
from pathlib import Path#код который берет название видео файла и создает аудиофайл под таким же названием
video_file=Path('Тренировка при СИДЯЧЕМ ОБРАЗЕ ЖИЗНИ и ОФИСНОЙ РАБОТЕ 💻 _ SMSTRETCHING2.mp4')#получаем путь до нашего видео файла

#укажем с каким файлом нужно работать
video=moviepy.editor.VideoFileClip(f'{video_file}')#обращаемся к к классу видеофайлклип(передаем ему путь)
audio=video.audio#далее получаем аудио дорожку из файла, обратившись к атрибуту одио
#Сохраняем аудиодорожку в файл
audio.write_audiofile(f'{video_file.stem}.mp3')

