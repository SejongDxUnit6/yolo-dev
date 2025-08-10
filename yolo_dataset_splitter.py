import os
import shutil
import random

# 📁 입력 폴더
source_root = "./sorted_images"  # 각 클래스별 이미지(.jpg/.png)와 라벨(.txt)이 있는 폴더

# 📁 출력 폴더 구조
train_img_root = "./dataset/images/train"
val_img_root = "./dataset/images/val"
train_label_root = "./dataset/labels/train"
val_label_root = "./dataset/labels/val"

# ⚙️ 설정
train_ratio = 0.8  # 8:2 비율

# ✅ 출력 폴더 생성
for path in [train_img_root, val_img_root, train_label_root, val_label_root]:
    os.makedirs(path, exist_ok=True)

# ✅ 클래스별 순회
for class_name in os.listdir(source_root):
    class_path = os.path.join(source_root, class_name)
    if not os.path.isdir(class_path):
        continue

    # 📦 이미지 파일 수집
    images = [f for f in os.listdir(class_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random.shuffle(images)  # 셔플

    # ✂️ 분할
    split_idx = int(len(images) * train_ratio)
    train_images = images[:split_idx]
    val_images = images[split_idx:]

    # 📤 Train 세트 복사
    for img in train_images:
        img_src = os.path.join(class_path, img)
        img_dst = os.path.join(train_img_root, img)
        shutil.copy2(img_src, img_dst)

        # 대응되는 라벨 복사
        label_name = os.path.splitext(img)[0] + ".txt"
        label_src = os.path.join(class_path, label_name)
        if os.path.exists(label_src):
            label_dst = os.path.join(train_label_root, label_name)
            shutil.copy2(label_src, label_dst)

    # 📤 Val 세트 복사
    for img in val_images:
        img_src = os.path.join(class_path, img)
        img_dst = os.path.join(val_img_root, img)
        shutil.copy2(img_src, img_dst)

        # 대응되는 라벨 복사
        label_name = os.path.splitext(img)[0] + ".txt"
        label_src = os.path.join(class_path, label_name)
        if os.path.exists(label_src):
            label_dst = os.path.join(val_label_root, label_name)
            shutil.copy2(label_src, label_dst)

    print(f"[✅ 분할 완료] {class_name}: Train={len(train_images)}, Val={len(val_images)}")

print("\n🎉 YOLO 데이터셋 분할 완료!")
