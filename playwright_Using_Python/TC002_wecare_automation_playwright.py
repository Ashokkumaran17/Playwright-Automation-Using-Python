from playwright.sync_api import sync_playwright
import time
"""
def test_wecare_portal():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    #Open the URL
    page.goto("https://wecare.inspirisys.com/")
    # call the Func
    tc_login(page)
    tc_logout(page)
    # Close the Browser
    browser.close()
    # Stop the Sync playwright
    pw.stop()
"""
def test_apply_OnDuty_wecare_portal():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    #Open the URL
    page.goto("https://wecare.inspirisys.com/")
    # call the Func
    tc_login(page)
    tc_menu_icon(page)
    tc_leave_icon(page)
    tc_OnDuty_Application(page)
    tc_datepicker_table_row_5(page)
    tc_proceed_btn(page)
    tc_reason(page)
    tc_contact_number(page)
    tc_apply_btn(page)
    tc_logout(page)
    # Close the Browser
    browser.close()
    # Stop the Sync playwright
    pw.stop()
def tc_login(page):
    # Enter the user name
    page.get_by_placeholder("user name").fill("<UserName>")
    # Enter the password
    page.get_by_placeholder("password").fill("<Password>")
    # click Sign In Button
    page.get_by_text("Sign in").click()

def tc_menu_icon(page):
    # click the menu
    # page.get_by_text("Menu").click()
    page.get_by_title("Click here for Menu").click()

def tc_leave_icon(page):
    # click the leave
    page.get_by_text("MY LEAVE").click()
    #page.get_by_role("link", name="Leave").click()

def tc_OnDuty_Application(page):
    # click On Duty Application
    page.get_by_text("OnDuty Application").click()

def tc_datepicker_table_row_5(page):
    page.locator("#OnDutyHD_laLeaveFrom").click()
    # select the date i.e 25 Marc 2024
    #page.locator('tr:has-text("25")').click()
    page.get_by_role("row", name="25 26 27 28 29 30").get_by_text("26").click()


def tc_proceed_btn(page):
    # click the proceed button
    page.locator("#btnProceed").click()

def tc_reason(page):
    page.locator("#OnDutyHD_laReasonDrop").click()
    # select the On Duty option from the drop down menu
    page.select_option("#OnDutyHD_laReasonDrop", label='On Duty')

def tc_contact_number(page):
    # Enter the contact Number
    page.get_by_label("Contact Number (On Leave)").fill("<PhoneNumber>")

def tc_apply_btn(page):
    time.sleep(2)
    page.locator("#btnSubmit").press("Enter")
    # click the apply button
    #page.locator("#btnSubmit").click()
    time.sleep(2)
    #page.click('input#btnSubmit')
    #page.click('input[value="Apply"]')
    #page.locator("input[value=\"Apply\"]").click()
    # click the Ok btn on popup
    #page.click("OK")
    page.locator("button", has_text="OK").click()
    time.sleep(2)




def tc_logout(page):
    page.locator("div[class=\"GoogleButton\"]").click()
    page.get_by_text("Sign out").click()

