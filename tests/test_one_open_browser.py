from base.basetest import BaseTest
import pytest
from base.basetest import vtest


@vtest
class Test_first_testing_case(BaseTest):


    def test_001_first_step(self):
        self.site
