from core.yolo.yolo_manager import YoloManager

if __name__=="__main__":
    model = YoloManager(model_path="yolov8s.pt")
    model.train_yolo(
        config_path="config.yaml",
        epochs=20,              # 추가로 10 epoch만 학습
        imgsz=640,
        batch=4,
        resume=False,           # "이어하기"가 아니라 "새로운 학습"으로 처리
        project="results",
        name="train1",  
        patience=5              # 5 epoch 동안 개선 없으면 자동 종료
    )