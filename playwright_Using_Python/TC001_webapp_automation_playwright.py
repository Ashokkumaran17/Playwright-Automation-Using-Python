from playwright.sync_api import sync_playwright

def test_login():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    #Open the URL
    page.goto("http://www.automationpractice.pl/index.php")
    # call the Func
    tc_login(page)
    tc_logout(page)
    # Close the Browser
    browser.close()
    # Stop the Sync playwright
    pw.stop()

def test_validate_address_my_account():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    # Open the URL
    page.goto("http://www.automationpractice.pl/index.php")
    # call the Func
    tc_login(page)
    tc005_add_my_first_address(page)
    tc_logout(page)
    # Close the Browser
    browser.close()
    # Stop the Sync playwright
    pw.stop()

def test_validate_my_account_menu():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    # Open the URL
    page.goto("http://www.automationpractice.pl/index.php")
    # call the Func
    tc_login(page)
    tc002_back_your_home(page)
    tc_logout(page)
    # Close the Browser
    browser.close()
    # Stop the Sync playwright
    pw.stop()

def test_validate_empty_cart():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    # Open the URL
    page.goto("http://www.automationpractice.pl/index.php")
    # call the Func
    tc_login(page)
    tc004_check_cart_status(page)
    tc_logout(page)
    # Close the Browser
    browser.close()
    # Stop the Sync playwright
    pw.stop()

def test_validate_women_tab():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    #Open the URL
    page.goto("http://www.automationpractice.pl/index.php")
    # call the Func
    tc_login(page)
    tc006_women_tab(page)
    tc_logout(page)
    # Close the Browser
    browser.close()
    # Stop the Sync playwright
    pw.stop()

def test_validate_dresses_tab():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    #Open the URL
    page.goto("http://www.automationpractice.pl/index.php")
    # call the Func
    tc_login(page)
    tc007_dresses_tab(page)
    tc_logout(page)
    # Close the Browser
    browser.close()
    # Stop the Sync playwright
    pw.stop()

def test_validate_t_shirts_tab():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    #Open the URL
    page.goto("http://www.automationpractice.pl/index.php")
    # call the Func
    tc_login(page)
    tc008_t_shirts_tab(page)
    tc_logout(page)
    # Close the Browser
    browser.close()
    # Stop the Sync playwright
    pw.stop()

def tc_login(page):
    # click Sign In
    page.locator("a[class=\"login\"]").click()
    # Enter the username Field
    page.locator("#email").fill("selenium_java_2023@yopmail.com")
    # Enter the Password Field
    page.locator("#passwd").fill("Java2023")
    # Click the Submit button
    page.locator("#SubmitLogin").click()

def tc002_back_your_home(page):
    page.get_by_text(" Home").click()

def tc003_back_your_address(page):
    # Click Back to your address
    page.get_by_text(" Back to your addresses").click()

def tc004_check_cart_status(page):
    page.get_by_title("View my shopping cart").click()
    text_val = page.locator("p[class=\"alert alert-warning\"]")
    expected_val = "Your shopping cart is empty."
    assert text_val.text_content() == expected_val


def tc005_add_my_first_address(page):
    page.get_by_text("Add my first address").click()
    page.get_by_label("Company").fill("Accel-ISL")
    page.get_by_label("Address *").fill("Park view street")
    page.get_by_label("Address (Line 2)").fill("St Marks Road")
    page.get_by_label("City ").fill("Palo Alto")
    # select the state from drop down menu
    page.select_option("#id_state", label='California')
    page.get_by_label("Zip/Postal Code ").fill("96162")
    page.get_by_label("Home phone ").fill("+1714-456789")
    page.get_by_label("Mobile phone ").fill("+1714-275567")
    page.get_by_label("Additional information").fill("Welcome")
    page.get_by_label("Please assign an address title for future reference. ").click()
    # Click Back to your address
    page.get_by_text(" Back to your addresses").click()
    # Click back to Home
    page.get_by_text(" Home").click()

def tc006_women_tab(page):
    # click the women tab
    page.locator("#block_top_menu").get_by_role("link", name="Women").click()
    # display the No of image counts
    women_tab_img = page.locator("//ul[@class=\"product_list grid row\"]/li")
    print(women_tab_img.count())
    expected_img_count = 7
    assert women_tab_img.count() == expected_img_count


def tc007_dresses_tab(page):
    # click the dresses tab
    page.locator("#block_top_menu").get_by_role("link", name="Dresses").click()
    # display the No of image counts
    dresses_tab_img = page.locator("//ul[@class=\"product_list grid row\"]/li")
    print(dresses_tab_img.count())
    expected_img_count = 5
    assert dresses_tab_img.count() == expected_img_count

def tc008_t_shirts_tab(page):
    # click the t-shirts tab
    page.locator("#block_top_menu").get_by_role("link", name="T-shirts").click()
    # display the No of image counts
    t_shirts_tab_img = page.locator("//ul[@class=\"product_list grid row\"]/li")
    print(t_shirts_tab_img.count())
    expected_img_count = 1
    assert t_shirts_tab_img.count() == expected_img_count


def tc009_home_icon(page):
    page.locator("i[class=\"icon-home\"]").click()

def tc_logout(page):
    # Click SignOut Button
    page.locator("a[class=\"logout\"]").click()





