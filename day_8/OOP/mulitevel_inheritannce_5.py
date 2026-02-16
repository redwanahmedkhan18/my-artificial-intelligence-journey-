class DataPipeline:
    def process(self):
        print("Processing raw data")

class MLModel(DataPipeline):
    def process(self):
        super().process()
        print("Training ML model")

class DeepLearningModel(MLModel):
    def process(self):
        super().process()
        print("Training Deep Neural Network")
dl_model = DeepLearningModel()
dl_model.process()
