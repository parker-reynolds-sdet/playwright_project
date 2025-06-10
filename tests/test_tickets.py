from playwright.sync_api import sync_playwright

concert_ticket_app_html_path = "file:///C:/Users/george.reynolds/Downloads/concertapp.html"
artist_tiles_xpath = "xpath=//div[@class='screen active']/div" # Will resolve to 3 selectors, need to index
full_name_input_box = "css=[id='name']"
email_input_box = "css=[id='email']"
number_tickets_input_box = "css=[id='tickets']"
card_type_input_dropdown = "css=[id='cardType']"
card_number_input_box = "css=[id='cardNumber']"
expiration_date_input_box = "css=[id='expiry']"
cvv_input_box = "css=[id='cvv']"
billing_address_input_box = "css=[id='billing']"
artist_confirm = "css=[id='concertNameConfirm']"
form_error_text = "css=[id='formError']"

def test_ticket_titlescreen():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(concert_ticket_app_html_path)
        tile1_text = page.locator(artist_tiles_xpath).first.text_content()
        assert "The Weeknd" in tile1_text

def test_ticket_purchase():
    with sync_playwright() as p:

        # Launch browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Initialize selector
        artist_to_select = "The Weeknd"
        artist_tile_selector = f"xpath=//div[text()='{artist_to_select}']"

        # Go to html location with browser
        page.goto(concert_ticket_app_html_path)

        # Select the artist
        page.click(artist_tile_selector)

        # Fill in the billing form
        page.fill(full_name_input_box, "Parker Reynolds")
        page.fill(email_input_box, "parker.reynolds@aveva.com")
        page.fill(number_tickets_input_box, "2")
        page.select_option(card_type_input_dropdown, "Visa")
        page.fill(card_number_input_box, "1234123412341234")
        page.fill(expiration_date_input_box, "03/30")
        page.fill(cvv_input_box, "101")
        page.fill(billing_address_input_box, "123 Grandma Street")

        # Submit the form
        page.click("css=button")

        # Verify landing screen
        confirmed_artist = page.locator(artist_confirm).text_content()
        assert artist_to_select in confirmed_artist
        
def test_validation():
    with sync_playwright() as p:

        # Launch browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Initialize selector
        artist_to_select = "The Weeknd"
        artist_tile_selector = f"xpath=//div[text()='{artist_to_select}']"

        # Go to html location with browser
        page.goto(concert_ticket_app_html_path)

        # Select the artist
        page.click(artist_tile_selector)

        # Fill in the billing form with a bad credit card number
        page.fill(full_name_input_box, "Parker Reynolds")
        page.fill(email_input_box, "parker.reynolds@aveva.com")
        page.fill(number_tickets_input_box, "2")
        page.select_option(card_type_input_dropdown, "Visa")
        page.fill(card_number_input_box, "123412341234123") #cc number too short
        page.fill(expiration_date_input_box, "03/30")
        page.fill(cvv_input_box, "101")
        page.fill(billing_address_input_box, "123 Grandma Street")

        # Submit the form
        page.click("css=button")

        # Verify error message
        form_error_message = page.locator(form_error_text).text_content()
        assert "Card number must be 16 digits." in form_error_message

def test_new_validation():

    # Launch browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Initialize selector
        artist_to_select = "The Weeknd"
        artist_tile_selector = f"xpath=//div[text()='{artist_to_select}']"

        # Go to html location with browser
        page.goto(concert_ticket_app_html_path)

        # Select the artist
        page.click(artist_tile_selector)

        # Fill in the billing form
        page.fill(full_name_input_box, "Parker Reynolds")
        page.fill(email_input_box, "parker.reynolds@aveva.com")
        page.fill(number_tickets_input_box, "2")
        page.select_option(card_type_input_dropdown, "Visa")
        page.fill(card_number_input_box, "1234123412341234")
        page.fill(expiration_date_input_box, "03/30")
        page.fill(cvv_input_box, "101")
        page.fill(billing_address_input_box, "123 Grandma Street")

        # Submit the form
        page.click("css=button")

        ### CHALLENGE: Make a change to the logic that fills in the form and verify a new error string ###