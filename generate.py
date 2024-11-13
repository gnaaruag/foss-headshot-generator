import replicate
import os 
from dotenv import load_dotenv

load_dotenv()


model_version = os.getenv("gen_mod_ver")
prompt = os.getenv("gen_prompt")
print(model_version)

output = replicate.run(
    model_version,
    input={"prompt": prompt}
)
print(output)