# This Python file uses the following encoding: utf-8
import cv2
import numpy as np
from ultralytics import YOLO  # YOLOv8 官方库
from pathlib import Path
from typing import Union, List, Dict


class YOLOv8Detector:
    def __init__(self, model_path: str = "trained_model_by_amns.onnx", conf_threshold: float = 0.5, iou_threshold: float = 0.5):
        """
        初始化YOLOv8检测器
        
        参数:
            model_path: 预训练模型路径 (.pt文件)
            conf_threshold: 置信度阈值 (0-1)
            iou_threshold: IoU阈值 (0-1)
        """
        self.model = YOLO(model_path)
        self.conf_threshold = conf_threshold
        self.iou_threshold = iou_threshold
        self.class_names = self.model.names

    def detect(self, input_image: Union[str, np.ndarray, Path]) -> tuple[np.ndarray, List[Dict]]:
        """
        执行目标检测并返回带标注的结果图像和检测信息
        
        参数:
            input_image: 输入图像 (文件路径、numpy数组或Path对象)
        
        返回:
            annotated_image: 带标注的图像 (numpy数组)
            detections: 检测结果列表 (结构化数据)
        """
        # 处理不同类型的输入
        if isinstance(input_image, (str, Path)):
            image = cv2.imread(str(input_image))
            if image is None:
                raise ValueError(f"无法读取图像: {input_image}")
        elif isinstance(input_image, np.ndarray):
            image = input_image.copy()
        else:
            raise TypeError("不支持的图像类型,请使用路径字符串、numpy数组或Path对象")
        
        # 执行推理
        results = self.model.predict(
            image,
            conf=self.conf_threshold,
            iou=self.iou_threshold,
            verbose=False
        )
        
        # 获取检测结果和带标注图像
        annotated_image = results[0].plot()
        detections = self._parse_results(results[0])
        
        return annotated_image, detections

    def _parse_results(self, result) -> List[Dict]:
        """解析YOLO结果对象为结构化数据"""
        detections = []
        
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            
            detection = {
                "bbox": [x1, y1, x2, y2],
                "confidence": float(box.conf.item()),
                "class_id": int(box.cls.item()),
                "class_name": self.class_names[int(box.cls.item())]
            }
            detections.append(detection)
         
        return detections

    def save_result(self, image: np.ndarray, output_path: Union[str, Path]) -> None:
        """
        保存结果图像到文件
        
        参数:
            image: 带标注的图像 (numpy数组)
            output_path: 输出文件路径
        """
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        cv2.imwrite(str(output_path), image)

    def draw_defects(self, image: np.ndarray, defects: List[Dict], 
                 bbox_color: tuple[int, int, int] = (0, 0, 255),  # 默认红色
                 text_color: tuple[int, int, int] = (255, 255, 255),  # 默认白色
                 line_width: int = 2,
                 font_scale: float = 0.7) -> np.ndarray:
        """
        在图像上绘制缺陷标识
    
        参数:
            image: 原始图像 (numpy数组)
            defects: 缺陷列表 (包含bbox, class_name, confidence等)
            bbox_color: 边界框颜色 (BGR格式)
            text_color: 文本颜色 (BGR格式)
            line_width: 边界框线宽
            font_scale: 文本大小比例
        
        返回:
            绘制了缺陷标识的图像 (numpy数组)
        """
        # 创建图像的副本，避免修改原始图像
        result_image = image.copy()
    
        # 遍历所有缺陷
        for defect in defects:
            # 获取边界框坐标
            x1, y1, x2, y2 = defect["bbox"]
        
            # 绘制边界框
            cv2.rectangle(
                img=result_image,
                pt1=(x1, y1),
                pt2=(x2, y2),
                color=bbox_color,
                thickness=line_width
            )
        
            # 准备文本标签
            label = f"{defect['class_name']} {defect['confidence']:.2f}"
        
            # 计算文本位置
            (text_width, text_height), _ = cv2.getTextSize(
                label, 
                cv2.FONT_HERSHEY_SIMPLEX, 
                font_scale, 
                thickness=line_width
            )
        
            # 绘制文本背景
            cv2.rectangle(
                img=result_image,
                pt1=(x1, y1 - text_height - 5),
                pt2=(x1 + text_width, y1),
                color=bbox_color,
                thickness=cv2.FILLED
            )
        
            # 绘制文本
            cv2.putText(
                img=result_image,
                text=label,
                org=(x1, y1 - 5),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=font_scale,
                color=text_color,
                thickness=line_width,
                lineType=cv2.LINE_AA
            )
    
        return result_image
    