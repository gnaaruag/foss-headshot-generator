### foss-headshot-generator

This repo lets you create a ai headshot and other prompt to image generations based on a custom trained lora

This repo helps you create a lora on your input data and then helps you generate images on it

This is intended as a self hosted free and open source "professional headshot generator" for your linkedin profile photos or any use case for personalised image generation you may have.

#### Steps to follow to run successfully

1. Install dependencies `pip install -r requirements.txt`
2. Go follow all the instructions given in `SETUP.md`
3. Run the training file `train.py`
4. Go to [https://replicate.com/trainings](https://replicate.com/trainings) and check the status of your training
5. After training is complete click `run trained model` page on replicate and copy the model_name/version
6. Add the model name and version in the `.env` and then run the `generate.py` script


Make sure that the input images you are adding are very high quality and show your face in all the good angles. This is the most important step in generating a good lora of yourself