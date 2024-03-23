from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import gradio as gr
import sys
from src.utils.logger import logger
from src.utils.config import Config
from src.core.yolov8 import YoloInference
from ultralytics import ASSETS

class Server:
    def __init__(self):
        root_config_dir = "configs"
        logger.debug(f"Root config dir: {root_config_dir}")

        self.config = Config(root_config_dir)
        logger.debug("Configs Loaded...")

        self.yolo = YoloInference(self.config.obj_detector.detection_model.model_name)

    def gradio_server(self):
        im_inp = gr.Image(type="pil", label="Input Image")
        cnf_thr = gr.Slider(minimum=0, maximum=1, value=0.25, label="Confidence threshold")
        iou_thr = gr.Slider(minimum=0, maximum=1, value=0.45, label="IoU threshold")
        im_out = gr.Image(type="pil", label="Output Image")
        demo = gr.Interface(
            fn=self.yolo.predict,
            inputs=[
                im_inp,
                cnf_thr,
                iou_thr
            ],
            outputs=im_out,
            title="Gradio Demo",
            description="Upload images for inference. The Ultralytics YOLOv8n model is used by default.",
            examples=[
                    [ASSETS / "bus.jpg", 0.25, 0.45],
                    [ASSETS / "zidane.jpg", 0.25, 0.45],
                ]
            )
        try:
            demo.launch(server_name = self.config.obj_detector.server.host, server_port = self.config.obj_detector.server.port)
        except KeyboardInterrupt:
            print("\n")
            logger.error("Keyboard Interrupted...")
            sys.exit(0)
        except Exception as e:
            logger.error(f"Error: {e}")
            sys.exit(0)
