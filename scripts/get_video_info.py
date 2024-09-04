import os
import cv2
import sys
import argparse

def get_video_info(video_path):
    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        return None

    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    duration = frame_count / fps

    video.release()
    return {
        'duration': duration,
        'resolution': f'{width}x{height}',
        'fps': fps
    }

parser = argparse.ArgumentParser(description='Validation / Info')
parser.add_argument('video_path', type=str, help='video file path')

args = parser.parse_args()
video_path = args.video_path

# Проверка существования файла
if not os.path.isfile(video_path):
    raise Exception('Файл не существует. Пожалуйста, попробуйте снова.')

# Проверка расширения файла
if not video_path.lower().endswith('.mp4'):
    raise Exception('Видео должно иметь расширение mp4. Пожалуйста, повторите.')

# Получение информации о видео
video_info = get_video_info(video_path)

# Проверка, удалось ли открыть видео
if video_info is None:
    raise Exception('Не удалось открыть видео. Пожалуйста, выберите другой файл.')

# Вывод информации о видео
print(f'Информация о видео: {video_info}')