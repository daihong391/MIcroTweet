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

