from app import process_chat
import unittest

class MyTestCase(unittest.TestCase):
    def test_whats_your_name(self):
        rsp = process_chat("What is your name?")
        print(rsp)
        self.assertEqual(rsp, 'My name is Alexa')

    def test_whats_your_name(self):
        rsp = process_chat("Are you male or female?")
        print(rsp)
        self.assertEqual(rsp, 'I am Female')


if __name__ == '__main__':
    unittest.main()
