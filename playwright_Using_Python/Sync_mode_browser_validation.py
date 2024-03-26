from playwright.sync_api import sync_playwright

#Validating the title with Sync mode using playwright
with sync_playwright() as p:
    browser = p.firefox.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    actual_title ="Fast and reliable end-to-end testing for modern web apps | Playwright"
    expected_title = page.title()
    print(expected_title)
    assert actual_title == expected_title
    browser.close()



