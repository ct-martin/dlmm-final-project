# Generating Descriptive Image Captions

Code for processing the Cooper Hewitt dataset and attempting to fine-tune the Salesforce BLIP model.

Other part of project available here: <https://github.com/embedded-robotics/deep-learning-multimodal-systems-final-project>

## Dataset Preparation

In order they should be run:

1. `nocaps-lengths.ipynb` - research on NoCaps dataset
2. `download-data.sh` - downloads the metadata, list of media files, and total size of Cooper Hewitt JPEGs
3. `si-find.ipynb` - searches the metadata, filters to the desired subset of the data, and splits into train & test datasets
4. `missing_media_check.ipynb` - validates the list of media to download and outputs final list for downloader to use
5. `download-media.py` - downloads the filtered set of media files, downsizes the images, and saves the downsized images

## Fine-tuning

* `finetune-v0.ipynb` - initial attempts to train the model and struggling with memory issues
* `finetune-v1.ipynb` - training code for first model, using WER
* `finetune-v2.ipynb` - revised training code using BLEU and filtering stopwords
* `finetune-experiment.ipynb` - an experiment to see how fast the model degraded with training

## Evaluation

* `eval-model-v1.ipynb` - evaluation of `v1` model
* `eval-model-v2.ipynb` - evaluation of the `v2` model; creates `report.md`
* `eval-model-experiment.ipynb` - evaluation of the degredation experiment model; creates `report-test.md`
