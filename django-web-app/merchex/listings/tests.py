#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
# SPDX-License-Identifier: GPL-3.0-or-later
"""Django test client checks, using an isolated in-memory test database."""
from django.test import TestCase
from .models import Band


class ListingsTests(TestCase):
    def test_about_page(self):
        response = self.client.get("/about-us/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "À propos")

    def test_band_list(self):
        Band.objects.create(name="Test Band")
        response = self.client.get("/hello/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Band")

    def test_unknown_page(self):
        self.assertEqual(self.client.get("/missing/").status_code, 404)
