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
        # inputbox.submit()
        time.sleep(3)

        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_name('.//tr')
        table_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, 'id_list_table'))
        )

        rows = table_element.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        # Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro
        # item. Ela insere "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        time.sleep(1)

        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)

        # A página é atualizada novamente e agora mostra os dois itens em sua lista
        table_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, 'id_list_table'))
        )

        rows = table_element.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])

        # Edith se pergunta se o site lembrará de sua lista. Então ela nota
        # que o site gerou um URL único para ela -- há um pequeno texto
        # explicativo para isso.
        self.fail('Finish the test!')

        # Ela acessa esse URL - sua lista de tarefas continua lá.

        # Satisfeita, ela volta a dormir



if __name__ == '__main__':
    unittest.main(warnings='ignore')
