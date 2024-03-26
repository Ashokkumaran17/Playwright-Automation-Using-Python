from playwright.sync_api import sync_playwright
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

def tc_login(page):
    # click Sign In
    page.locator("a[class=\"login\"]").click()
    # Enter the username Field
    page.locator("#email").fill("selenium_java_2023@yopmail.com")
    # Enter the Password Field
    page.locator("#passwd").fill("Java2023")
    # Click the Submit button
    page.locator("#SubmitLogin").click()

def tc004_check_cart_status(page):
    page.get_by_title("View my shopping cart").click()
    text_val = page.locator("p[class=\"alert alert-warning\"]")
    expected_val = "Your shopping cart is empty."
    assert text_val.text_content() == expected_val
def tc_logout(page):
    # Click SignOut Button
    page.locator("a[class=\"logout\"]").click()
