from ultralytics import ASSETS, YOLO
import PIL.Image as Image

class YoloInference:
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name
        self.model = YOLO(self.model_name)
    
    def predict(self, img, conf_threshold, iou_threshold):
        results = self.model.predict(
            source=img,
            conf=conf_threshold,
            iou=iou_threshold,
            show_labels=True,
            show_conf=True,
            imgsz=640,
        )
        for r in results:
            im_array = r.plot()
            im = Image.fromarray(im_array[..., ::-1])

        return im