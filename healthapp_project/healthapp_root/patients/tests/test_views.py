from django.test import TestCase
from django.urls import reverse

from patients.views import *


class PatientSignUpViewTest(TestCase):

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
#        response.get_context_data()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('Patient')
        self.assertEqual(response.status_code, 404)


#class AuthorListViewTest(TestCase):
#    @classmethod
#    def setUpTestData(cls):
#        # Create 13 authors for pagination tests
#        number_of_authors = 13
#
#        for author_id in range(number_of_authors):
#            Author.objects.create(
#                                  first_name=f'Christian {author_id}',
#                                  last_name=f'Surname {author_id}',
#                                  )
#
#def test_view_url_exists_at_desired_location(self):
#    response = self.client.get('/catalog/authors/')
#    self.assertEqual(response.status_code, 200)
#
#    def test_view_url_accessible_by_name(self):
#        response = self.client.get(reverse('authors'))
#        self.assertEqual(response.status_code, 200)
#
#    def test_view_uses_correct_template(self):
#        response = self.client.get(reverse('authors'))
#        self.assertEqual(response.status_code, 200)
#        self.assertTemplateUsed(response, 'catalog/author_list.html')
#
#    def test_pagination_is_ten(self):
#        response = self.client.get(reverse('authors'))
#        self.assertEqual(response.status_code, 200)
#        self.assertTrue('is_paginated' in response.context)
#        self.assertTrue(response.context['is_paginated'] == True)
#        self.assertTrue(len(response.context['author_list']) == 10)
#
#    def test_lists_all_authors(self):
#        # Get second page and confirm it has (exactly) remaining 3 items
#        response = self.client.get(reverse('authors')+'?page=2')
#        self.assertEqual(response.status_code, 200)
#        self.assertTrue('is_paginated' in response.context)
#        self.assertTrue(response.context['is_paginated'] == True)
#        self.assertTrue(len(response.context['author_list']) == 3)
