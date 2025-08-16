from ultralytics import YOLO
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # 윈도우 기본 한글 폰트
matplotlib.rcParams['axes.unicode_minus'] = False

def val(model_path, data_yaml):
    # 모델 경로 설정
    model = YOLO(model_path)

    # 모델1 성능 평가
    metrics = model.val(data=data_yaml, split="val")
    print("\n[모델 성능]")
    print(f"mAP50: {metrics.box.map50:.4f}")
    print(f"mAP50-95: {metrics.box.map:.4f}")
    print(f"Precision: {metrics.box.mp:.4f}")
    print(f"Recall: {metrics.box.mr:.4f}")

if __name__=='__main__':
    val('results/train1/weights/best.pt','./config.yaml')
    val('results/train12/weights/best.pt','./config.yaml')
    val('results/train13/weights/best.pt','./config.yaml')
    val('results/train2/weights/best.pt','./config.yaml')
    val('results/train22/weights/best.pt','./config.yaml')

"""
train1
[모델 성능]
mAP50: 0.7026
mAP50-95: 0.5888
Precision: 0.6559
Recall: 0.6722

train13
[모델 성능]
mAP50: 0.7161
mAP50-95: 0.5994
Precision: 0.7744
Recall: 0.6092

train222
[모델 성능]
mAP50: 0.6828
mAP50-95: 0.5651
Precision: 0.6789
Recall: 0.6233
"""