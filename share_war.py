import selenium, time, argparse
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime

#Your Credentials File
from credentials import *
import pdb

def rt(d):
    times = np.random.rand(1000)+np.random.rand(1000)+d
    return np.random.choice(times, 1).tolist()[0]

def login():
    url = "https://poshmark.com/login"
    driver.get(url)

    time.sleep(rt(5))

    try:
        #Login
        print("[*] logging into Poshmark seller account...the share war will begin momentarily...")
        username = driver.find_element_by_name("login_form[username_email]")
        username.send_keys(poshmark_email)
        time.sleep(rt(5))

        password = driver.find_element_by_name("login_form[password]")
        password.send_keys(poshmark_password)
        time.sleep(rt(5))


        password.send_keys(Keys.RETURN)
        time.sleep(rt(5))

        #Check for Captcha
        try:
            captcha_fail = driver.find_element_by_xpath("//span[@class='base_error_message']")
            if len(str(captcha_fail)) > 100:
                print(("[*] Caught by Captchas: Proceed to Debugger in terminal..."))
                import pdb; pdb.set_trace()
                print(("[*] Please complete captchas, robots game before proceeding..."))
                login_pdb()
                return
            else:
                pass
        except:
            pass

        #Navigate to Seller Page
        time.sleep(rt(10))
        seller_page = "https://poshmark.com/closet/{}".format(closet_name)
        driver.get(seller_page)

    except:
        #Captcha Catch
        print("[*] ERROR in Share War: Thrwarted by Captchas: self share")
        login_pdb()
        pass


def login_pdb():

    try:
        import pdb; pdb.set_trace()

        #Login
        username = driver.find_element_by_name("login_form[username_email]")
        username.clear()
        username.send_keys(poshmark_email)
        time.sleep(rt(5))

        password = driver.find_element_by_name("login_form[password]")
        password.send_keys(poshmark_password)
        time.sleep(rt(5))
        password.send_keys(Keys.RETURN)

        #Navigate to Seller Page
        time.sleep(rt(5))
        seller_page = "https://poshmark.com/closet/{}".format(closet_name)
        driver.get(seller_page)

    except:
        print("[*] ERROR in Share War: Thrwarted by Captchas: self share")
        pass

def brand_page(brand):
    try:
        # Navigate to Brand Page
        time.sleep(rt(10))
        brand_page = "https://poshmark.com/brand/{}-Women-Jewelry?sort_by=added_desc".format(brand)
        driver.get(brand_page)

    except:
        # Captcha Catch
        print("[*] ERROR in Share War: Thrwarted by Captchas: brand page")
        pass

def scroll_page(n, delay=3):
    scroll = 0
    print("[*] scrolling through all items in closet...")
    for i in range(1, n+1):
        scroll +=1
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(rt(delay))


def get_closet_urls():
    items = driver.find_elements_by_xpath("//div[@class='item-details']")
    urls = [item.find_element_by_css_selector('a').get_attribute('href') for item in items]
    return urls


def get_closet_share_icons():
    # items = driver.find_elements_by_xpath("//div[@class='social-info d-fl ai-c jc-c']")
    # share_icons = [item.find_element_by_css_selector("a[class='share']") for item in items]
    products = driver.find_elements_by_xpath("//div[@class='col-x12 col-l6 col-s8']")
    share_icons = []
    for product in products:
        try:
            soldout = product.find_element_by_css_selector("i[class='icon inventory-tag sold-out-tag']")
            # print("sold out", soldout)
            continue
        except:
            try:
                soldout = product.find_element_by_css_selector("i[class='icon inventory-tag sold-tag']")
                # print ("sold", soldout)
                continue
            except:
                try:
                    soldout = product.find_element_by_css_selector("i[class='icon inventory-tag not-for-sale-tag']")
                    # print("not for sale", soldout)
                    continue
                except:
                    share_icons.append(product.find_element_by_css_selector("a[class='share']"))
                    # print("normal", product)
    return share_icons


def clicks_share_followers(share_icon, d=6, share_to= "followers"):

    #First share click
    driver.execute_script("arguments[0].click();", share_icon); time.sleep(rt(d))

    #Second share click
    # pm-party-share-link grey
    share_followers = driver.find_element_by_xpath("//a[@class='pm-{}-share-link grey']".format(share_to))
    driver.execute_script("arguments[0].click();", share_followers); time.sleep(rt(d))


# def share(d=4.5):
#     #shortcut to reshare in debugger mode
#     [clicks_share_followers(item, d) for item in share_icons]


def open_closet_item_url(url):
    print(url)
    driver.get(url)
    time.sleep(rt(5))




def deploy_share_war(n=3, order=True, share_to = "followers"):
    print("[*] DEPLOYING SHARE WAR")

    try:
        login()
        if self_share:
            scroll_page(n)
            share_icons = get_closet_share_icons()

            if order is True:
                share_icons.reverse()
            else:
                pass
            print("[{}] sharing PoshMark listings for {} items in closet...".format(str(datetime.now()),len(share_icons)))
            print("[{}] please wait...".format(str(datetime.now())))

            #Share Listings
            [clicks_share_followers(item, share_to=share_to) for item in share_icons]
            print("[{}] closet successfully shared...posh-on...".format(str(datetime.now())))
        else:
            print("skip self share process")

        #Share Brand Listings
        if brand_share:
            time.sleep(rt(5))
            brand_list = brands_to_share.split(' ')
            print("[{}] starting to share the following brands {}".format(str(datetime.now()),brand_list))

            for i in brand_list:
                time.sleep(rt(5))
                brand_page(i)
                scroll_page(scroll_the_brand)
                share_icons = get_closet_share_icons()
                print("[{}] sharing brand listings for {} for {} items".format(str(datetime.now()), i, len(share_icons)))
                print("[{}] please wait...".format(str(datetime.now())))
                # Share Listings
                [clicks_share_followers(item, share_to=share_to) for item in share_icons]

                print("[{}] {} successfully shared...posh-on...".format(str(datetime.now()),i))
            print("[*] all brands successfully shared...posh-on...")
        else:
            print("skip brand share process")

        #Share Category Listings
        if category_share:
            time.sleep(rt(5))
            category_page = "https://poshmark.com/category/Women"
            driver.get(category_page)
            scroll_page(scroll_the_category)
            share_icons = get_closet_share_icons()

            print("[{}] sharing PoshMark category listings for {} items in closet...".format(str(datetime.now()),
                                                                                    len(share_icons)))
            print("[{}] please wait...".format(str(datetime.now())))
            #Share Listings
            [clicks_share_followers(item, share_to=share_to) for item in share_icons]
            print("[{}] closet successfully shared...posh-on...".format(str(datetime.now())))
        else:
            print("skip self share process")
        pass

    except:
        print("[*] ERROR in Share War")
        pass


    print("[*] the share war will continue in {} minutes...current time: {}".format(int(random_loop_time/60), str(datetime.now())))


# if __name__=="__main__":
# parser = argparse.ArgumentParser()
# parser.add_argument("-t", "--time", default=3600, type=float, help="time in seconds")
# parser.add_argument("-n", "--number", default=7, type=int, help="number of closet scrolls")
# parser.add_argument("-o", "--order", default=True, type=bool, help="preserve closet order")
# args = parser.parse_args()


#Start Share War Loop
starttime=time.time()

# while True:
#     #Start Driver, Get URLS, Close
#     driver = webdriver.Chrome(executable_path=driver_path)
#     driver.implicitly_wait(0)
#
#     #Time Delay: While Loop
#     random_loop_time = rt(timing_to_share)
#
#     #Run Main App
#     # change it to "party" or "followers" if you want to share listings to a party or followers
#     deploy_share_war(scroll_my_closet, True, "followers")
#
#     time.sleep(rt(10))
#     driver.close()
#
#         #Time Delay: While Loop
#     time.sleep(random_loop_time - ((time.time() - starttime) % random_loop_time))
#


driver = webdriver.Chrome(executable_path=driver_path)
driver.implicitly_wait(0)

#Time Delay: While Loop
random_loop_time = rt(timing_to_share)

#Run Main App
# change it to "party" or "followers" if you want to share listings to a party or followers
deploy_share_war(scroll_my_closet, True, "party")

time.sleep(rt(10))
driver.close()

#Time Delay: While Loop
time.sleep(random_loop_time - ((time.time() - starttime) % random_loop_time))