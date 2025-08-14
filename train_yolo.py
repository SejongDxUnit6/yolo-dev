from core.yolo.yolo_manager import YoloManager
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # 윈도우 기본 한글 폰트
matplotlib.rcParams['axes.unicode_minus'] = False

if __name__=="__main__":
    # model = YoloManager(model_path="yolov8s.pt")
    # model.train_yolo(
    #     config_path="config.yaml",
    #     epochs=26,              # 추가로 10 epoch만 학습
    #     imgsz=768,
    #     batch=8,
    #     resume=False,           # "이어하기"가 아니라 "새로운 학습"으로 처리
    #     project="results",
    #     name="train2",  
    #     patience=5              # 5 epoch 동안 개선 없으면 자동 종료
    # )

    model = YoloManager(model_path="results/train222/weights/best.pt")
    model.train_yolo(
        config_path="config.yaml",
        epochs=1,              # 추가로 10 epoch만 학습
        imgsz=768,
        batch=8,
        resume=False,           # "이어하기"가 아니라 "새로운 학습"으로 처리
        project="results",
        name="train22"
    )