import unittest
from rsa import RSA
from key import RsaKey

class TestRSA(unittest.TestCase):

    def test_encrypt_decrypt_small_key(self):
        public_key = "0101-19bb"
        private_key = "9d5b-19bb"
        rsa_public = RSA(public_key)
        rsa_private = RSA(private_key)
        message = "WF"
        expected_encrypted = "8f84"
        encrypted = rsa_public.encrypt(message)
        self.assertEqual(encrypted, expected_encrypted)
        decrypted = rsa_private.decrypt(encrypted)
        self.assertEqual(decrypted, message)

    def test_encrypt_decrypt_large_key(self):
        public_key = "010001-c9f91a9ff3bd6d84005b9cc8448296330bd23480f8cf8b36fd4edd0a8cd925de139a0076b962f4d57f50d6f9e64e7c41587784488f923dd60136c763fd602fb3"
        private_key = "81b08f4eb6dd8a4dd21728e5194dfc4e349829c9991c8b5e44b31e6ceee1e56a11d66ef23389be92ef7a4178470693f509c90b86d4a1e1831056ca0757f3e209-c9f91a9ff3bd6d84005b9cc8448296330bd23480f8cf8b36fd4edd0a8cd925de139a0076b962f4d57f50d6f9e64e7c41587784488f923dd60136c763fd602fb3"
        rsa_public = RSA(public_key)
        rsa_private = RSA(private_key)
        message = "The night is dark and full of terrors"
        expected_encrypted = "445b349e7318ad6af16b0bbb718be88ba1c41751f95751cd58857f88fe31f970405c6ec3f16d79172543bf4e571b5596d212f3e79cd08ef14abd244e325b80"
        encrypted = rsa_public.encrypt(message)
        self.assertEqual(encrypted, expected_encrypted)
        decrypted = rsa_private.decrypt(encrypted)
        self.assertEqual(decrypted, message)

if __name__ == '__main__':
    unittest.main()
