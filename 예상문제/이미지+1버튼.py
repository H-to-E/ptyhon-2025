import tkinter as tk
from PIL import ImageTk, Image
import os

# 현재 파이썬 파일이 있는 폴더 경로
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def update_image():
    """현재 인덱스에 해당하는 이미지를 화면에 표시"""
    global current_index
    image_path = os.path.join(BASE_DIR, images[current_index])

    image = Image.open(image_path)
    image = image.resize((400, 300))  # 이미지 크기 조정

    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo  # 이미지가 사라지지 않도록 참조 유지

def next_image():
    """버튼을 누를 때마다 다음 이미지로 변경"""
    global current_index
    current_index = (current_index + 1) % len(images)  # 마지막 이미지 다음엔 첫 번째로
    update_image()

# Tkinter 기본 설정
root = tk.Tk()
root.title("단일 버튼 이미지 슬라이더")

# 이미지 파일 목록
images = ['image1.png', 'image2.png', 'image3.png', 'image4.png']
current_index = 0  # 현재 이미지 인덱스

# 이미지 표시 라벨
image_label = tk.Label(root)
image_label.pack(padx=10, pady=10)

# 다음 이미지로 넘기는 버튼 (하나만)
next_button = tk.Button(root, text="다음 이미지 ▶", command=next_image, width=20, height=2)
next_button.pack(pady=10)

# 첫 번째 이미지 표시
update_image()

# 메인 루프 실행
root.mainloop()

