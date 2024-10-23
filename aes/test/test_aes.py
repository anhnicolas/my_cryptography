import unittest
from aes import AES

class TestAES(unittest.TestCase):

    def test_aes_encryption_decryption(self):
        message = "All men must die"
        key_hex = "57696e74657220697320636f6d696e67"
        aes_instance = AES(key=key_hex, single_block=True)
        cipher_text = aes_instance.encrypt(message)
        expected_cipher = "744ce22c385958348f0df26eceb62eef"
        self.assertEqual(cipher_text, expected_cipher, "The cipher text does not match the expected value")
        decrypted_message = aes_instance.decrypt(cipher_text)
        self.assertEqual(decrypted_message, message, "The decrypted message does not match the original")

if __name__ == '__main__':
    unittest.main()
