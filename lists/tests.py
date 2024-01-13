from django.test import TestCase

from lists.models import Item


# Create your tests here.
class HomePageTest(TestCase):

    def test_uses_home_template(self):

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        print(f'\n\nfirst_saved_item: {first_saved_item.text}\n\n')

        second_saved_item = saved_items[1]
        print(f'\n\nsecond_saved_item: {second_saved_item.text}\n\n')
        #só funciona com .text

        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')




