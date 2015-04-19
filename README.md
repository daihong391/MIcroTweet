# Micro Twitter Project:

## 1. Instructions
This project aims to build a Django-powered micro edition of Twitter. As this is a minor project, I will adopt the embedded database-SQLite 3. This project is mainly divided into two parts: HTML and database, and the bellowing is the detailed design flow:

![Project Flow](https://github.com/daihong391/MIcroTweet/raw/master/images/projectFlow.png)

The first part, HTML, is mainly constitute of four sections: "main page", "user page", "user Tweets display", and "other people's tweets display". Meanwhile, "main page" needs two forms: one is for creating an account, another is for login, and a form for posting Tweets is embraced by "user page".

Considering the structure of this project, we need three databases: the first one for recording user's information(such as username, password, and email), the second one is for recording the Tweet's information(such as username, content), and the last one is for recording the following(such as username, following).

The bellowing figure shows the relationship between HTMLs and databases:

![Relationship between HTMLs and databases](https://github.com/daihong391/MIcroTweet/raw/master/images/relation.png)

## 2. Details
### 2.1 HTML
#### 2.1.1 Main Page

This page mainly focuses on the functions for logging in or creating an account, and the bellowing is the raw version of the main page:

![Main Page](https://github.com/daihong391/MIcroTweet/raw/master/images/mainpage.png)

If the username or password is incorrect, you will stay in the main page.

#### 2.1.2 User Page

This page is being realized, and these two figures show the frame of user page and a window for composing a new Tweet:

![User Page](https://github.com/daihong391/MIcroTweet/raw/master/images/userpage.png)

![User Page](https://github.com/daihong391/MIcroTweet/raw/master/images/newtweet.png)

User page includes following functions:
* checking the number of Tweets on the left top
* posting a new Tweet by clicking top right 'Tweet' image
* searching other people's Tweets by using the search box

#### 2.1.3 Tweets by User

This page displays all Tweets posted by user:

![User Page](https://github.com/daihong391/MIcroTweet/raw/master/images/tweetsByUser.png)

#### 2.1.4 Tweets by Following

This page is very similar to the page "Tweets by User", and shows as following:

![User Page](https://github.com/daihong391/MIcroTweet/raw/master/images/tweetsByFollowing.png)