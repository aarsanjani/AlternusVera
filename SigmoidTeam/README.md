## Objective:
Fake news on the basis of several factors. Each factor will be trained against the separately related dataset. Later these trained models will be used to predict against master dataset and added as a column in order to predict fakeness.<br>

High level a polynomial equation to predict is <br>

**y = a1(number of words) + a2(Domain Rank) + a3(Political Affiliation) + a4(Toxicity Detection) + a5(Spam Detection) +a6(Stance Detection) + a7(Clickbait) + a8(News Category Determination) + a9(Sentiment)**

<br>
DataDource: <br>
https://www.kaggle.com/mrisdal/fake-news<br>

* uuidUnique identifier
* ord_in_thread
* authorauthor of story
* publisheddate published
* titletitle of the story
* texttext of story
* languagedata from webhose.io
* crawleddate the story was archived
* site_urlsite URL from BS detector
* countrydata from webhose.io
* domain_rankdata from webhose.io
* thread_title
* spam_scoredata from webhose.io
* main_img_urlimage from story
* replies_countnumber of replies
* participants_countnumber of participants
* likesnumber of Facebook likes
* commentsnumber of Facebook comments
* sharesnumber of Facebook shares
* typetype of website (label from BS detector)

<br>
https://www.kaggle.com/jruvika/fake-news-detection


## Team Responsibilities

*   Gyanesh Pandey - 012506936 :  Stance Detection, Spam Detection
*   Manoj Kumar - 012494989 : Toxicity Detection, News Category Determination, Domain Rank
*   Shalini Narang - 012507573 : Click Bait, Sentiment Analysis, Echo Chamber
*   Yamini Muralidharen - 012449632 : Political Affiliation, Domain Rank

Everyone participated in Data Preprocessing and fake news detection master file.

**Project links:**<br>
Master Notebook: [ https://colab.research.google.com/drive/1XUkF7leYm_8QIpUCfz6HM7-TWDKbegRf ] <br>
Models: [ https://github.com/manojknit/AlternusVera/tree/master/SigmoidTeam/NLP_FakeNews ]  <br>
Datasets: [ https://github.com/manojknit/AlternusVera/tree/master/SigmoidTeam/dataset ]  <br>
Data Enrichment code: [ https://github.com/manojknit/AlternusVera/tree/master/SigmoidTeam/DataEnrich ]  <br>

## Project Journey

‘Fake News’ is one of the most debated topics in the context of current political discourse across the world. In the 2016 presidential election in US, the impact of misleading ‘News’ like articles received a substantial attention, particularly after the election of President Trump. According to a Pew Research poll*, 64% of adults in US say that fake news has left them confused about basic facts. Given the ubiquity of internet and ease of disseminating unverified information on internet, it is imperative that we need to develop tools and methods to indicate the veracity of a piece of information.

We, the team Sigmoid felt that it is our social responsibility to make use of our knowledge and build a system using machine learning, that could help decide if the news is fake or not. 

#### We started with Fake News data set provided by Kaggle.com. During our initial analysis we realized that the data set had a very limited set of features. We also felt that the dataset can be further enriched by adding domain ranking and spam detection features to identify whether the news is fake or not. Data was only having fake news so we balance it by adding real news from from different data source. 

### Data Preprocessing: 
Data set was not even readable format so performed tons of data preprocession(cleansing, formatting, selection, transformation etc.)
1. Replaced null
2. Special character handling
3. Structuring news content
4. Transformed Real News data from file level to original fake news format.
5. Encoding

### Data Enrichment:
1. Downloaded real news data(https://webhose.io/datasets/) and formatted to align to merge in Kaggle fake news data. Also scrapped from google news.
  - Python code: https://github.com/manojknit/MachineLearningModels/blob/master/DataEnrich/Webhose_RealNews_DataPull.py
  - Output file: https://github.com/manojknit/MachineLearningModels/blob/master/dataset/fake_real_dataset.csv
2. Used Alexa API to get domain ranking data.
  - Python code: https://github.com/manojknit/MachineLearningModels/blob/master/Regression/fetch_domain_rank.py
  - Output file: https://github.com/manojknit/MachineLearningModels/blob/master/dataset/fake_real_dataset.csv
3. Added column by running spam detection madel. 
  - Python code: https://github.com/manojknit/MachineLearningModels/blob/master/DataEnrich/Spam_Score.py
  - Output Data set : https://github.com/manojknit/MachineLearningModels/blob/master/dataset/fake_real_dataset_spam.csv
 
### Latent Manifold:
 After data enrichment we found latent variables like domain rank, spam score. We fount Domain Rank as Latent Manifold.
 
Following diagram depicts the data enrichment process for fake news.

![Fake news data enrichment ](https://s3-us-west-2.amazonaws.com/themodestwhite.com/ml_fn.jpg)

Once the dataset was sufficiently enriched, we tried executing a couple of machine learning algorithms on our dataset. We encountered following issues:
1. Any sophisticated approach to identify fake news uses **"NLP"** techniques. We as a team didn't have much knowledge on NLP at the time so we put this on hold.
2. Also, the data didn't have many numerical columns that could be used for many classification algorithms. We were not familiar with **"Vectorization"** techniques which could use a piece of text transformed into a **"bag-of-words"**.

Note: Big datasets are not available in git. Please download from internet.
