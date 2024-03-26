import asyncio
from playwright.async_api import async_playwright
import time
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=2000)
        page = await browser.new_page()
        await page.goto("https://playwright.dev/")
        time.sleep(10)
        actual_title = "Fast and reliable end-to-end testing for modern web apps | Playwright"
        expected_title = await page.title()
        print(expected_title)
        assert actual_title == expected_title
        await browser.close()
asyncio.run(main())