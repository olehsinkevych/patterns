from unittest import TestCase

from employees import Developer


class TestDeveloper(TestCase):

    def setUp(self) -> None:
        pass

    def test_developer_attributes(self):
        dev = Developer()
        self.a