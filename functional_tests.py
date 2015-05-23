from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Patrick has heard about a sweet new to-do app. He goes
        # to check it out
        self.browser.get('http://localhost:8000')

        # He noticies the title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He types "Buy peacock feathers" into a text box (Patrick's hobby)
        inputbox.send_keys('Buy peacock feathers')
        # When he hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )
        # There is still a text box inviting him to add another item. He
        # enters "Use peacoc feathers to make a fly"
        self.fail('Finish the test!')
        
        # The page updates again, and now shows both items on his list

        # He wonders if the site will remember his list. He notices 
        # that the site has generated a unique URL for him -- there is
        # some explanatory text to that effect.

        # He visits that URL - his to-do list is still there.

        # He goes back to sleep.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
