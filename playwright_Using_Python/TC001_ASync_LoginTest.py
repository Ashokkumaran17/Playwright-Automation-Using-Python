import asyncio
from playwright.async_api import async_playwright
async def Login():
    pw = await async_playwright().start()
    browser = await pw.chromium.launch(headless=False, slow_mo=500)
    page = await browser.new_page()
    #Open the URL
    await page.goto("http://www.automationpractice.pl/index.php")
    # click Sign In
    await page.locator("a[class=\"login\"]").click()
    # Enter the user name Field
    await page.locator("#email").fill("selenium_java_2023@yopmail.com")
    # Enter the Password Field
    await page.locator("#passwd").fill("Java2023")
    # Click the Submit button
    await page.locator("#SubmitLogin").click()
    # Click SignOut Button
    await page.locator("a[class=\"logout\"]").click()
    # Close the Browser
    await browser.close()
    # Stop the Sync playwright
    await pw.stop()

# Execute the Login func
asyncio.run(Login())





