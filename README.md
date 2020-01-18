![](https://d2zlsagv0ouax1.cloudfront.net/assets/home_page/hp-v5-logo@2x-6003c7f00d83f4df697830d18bdcf167.png)

# Welcome to the Poshmark Sharing App

This script is designed for users with a [seller account on Poshmark marketplace](https://poshmark.com).

It is designed to automate sharing the listings for every item in your closet with all subscribers. Once the script is executed, it will share your listings every 60 minutes. You can edit the timing and other options if you desire.

# Let the Share War Begin

### Prerequisites

* Python 3.5+
* Firefox 46.0.1+
* [Selenium](http://selenium-python.readthedocs.io)==2.53.6+

### Setup

#### Git Clone

First clone the repository in terminal:
* `git clone git@github.com:ktji/poshmark_sharing-master.git

#### User Credentials

You will need to modify a `credentials.py` file.

```python
poshmark_email = "myemail@gmail.com"
poshmark_password = "mypassword"
brands_to_share = 'brand1 brand2 brand3'
driver_path = r'enteryourdriverpath'
```

Edit the text in quotes to your actual username and password. Enter the brands you want to share with a space between brands. 
Download and edit your driver path. I used a chromedriver. You can also use firefox or other browsers drivers. Save the file.




## Run Share War App in Terminal

In terminal run the following command: `python share_war.py`

*Note:* If you have several versions of python, you will need to amend the above line to run your python 3 alias, e.g. `python3 share_war.py`.

## Run the Jupyter App

This program can also be run in Jupyter with a Python 3 kernel. Simply launch `jupyter notebook` in terminal and click the notebook, `PoshMark_Seller_Sharing_App.ipynb`. Once in the notebook, simply follow the instructions to run the script.

## Options

There are a variety of optional arguments for the script, including timing, closet scroll size, and audiance.

### Timing

You can adjust the timing in `credentials.py` file. The default is 3600 seconds (60 minutes). Here are some examples:

.

```python
# Update the timing, scroll
timing_to_share = float(3600)
timing_to_share = float(7200) # two hours
```

### Closet Size

If you have many listings, you may need to increase the number of times the application scrolls to the end of page:

```python
scroll_my_closet = int(8) # scroll 8 times
```

If you want to skip one step of sharing, put False in `credentials.py` file. For example

```python
# DO NOT run self share
self_share = False
scroll_my_closet = int(8)
```

### Shared audiance

You can choose to share to your followers or to the party. Edit one field in 'share_way.py'

```python
#Run Main App
# change it to "party" or "followers" if you want to share listings to a party or followers
deploy_share_war(scroll_my_closet, True, "party") # change party to followers if you want to share to your followers only
```




