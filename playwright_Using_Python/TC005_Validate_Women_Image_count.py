from playwright.sync_api import sync_playwright

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

def tc_login(page):
    # click Sign In
    page.locator("a[class=\"login\"]").click()
    # Enter the username Field
    page.locator("#email").fill("selenium_java_2023@yopmail.com")
    # Enter the Password Field
    page.locator("#passwd").fill("Java2023")
    # Click the Submit button
    page.locator("#SubmitLogin").click()

def tc006_women_tab(page):
    # click the women tab
    page.locator("#block_top_menu").get_by_role("link", name="Women").click()
    # display the No of image counts
    women_tab_img = page.locator("//ul[@class=\"product_list grid row\"]/li")
    print(women_tab_img.count())
    expected_img_count = 7
    assert women_tab_img.count() == expected_img_count
def tc_logout(page):
    # Click SignOut Button
    page.locator("a[class=\"logout\"]").click()
