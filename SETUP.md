### Setting up prerequisites before running the scripts

1. Visit [this](https://replicate.com/create) url, create a replicate account if you don't have one already.
and then create a model with whatever hardware you want and `Finetuned image model` in type of model.

2. Go to account settings on replicate and create a `REPLICATE_API_TOKEN`.

3. Go to your terminal and paste `export REPLICATE_API_TOKEN=<paste-your-token-here>` .

4. Now that you have everything you need you can make a `.env` file based on the `.env.example` file. 

5. Get about 15-20 high resolution images of your face from different angles and put them in a folder.

6. Enter _into_ that folder and type the following into the commandline `zip -r foldername.zip . `.

7. Make sure to add this `.zip` into the working directory.

8. At this stage you should have three of the four fields in the `.env` ready. i.e. `replicate_model_name`, `input_images` and `gen_mod_ver`.

9. The `gen_mod_ver` parameter will be available once the model is trained.

