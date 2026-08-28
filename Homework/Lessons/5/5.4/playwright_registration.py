from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    firefox = playwright.firefox.launch(headless=False)

    page = firefox.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    email_input.fill("user.name@gmail.com")

    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    username_input.fill("username")

    
    page.wait_for_timeout(5000)