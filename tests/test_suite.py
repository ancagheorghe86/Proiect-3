import unittest
import HtmlTestRunner


from tests.test_keys import TestKeys
from tests.test_alerts import TestAlerts

class TestSuite(unittest.TestCase):
    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()

        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys)
        ])

        runner = HtmlTestRunner.HtmlTestRunner(
            combine_reports=True,
            report_title="testul nostru",
            report_name="ASJDJ"
        )
        runner.run(teste_de_rulat)