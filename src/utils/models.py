from pydantic import BaseModel

class LoggerModel(BaseModel):
    environment: str


class ServerModel(BaseModel):
    host: str
    port: int

class DetectionModel(BaseModel):
    model_name: str
    conf_threshold: float
    iou_threshold: float

class Model(BaseModel):
    logger: LoggerModel
    server: ServerModel
    detection_model: DetectionModel
