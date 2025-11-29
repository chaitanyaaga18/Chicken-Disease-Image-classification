from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline


if __name__ == "__main__":
    try:
        logger.info("******************* PIPELINE STARTED *******************")

        # 1. Data ingestion (will just skip download for you)
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()

        # 2. Prepare base model
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()

        # 3. Train model
        model_trainer = ModelTrainingPipeline()
        model_trainer.main()

        # 4. Evaluate model (optional but will run)
        evaluation = EvaluationPipeline()
        evaluation.main()

        logger.info("******************* PIPELINE FINISHED *******************")

    except Exception as e:
        logger.exception(e)
        raise e
