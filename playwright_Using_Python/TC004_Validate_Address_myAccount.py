from playwright.sync_api import sync_playwright

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

def tc_login(page):
    # click Sign In
    page.locator("a[class=\"login\"]").click()
    # Enter the username Field
    page.locator("#email").fill("selenium_java_2023@yopmail.com")
    # Enter the Password Field
    page.locator("#passwd").fill("Java2023")
    # Click the Submit button
    page.locator("#SubmitLogin").click()

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

def tc_logout(page):
    # Click SignOut Button
    page.locator("a[class=\"logout\"]").click()
