import replicate
import os
from dotenv import load_dotenv

load_dotenv()

file_input_path = os.getenv("input_images")
replicate_model_name = os.getenv("replicate_model_name")
print(file_input_path)
print(replicate_model_name)
file_input = open("./" + file_input_path, "rb")


try:
	training = replicate.trainings.create(
		destination=replicate_model_name,
		version="ostris/flux-dev-lora-trainer:e440909d3512c31646ee2e0c7d6f6f4923224863a6a10c494606e79fb5844497",
		input={
			"steps": 2000,
			"lora_rank": 16,
			"optimizer": "adamw8bit",
			"batch_size": 1,
			"resolution": "512,768,1024",
			"autocaption": True,
			"input_images": file_input,
			"trigger_word": "TOK",
			"learning_rate": 0.0004,
			"wandb_project": "flux_train_replicate",
			"wandb_save_interval": 100,
			"caption_dropout_rate": 0.05,
			"cache_latents_to_disk": False,
			"wandb_sample_interval": 100
		},
	)
	print(training)
except Exception as e:
	print(f"An error occurred: {e}")
print("done")