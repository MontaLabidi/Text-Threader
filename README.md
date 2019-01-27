# Text Threader

<p align="center">
    <img src="https://user-images.githubusercontent.com/36813986/117892826-4f0ade80-b2b1-11eb-9e60-4bce6b96cb75.jpg">
</p>

**Text Threader** is a web application made with [Django 2](https://www.djangoproject.com/download/)
and [Angular 7](https://angular.io/) to detect the language and sentiment of a given text.
It mainly detects _Arabic_ or _Tunisian dialect_ and a _Positive_ or a _Negative_ sentiment and supports testing
multiple text documents.


### Features

* Detects the language of a text written in any character encoding (_Arabic_ / _Tunisian_/ _Other_)

* Analyse the Sentiment of a text written in any character encoding (_Negative_ / _Positive_/ _Other_)

* Supports streaming multiple files with texts to classify and analyse 

# Getting Started

## Pre-requisites

For building and running the application you need:

* Backend:
    - [Python 3.6](https://www.python.org/)
    - [Django 2.1](https://www.djangoproject.com/download/)

* Frontend:
    - [Node.js](https://nodejs.org/en/download/)
    - [npm](https://www.npmjs.com/get-npm) (comes with Node.js)


## Installation

### Classification Model Setup

This step is optional if you are just looking to use the application since it is already set up with the needed models,
but if you want to tweak on the classification models used then install [Jupyter notebook](https://jupyter.org/) and open
the following notebooks:
 
* **Language identification**

    These steps give an overview on the language identification pipeline of the `Lang-classifier.ipynb` Jupyter notebook:
    
    * Text Cleaning
    * Construct the training and test dataframes using our labaled data
    * Convert the training documents into numeric feature vectors using the _BOW-tfidf_ method with _character ngrams_
    * Create a language classifier using Naive Bayes method (tfidf version)
    * Evaluate performance of this classifier based on the test corpus: calculate classification accuracy, precision,
     recall, F1, and confusion matrix

* **Sentiment analysis**

    These steps give an overview on the sentiment analysis pipeline of the `Sentiment-analysis.ipynb` Jupyter notebook:
    
    * Text Cleaning
    * Normalization & tokenization
    * Remove stop words
    * Stemming
    * Extract the vocabulary set from the corpus and calculate IDF values of each word in this set
    * tune the BOW configuration parameters (min_df, max_df, etc.)
    * Building the Clarification model: tested Naive Bayes and Logistic Regression, chose the NB classifier because it gave the better accuracy and confusion matrix.

After making changes to the pipelines, its just a matter of running them to dump all the models that the Backend will
use to predict and analyse the texts.

### Backend 

For this step, we recommend setting up a virtual environment and activating it, this is optional:
 [Python 3 Virtual Environment Tutorial](https://docs.python.org/3/tutorial/venv.html)

First `cd` into the `Text-Threader-Backend` directory.

Install project dependencies:

    $ pip install -r requirements.txt

    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver


### Frontend

First `cd` into the `Text-Threader-Frontend` directory.

The frontend for **FMS** was generated with [Angular CLI](https://github.com/angular/angular-cli) version 7.1.4.

To get it up and running, you need to first install the dependencies using `npm`:

    $ npm install

then simply serve it using:

    $ npm start

Now you should be able to access **Text Threader** at `http://localhost:4200/`


# Usage

* At the Home page the user will two options:
    upload files to be classified and analysed simply by clicking the upload button:

    ![main_page](https://user-images.githubusercontent.com/36813986/117522379-e9fe7280-afaa-11eb-9eec-aaf8ec016934.png)

    Or navigate to the second tab where he can just enter the text manually to be classified and analysed:

    ![main_page_second_tab](https://user-images.githubusercontent.com/36813986/117522380-ea970900-afaa-11eb-94bb-de5d27a6ab4d.png)

### Classify Documents

*   To classify a list of texts, the user can simply write them into a `txt` file(s) and click the upload button
    so that the upload files pop up will appear for the user:

    ![upload_files](https://user-images.githubusercontent.com/36813986/117522381-ea970900-afaa-11eb-8cfa-be419431587e.png)

    after that the user can choose any number of text files from his local file system and click choose:

    ![uploaded_files](https://user-images.githubusercontent.com/36813986/117522382-eb2f9f80-afaa-11eb-9f8a-4eb98fa319a1.png)
    
    after choosing the appropriate files, the user can then click on the Analyse button to initialise the language and
     sentiments analysis process for every text in the documents., the user will have a visual to indicate for him the
     progress on every file:
    
    ![analyse_files](https://user-images.githubusercontent.com/36813986/117522384-ebc83600-afaa-11eb-99e7-ed0c6fba9ea0.png)

    Once the classification and analysis are finished on a document, an automatic download of a csv result file will initiate:
    
    ![analysed_files](https://user-images.githubusercontent.com/36813986/117522376-e8cd4580-afaa-11eb-94b0-6f1b92f47cc5.png)

    then the user can visualise the results for every file in the downloaded file with the __name = input_file_name + _Result__
    and it should have two columns that are the language and sentiment predictions of the corresponding text row:
        
        TUN,NEG
        ARA,POS
        ARA,NEG
        ...
        
    
    
### Classify simple text

* If the user wishes to just analyse a simple text, then he can navigate to the second tab and enters his text:

    ![analyse_text](https://user-images.githubusercontent.com/36813986/117522374-e834af00-afaa-11eb-8b2b-b13330f014f7.png)

    very shortly after the results of the language and sentiment predictions will appear on hos screen:

    ![analysed_text](https://user-images.githubusercontent.com/36813986/117522377-e965dc00-afaa-11eb-83c9-37a1c9e7d54d.png)

