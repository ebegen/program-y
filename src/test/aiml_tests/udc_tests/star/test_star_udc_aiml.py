import unittest
import os
from test.aiml_tests.client import TestClient
from programy.config.brain import BrainFileConfiguration

class BasicTestClient(TestClient):

    def __init__(self):
        TestClient.__init__(self)

    def load_configuration(self, arguments):
        super(BasicTestClient, self).load_configuration(arguments)
        self.configuration.brain_configuration._aiml_files = BrainFileConfiguration(file=os.path.dirname(__file__)+os.sep+'star_udc.aiml')

class UDCAIMLTests(unittest.TestCase):

    def setUp(self):
        UDCAIMLTests.test_client = BasicTestClient()

    def test_udc_multi_word_question(self):
        response = UDCAIMLTests.test_client.bot.ask_question("test", "Ask Question")
        self.assertIsNotNone(response)
        self.assertEqual(response, "UDC Star Response")

    def test_udc_single_word_question(self):
        response = UDCAIMLTests.test_client.bot.ask_question("test", "Question")
        self.assertIsNotNone(response)
        self.assertEqual(response, "UDC Star Response")

    def test_udc_empty_string_question(self):
        response = UDCAIMLTests.test_client.bot.ask_question("test", "")
        self.assertIsNotNone(response)
        self.assertEqual(response, "")
