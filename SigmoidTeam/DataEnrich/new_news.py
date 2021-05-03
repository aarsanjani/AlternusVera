import newspaper
import csv
import uuid

myfile = open('fake_real_dataset_spam.csv','a+', encoding='utf-8')
wrtr = csv.writer(myfile, delimiter='\t', quotechar='"')
wrtr.writerow(['url','author','publishDate','title','suteURL','country','title','fake','text','imageURL'])

siteurl1='https://www.buzzfeed.com/'  ##bs 99999
buzzfeed_paper = newspaper.build(siteurl1)

for article in buzzfeed_paper.articles:
        uid=uuid.uuid4().hex
        url = article.url
        article.download()
        article.parse()
        article.nlp()
        title=article.title
        keyword=article.keywords
        author=article.authors  
        publishDate=article.publish_date
        csvRow=[uid,author, publishDate,title, siteurl1, 'US', title, 0,article.text, article.top_image]
        #print(url)
        print(csvRow)
        wrtr.writerow(csvRow)
        myfile.flush()
        
        
siteurl2 = 'http://100PercentFedUp.com/' ##bias, 25689
buzzfeed_paper2 = newspaper.build(siteurl2)

for article in buzzfeed_paper2.articles:
        uid=uuid.uuid4().hex
        url = article.url
        article.download()
        article.parse()
        article.nlp()
        title=article.title
        keyword=article.keywords
        author=article.authors  
        publishDate=article.publish_date
        csvRow=[uid,author, publishDate,title, siteurl2, 'US', title, 0,article.text, article.top_image]
        #print(url)
        print(csvRow)
        wrtr.writerow(csvRow)
        myfile.flush()

siteurl3="https://www.clickhole.com/" ##satire, 16425
buzzfeed_paper3 = newspaper.build(siteurl3)

for article in buzzfeed_paper3.articles:
        uid=uuid.uuid4().hex
        url = article.url
        article.download()
        article.parse()
        article.nlp()
        title=article.title
        keyword=article.keywords
        author=article.authors  
        publishDate=article.publish_date
        csvRow=[uid,author, publishDate,title, siteurl3, 'US', title, 0,article.text, article.top_image]
        #print(url)
        print(csvRow)
        wrtr.writerow(csvRow)
        myfile.flush()  
        
siteurl4="http://bizstandardnews.com/" ##satire, 16425
buzzfeed_paper4 = newspaper.build(siteurl4)

for article in buzzfeed_paper4.articles:
        uid=uuid.uuid4().hex
        url = article.url
        article.download()
        article.parse()
        article.nlp()
        title=article.title
        keyword=article.keywords
        author=article.authors  
        publishDate=article.publish_date
        csvRow=[uid,author, publishDate,title, siteurl4, 'US', title, 0,article.text, article.top_image]
        #print(url)
        print(csvRow)
        wrtr.writerow(csvRow)
        myfile.flush() 
        
        
siteurl5="https://21stcenturywire.com/" ##satire, 16425
buzzfeed_paper5 = newspaper.build(siteurl5)

for article in buzzfeed_paper5.articles:
        uid=uuid.uuid4().hex
        url = article.url
        article.download()
        article.parse()
        article.nlp()
        title=article.title
        keyword=article.keywords
        author=article.authors  
        publishDate=article.publish_date
        csvRow=[uid,author, publishDate,title, siteurl5, 'US', title, 0,article.text, article.top_image]
        #print(url)
        print(csvRow)
        wrtr.writerow(csvRow)
        myfile.flush() 
        
        
siteurl6="http://politicalblindspot.com/" ##satire, 16425
buzzfeed_paper6 = newspaper.build(siteurl6)

for article in buzzfeed_paper6.articles:
        uid=uuid.uuid4().hex
        url = article.url
        article.download()
        article.parse()
        article.nlp()
        title=article.title
        keyword=article.keywords
        author=article.authors  
        publishDate=article.publish_date
        csvRow=[uid,author, publishDate,title, siteurl6, 'US', title, 0,article.text, article.top_image]
        #print(url)
        print(csvRow)
        wrtr.writerow(csvRow)
        myfile.flush() 

siteurl7 = 'https://www.cnn.com/' ##bias, 25689
buzzfeed_paper7 = newspaper.build(siteurl7)

for article in buzzfeed_paper7.articles:
        uid=uuid.uuid4().hex
        url = article.url
        article.download()
        article.parse()
        article.nlp()
        title=article.title
        keyword=article.keywords
        author=article.authors  
        publishDate=article.publish_date
        csvRow=[uid,author, publishDate,title, siteurl7, 'US', title, 1,article.text, article.top_image]
        #print(url)
        print(csvRow)
        wrtr.writerow(csvRow)
        myfile.flush()

siteurl8="http://www.foxnews.com/" ##satire, 16425
buzzfeed_paper8 = newspaper.build(siteurl8)

for article in buzzfeed_paper8.articles:
        uid=uuid.uuid4().hex
        url = article.url
        article.download()
        article.parse()
        article.nlp()
        title=article.title
        keyword=article.keywords
        author=article.authors  
        publishDate=article.publish_date
        csvRow=[uid,author, publishDate,title, siteurl8, 'US', title, 1,article.text, article.top_image]
        #print(url)
        print(csvRow)
        wrtr.writerow(csvRow)
        myfile.flush()      
		
myfile.close()
