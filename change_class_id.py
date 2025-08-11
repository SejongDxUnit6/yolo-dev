import os

# 원본 COCO 카테고리ID → 한글명
item_dict = {
    174: "계산기",
    167: "마우스",
    156: "보조배터리",
    146: "무선이어폰",
    150: "스마트워치",
    141: "노트북",
    136: "태블릿펜",
    131: "태블릿",
    132: "무선헤드폰",
    133: "USB메모리",
    126: "휴대폰",
    127: "무선이어폰크래들",

    276: "반지",
    277: "팔찌",
    278: "목걸이",
    279: "귀걸이",
    280: "아날로그손목시계",

    299: "연필",
    300: "볼펜",
    314: "지우개",
    317: "필통",
    319: "샤프",
    323: "커터칼",
    324: "샤프심통",
    328: "자",

    457: "안경",
    464: "캡/야구 모자",
    466: "백팩",
    467: "지갑"
}

# 한글명 → YOLO 클래스 ID
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

# 변환할 폴더 경로
label_folder = r"D:\yolo-dev\dataset\labels\train"  # 경로 수정
# label_folder = r"D:\yolo-dev\dataset\labels\val"

for filename in os.listdir(label_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(label_folder, filename)

        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if not parts:
                continue

            try:
                category_id = int(parts[0])  # COCO 카테고리 ID
                if category_id in item_dict:
                    class_name = item_dict[category_id]
                    class_id = item_dict_reverse[class_name]
                    parts[0] = str(class_id)
                    new_lines.append(" ".join(parts))
                else:
                    print(f"[경고] {filename} → 알 수 없는 category_id: {category_id}")
            except ValueError:
                print(f"[오류] {filename} → 잘못된 라인: {line.strip()}")

        # 변환 결과 저장 (덮어쓰기)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines))

print("✅ 변환 완료!")
