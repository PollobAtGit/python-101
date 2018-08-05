import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class HomePageFunctionalTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        self.browser.get("http://127.0.0.1:8000/")
        self.assertIn("To-Do", self.browser.title)

    def test_can_start_a_list_and_get_it_later(self):
        self.browser.get("http://127.0.0.1:8000/")

        header = self.browser.find_element_by_tag_name('h1')

        self.assertTrue(header.text == "To-Do")

        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute(
            'placeholder'), 'Enter a todo item')

        input_box.send_keys('buy pea-cock feathers')

        input_box.send_keys(Keys.ENTER)

        import time
        # This time delay is required
        time.sleep(3)

        table = self.browser.find_element_by_id('id_list_table')

        rows = table.find_elements_by_tag_name('tr')

        self.assertTrue("1: buy pea-cock feathers---",
                        [row.text for row in rows])


if __name__ == "__main__":
    unittest.main()
