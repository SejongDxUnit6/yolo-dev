import os
import json

# YOLO 클래스 ID ↔️ 한글 클래스 이름
item_dict = {
    174: "계산기", 167: "마우스", 156: "보조배터리", 146: "무선이어폰", 150: "스마트워치",
    141: "노트북", 136: "태블릿펜", 131: "태블릿", 132: "무선헤드폰", 133: "USB메모리",
    126: "휴대폰", 127: "무선이어폰크래들", 276: "반지", 277: "팔찌", 278: "목걸이",
    279: "귀걸이", 280: "아날로그손목시계", 299: "연필", 300: "볼펜", 314: "지우개",
    317: "필통", 319: "샤프", 323: "커터칼", 324: "샤프심통", 328: "자", 457: "안경",
    464: "캡/야구 모자", 466: "백팩", 467: "지갑"
}

item_dict_reverse = {
    "계산기": 0,
    "마우스": 1,
    "보조배터리": 2,
    "무선이어폰": 3,
    "스마트워치": 4,
    "노트북": 5,
    "태블릿펜": 6,
    "태블릿": 7,
    "무선헤드폰": 8,
    "USB메모리": 9,
    "휴대폰": 10,
    "무선이어폰크래들": 11,
    "반지": 12,
    "팔찌": 13,
    "목걸이": 14,
    "귀걸이": 15,
    "아날로그손목시계": 16,
    "연필": 17,
    "볼펜": 18,
    "지우개": 19,
    "필통": 20,
    "샤프": 21,
    "커터칼": 22,
    "샤프심통": 23,
    "자": 24,
    "안경": 25,
    "캡/야구 모자": 26,
    "백팩": 27,
    "지갑": 28
}


# 전체 대상 처리 
source_roots = [
    ["./dataset/images/train", "./dataset/labels/train"],
    ["./dataset/images/val",  "./dataset/labels/val"]
]

for image_dir, label_dir in source_roots:
    os.makedirs(image_dir, exist_ok=True)
    os.makedirs(label_dir, exist_ok=True)

json_folder = r"./resources"
for source_root in source_roots:
    for file_name in os.listdir(source_root[0]):
        json_path = os.path.join(json_folder, file_name.split(".")[0] + ".json")
        if not os.path.exists(json_path):
            print(f"[⚠️ 없음] {json_path}")
            continue

        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        image_info = data.get("images", [{}])[0]
        ann_list = data.get("annotations", [])

        img_w = image_info.get("width")
        img_h = image_info.get("height")
        if not (img_w and img_h):
            print(f"[무시됨] {file_name}.json → 이미지 크기 없음")
            continue

        # 클래스 ID 추출 (첫 항목 기준)
        if not ann_list:
            print(f"[무시됨] {file_name}.json → bbox 없음")
            continue

        for ann in ann_list:
            category_id = ann.get("category_id")
            bbox = ann.get("bbox")

            if category_id not in item_dict or not bbox:
                print(f"[무시됨] {file_name}.json → 알 수 없는 클래스 ID: {category_id}")
                continue

            class_name = item_dict[category_id]
            class_id = item_dict_reverse[class_name]
                
            x, y, w, h = bbox
            x_center = (x + w / 2) / img_w
            y_center = (y + h / 2) / img_h
            w_norm = w / img_w
            h_norm = h / img_h

            yolo_line = f"{class_id} {x_center:.6f} {y_center:.6f} {w_norm:.6f} {h_norm:.6f}\n"

            yolo_txt_path = os.path.join(source_root[1], file_name.split(".")[0] + ".txt")

            with open(yolo_txt_path, 'a', encoding='utf-8') as out:
                out.write(yolo_line)

        print(f"[✅ 완료] {file_name}.json → {yolo_txt_path}.txt")

print("\n🎉 지정된 JSON 파일만 YOLO 포맷으로 변환 완료!")
