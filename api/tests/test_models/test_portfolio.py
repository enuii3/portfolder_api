from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from api.tests.factories.portfolio import PortfolioFactory

PORTFOLIO_URL = '/api/portfolios/'


class PortfolioModelsTestCase(TestCase):
    def setUp(self):
        self.portfolio = PortfolioFactory()
        self.client = APIClient()

    def test_should_get_portfolio(self):
        PortfolioFactory()
        res = self.client.get(PORTFOLIO_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)

