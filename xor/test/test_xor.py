import unittest
from xor import XOR

class TestXOR(unittest.TestCase):

    def setUp(self):
        # Example key and messages for testing
        self.key = '576861742069732064656164206d6179206e6576657220646965'
        self.xor = XOR(self.key)
        self.message = 'You know nothing, Jon Snow'
        self.encrypted_message = '20070f2700071c6a4449060a490515164e4e12190b190011063c'

    def test_encrypt(self):
        # Test encryption
        encrypted = self.xor.encrypt(self.message)
        self.assertEqual(encrypted, self.encrypted_message)

    def test_decrypt(self):
        # Test decryption
        decrypted = self.xor.decrypt(self.encrypted_message)
        self.assertEqual(decrypted, self.message)

    def test_encrypt_decrypt(self):
        # Test that encrypting and then decrypting returns the original message
        encrypted = self.xor.encrypt(self.message)
        decrypted = self.xor.decrypt(encrypted)
        self.assertEqual(decrypted, self.message)

if __name__ == '__main__':
    unittest.main()
