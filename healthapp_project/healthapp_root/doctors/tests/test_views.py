from django.test import TestCase
from django.urls import reverse
import datetime
from django.utils import timezone

from doctors.views import DoctorSignUpView


class DoctorSignUpViewTest(TestCase):
    @classmethod
    def get_context_data_Test(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)

        self.assertIs(future_question.was_published_recently(), False)

    def form_valid_Test(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)

        self.assertIs(future_question.was_published_recently(), False)



##
## class AuthorListViewTest(TestCase):
##    @classmethod
##    def setUpTestData(cls):
##        # Create 13 authors for pagination tests
##        number_of_authors = 13
##
##        for author_id in range(number_of_authors):
##            Author.objects.create(
##                                  first_name=f'Christian {author_id}',
##                                  last_name=f'Surname {author_id}',
##                                  )
##
## def test_view_url_exists_at_desired_location(self):
##    response = self.client.get('/catalog/authors/')
##    self.assertEqual(response.status_code, 200)
##
##    def test_view_url_accessible_by_name(self):
##        response = self.client.get(reverse('authors'))
##        self.assertEqual(response.status_code, 200)
##
##    def test_view_uses_correct_template(self):
##        response = self.client.get(reverse('authors'))
##        self.assertEqual(response.status_code, 200)
##        self.assertTemplateUsed(response, 'catalog/author_list.html')
##
##    def test_pagination_is_ten(self):
##        response = self.client.get(reverse('authors'))
##        self.assertEqual(response.status_code, 200)
##        self.assertTrue('is_paginated' in response.context)
##        self.assertTrue(response.context['is_paginated'] == True)
##        self.assertTrue(len(response.context['author_list']) == 10)
##
##    def test_lists_all_authors(self):
##        # Get second page and confirm it has (exactly) remaining 3 items
##        response = self.client.get(reverse('authors')+'?page=2')
##        self.assertEqual(response.status_code, 200)
##        self.assertTrue('is_paginated' in response.context)
##        self.assertTrue(response.context['is_paginated'] == True)
##        self.assertTrue(len(response.context['author_list']) == 3)
##
##
##
## from django.contrib.auth.mixins import LoginRequiredMixin
##
## class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
##    """Generic class-based view listing books on loan to current user."""
##    model = BookInstance
##    template_name ='catalog/bookinstance_list_borrowed_user.html'
##    paginate_by = 10
##
##    def get_queryset(self):
##        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
