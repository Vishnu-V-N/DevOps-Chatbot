import unittest

class TestChatbot(unittest.TestCase):
    def test_response(self):
        self.assertEqual(chatbot_response("Hello"), "Hi there! How can I help you?")

    def test_invalid_input(self):
        self.assertEqual(chatbot_response(""), "I'm sorry, I didn't understand that.")

    def test_multiple_inputs(self):
        inputs = ["Hi", "How are you?", "What can you do?"]
        expected_outputs = ["Hi there! How can I help you?", "I'm doing well, thank you!", "I can assist you with various tasks."]
        for input_text, expected_output in zip(inputs, expected_outputs):
            self.assertEqual(chatbot_response(input_text), expected_output)

if __name__ == '__main__':
    unittest.main()