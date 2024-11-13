### Setting up prerequisites before running the scripts

1. Visit [this](https://replicate.com/create) url, create a replicate account if you don't have one already.
and then create a model with whatever hardware you want and `Finetuned image model` in type of model.

2. Go to account settings on replicate and create a `REPLICATE_API_TOKEN`.

3. Go to your terminal and paste `export REPLICATE_API_TOKEN=<paste-your-token-here>` .

<!-- 4. Go to [huggingface.co](https://huggingface.co/) and create a model and copy the name of the model. Prefrably use the same name as your replicate model.

5. Also go to the settings on [huggingface](https://huggingface.co/settings/profile) and create an access-token, copy it. and store it somewhere.  -->

4. Now that you have all the necessary info you can make a `.env` file based on the `.env.example` file. 

5. Get about 15-20 high resolution images of your face and put them in a folder.

6. Enter into that folder and type the following into the commandline `zip -r foldername.zip` .

7. Make sure to add this `.zip` into the working directory.

