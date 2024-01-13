from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, 'id_list_table'))
        )

        rows = table_element.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith ouviu falar de uma nova aplicação online interessante para
        # lista de tarefas. Ela decide verificar sua homepage
        self.browser.get('http://localhost:8000')

        # Ela percebe que o título da página e o cabeçalho mencionam listas de
        # tarefas (to-do)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        time.sleep(3)

        # Ela é convidada a inserir um item de tarefa imediatamente
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Ela digita "Buy peacock feathers" em uma caixa de texto
        inputbox.send_keys('Buy peacock feathers')

        time.sleep(1)

        # Quando ela tecla enter, a página é atualizada, e agora a página lista
        # "1: Buy peacock feathers" como item em uma lista de tarefas
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro
        # item. Ela insere "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        time.sleep(1)

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Edith se pergunta se o site lembrará de sua lista. Então ela nota
        # que o site gerou um URL único para ela -- há um pequeno texto
        # explicativo para isso.
        self.fail('Finish the test!')

        # Ela acessa esse URL - sua lista de tarefas continua lá.

        # Satisfeita, ela volta a dormir



if __name__ == '__main__':
    unittest.main(warnings='ignore')
