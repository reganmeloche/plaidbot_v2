# Plaidbot

Plaidbot allows you to predict the author of a Slack message using a custom slack application backed by a classifier trained on your Slack message history. It can be set up as a fun custom application that can be triggered with a slash command.

<img src="img/sample.png" width="300" />

This repo contains components for training and hosting a machine learning model that can be easily hooked up to a custom Slack application using a slash command. It is a supervised learning approach that learns to predict authorship based on your message history. Once the model is trained, it gets stored in the HuggingFace model repository. A separate Flask web application then loads that trained model when the web application is deployed. A customized slackbot is set up to make a web request to this application, which will send the slack message. The web application will respond with a guess as to which user sent the message.

The process is illustrated in the following diagram.

<img src="img/diagram.jpg" width="500" />

This following instructions will guide you through the process of setting this application up using your own Slack channel.

## How to use it

Preliminary Notes:
- Some of the steps can take a while, including the Slack data export, loading the messages, training the classifier (especially without a GPU), and deployment. This depends largely on the number of messages you are training on.
- Less users will generally yield better performance, and the dataset is likely to be very imbalanced. For example, if you have a slack group of 8 people, and 2 or 3 do not send very many messages, the classifier will have a difficult time predicting those users. The instructions show you how you can customize the process to only use a handful of desired users.

### Setup

First, we will need to do some housekeeping and get set up on all of the required web services. We will do the training in a Google CoLab environment, where we are able to use an interactive approach and take advantage of GPUs to quickly train our models.

#### Account Setup

Create a folder in Google Drive to store and run everything for training. It is strongly recommended that you upgrade to a Premium CoLab account where you have access to GPUs for training. You only need this for the training. Once the model is trained, a GPU is not required for deployment.

Create an account on [HuggingFace](https://huggingface.co/). HuggingFace is a powerful data science platform that comes with powerful libraries and allows you to upload trained models. Once our model is trained, it will be uploaded to HuggingFace. Once it is there, we will deploy our web application, so that the model can be retrieved and used to make predictions.

Create an account on [Azure](https://portal.azure.com/) so that we can deploy the app using an App Service. You can use other providers as well, but I have not tested them.


### Export Slack History

We will be exporting the Slack message history for training our classifier. The message export is available on the free tier.

Follow the [steps provided](https://slack.com/help/articles/201658943-Export-your-workspace-data) by Slack for exporting your desired message history. 

Unzip the folder and you will get a set of folders for each channel in your slack group. Each channel folder should contain a collection of files of the format `YYYY-MM-DD.json`

Create a folder called "messages" in your Google Drive folder and move all of these folders and files into it. Make sure to include the `users.json` file as well.

Clone the plaidbot Github repo. Copy the 'src' folder and the 'train.ipynb' notebook into your Google Drive folder. Your Google Drive folder should now be setup as follows:
- messages/
  - general/
    - 2022-01-01.json
    -  ...other json message files...
  - random/
  - ...other channel folders...
  - users.json
- src/
  - ...all code files...
- train.ipynb


### Training the Classifier

We will now train a classifier on our exported data. The result will be a model, which gets stored in HuggingFace. All of this is done via the easy-to-use training notebook interface in the train.ipynb file. Open the train.ipynb file in Google CoLab and follow the steps in the notebook. If you're using the premium tier, ensure you switch to a GPU. You will need to set some other options and configuration before the training, but this is all explained in the notebook. Once you're finished, you should have a model saved in HuggingFace. 

Also ensure that you copy and save the user_int_name_dict generated during training. We'll need in the next step.

### Deployment

Open the code that you cloned in an IDE (I use VS Code). Test it locally to ensure that the model is being loaded from HuggingFace:
- Copy the dictionary from the previous step into the `src/options/model_options.py` file
- Set any of the other relevant options in this same file. Ensure you put the same saved model name and hugging face token that you used for training into the corresponding options
- Set a secret in the `src/options/web_options.py`. This adds some simple protection to your endpoints. It will need to be added as a query parameter when making a web request
- Create a virtual environment and install the libraries: 
- Run 'flask run' to run the server locally

On startup, the app will load the model from HuggingFace. You are now able to make predictions by calling the /predict endpoint. Make sure to add the appropriate secret as a query parameter. Note that it takes a while for the model to load into the web app after deployment. Give it a few minutes and then it should be ready to make predictions.

<img src="img/postman.png" width="500" />

We can now deploy our code to production. This will depend on your hosting provider. I used Azure to host it, and I downloaded the Azure App Service extension on VS Code for simple deployment. 

### Set up Slack Application

Finally we need to create the slack integration so that it can be called from your slack channel. 

Create a custom [slack app](https://api.slack.com/apps)

Add a slash command as follows: 

<img src="img/slash.png" width="500" />

You should now be able to use the /predict command from your Slack channel and have Plaidbot send back the predicted user.



## Development

Feel free to fork the repo and customize it as desired. Make sure not to check any sensitive credentials from the options files into Github.

Create a virtual environment, activate it (e.g. `source plaidbot-env/Scripts/activate`) and install the libraries (`pip install -r requirements`)

The tests are written with the unittest module and a unit test can be run as follows: `python -m unittest tests/file_to_test.py`

To run all unit tests: `python -m unittest discover -s 'tests/' -p '*_tests.py'`

Test coverage is done using the coverage library. To use it simply replace the `python` part of the test command with `coverage run`. For example: `coverage run --source=src -m unittest discover -s 'tests/' -p '*_tests.py'`. You can then use the `coverage report` command to view a coverage report or `coverage html` to generate a more detailed report that can be viewed in a browser. 


