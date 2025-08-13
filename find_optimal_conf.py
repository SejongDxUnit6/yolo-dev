import numpy as np
from ultralytics import YOLO
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # 윈도우 기본 한글 폰트
matplotlib.rcParams['axes.unicode_minus'] = False

if __name__=='__main__':
    # 모델 로드
    model = YOLO("results/train1/weights/best.pt")  # 경로는 상황에 맞게 수정

    # 테스트할 conf 범위 설정
    conf_range = np.arange(0.1, 0.91, 0.05)

    # 결과 저장용
    conf_scores = []

    for conf in conf_range:
        metrics = model.val(conf=conf, save=False, verbose=False)
        precision = metrics.box.p[0]  # class 평균 precision
        recall = metrics.box.r[0]     # class 평균 recall
        
        # F1 score 계산
        if precision + recall > 0:
            f1_score = 2 * (precision * recall) / (precision + recall)
        else:
            f1_score = 0.0

        print(f"conf: {conf:.2f} | Precision: {precision:.3f}, Recall: {recall:.3f}, F1: {f1_score:.3f}")
        conf_scores.append((conf, f1_score))

    # 최적 conf 선택
    best_conf, best_f1 = max(conf_scores, key=lambda x: x[1])
    print(f"\n최적 conf: {best_conf:.2f} (F1 Score: {best_f1:.3f})")

""" 최적 conf: 0.50 (F1 Score: 0.886) """