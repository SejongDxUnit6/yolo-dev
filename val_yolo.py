from ultralytics import YOLO
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # 윈도우 기본 한글 폰트
matplotlib.rcParams['axes.unicode_minus'] = False

def val(model_path, data_yaml):
    # 모델 경로 설정
    model = YOLO(model_path)

    # 모델1 성능 평가
    metrics = model.val(data=data_yaml, split="val", project="results", name="val1")
    print("\n[모델 성능]")
    print(f"mAP50: {metrics.box.map50:.4f}")
    print(f"mAP50-95: {metrics.box.map:.4f}")
    print(f"Precision: {metrics.box.mp:.4f}")
    print(f"Recall: {metrics.box.mr:.4f}")

if __name__=='__main__':
    val('results/train1/weights/best.pt','./config.yaml')
    val('results/train12/weights/best.pt','./config.yaml')
    val('results/train13/weights/best.pt','./config.yaml')
