from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

stage_name = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>Stage {stage_name} started <<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>Stage {stage_name} completed <<<<<<<<<")
except Exception as e:
    logger.error(f"Stage {stage_name} failed")
