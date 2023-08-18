from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

stage_name = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>Stage {stage_name} started <<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>Stage {stage_name} completed <<<<<<<<<")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"f****************")
    logger.info(f">>>>>>Stage {STAGE_NAME} completed <<<<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>Stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e