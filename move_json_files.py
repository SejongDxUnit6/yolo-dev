import os
import shutil

# 주어진 폴더 리스트
json_folders = [
    r'C:\Users\user\Downloads\037.Small object detection을 위한 이미지 데이터\01.데이터\2.Validation\2.라벨링데이터\VL_보석_귀금속_시계\mnt\nas2\Projects\TTA_2022_jgcha\jhbae\037.Small object detection을 위한 이미지 데이터\01.데이터\2.Validation\2.라벨링데이터\VL_보석_귀금속_시계\jewlery01',
    r'C:\Users\user\Downloads\037.Small object detection을 위한 이미지 데이터\01.데이터\2.Validation\2.라벨링데이터\VL_문구류\mnt\nas2\Projects\TTA_2022_jgcha\jhbae\037.Small object detection을 위한 이미지 데이터\01.데이터\2.Validation\2.라벨링데이터\VL_문구류\stationary01',
    r'C:\Users\user\Downloads\037.Small object detection을 위한 이미지 데이터\01.데이터\2.Validation\2.라벨링데이터\VL_전자기기\mnt\nas2\Projects\TTA_2022_jgcha\jhbae\037.Small object detection을 위한 이미지 데이터\01.데이터\2.Validation\2.라벨링데이터\VL_전자기기\electronics01',
    r'C:\Users\user\Downloads\037.Small object detection을 위한 이미지 데이터\01.데이터\2.Validation\2.라벨링데이터\VL_피혁_잡화\mnt\nas2\Projects\TTA_2022_jgcha\jhbae\037.Small object detection을 위한 이미지 데이터\01.데이터\2.Validation\2.라벨링데이터\VL_피혁_잡화\leather01'
]

# 이동할 목적지 폴더
target_dir = r"./dataset/labels/resources"
os.makedirs(target_dir, exist_ok=True)

# 각 폴더 순회하며 json 이동
for folder in json_folders:
    if not os.path.exists(folder):
        print(f"경로 없음: {folder}")
        continue

    for file_name in os.listdir(folder):
        if file_name.lower().endswith(".json"):
            src_path = os.path.join(folder, file_name)
            dst_path = os.path.join(target_dir, file_name)

            # 이름 중복 시 번호 붙이기
            base, ext = os.path.splitext(file_name)
            counter = 1
            while os.path.exists(dst_path):
                dst_path = os.path.join(target_dir, f"{base}_{counter}{ext}")
                counter += 1

            shutil.move(src_path, dst_path)
            print(f"이동: {src_path} → {dst_path}")

print("모든 JSON 이동 완료.")
