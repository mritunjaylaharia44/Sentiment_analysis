# Sentiment Analysis Django App
A simple django app for sentiment analysis on reviews. Reviews maybe for movie, product etc.

The app outputs the sentiment and the confidence of the model for choosing that particular class. 
![preview](https://github.com/zed1025/Django-Sentiment-Analysis-App/blob/master/preview.gif)

## Requirements
- python7.7.7
- Scikit Learn@0.22.2
- nltk@3.5b1 with nltk corpus
- django 3.0.x


## Installation and setup
- Run the [Sentiment_Analysis_Notebook.ipynb](https://github.com/zed1025/Django-Sentiment-Analysis-App/blob/master/sentiment/sentiment_model/Sentiment_Analysis_Notebook.ipynb) file. It will populate the picked_files directory with the pickled files needed. This will reduce the time it taked to make predictions. The generated picked files will be huge ~800MB
- Run the server using `python manage.py runserver`
- App hosted on `locahost:8000`
