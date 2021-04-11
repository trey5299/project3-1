from cis301.phonebill.abstract_phonebill import AbstractPhoneBill
from cis301.phonebill.phonebill_parser import PhoneBillParser


class TextParser(PhoneBillParser):
    def parse(self) -> AbstractPhoneBill:
        pass

    def test_PhoneCall(self):
        parsed = self.parser.parse(self.category_url)
        self.assertEqual(parsed, self.category_embed)

    def test_Phonebill(self):
        parsed = self.parser.parse('Testing %s' % self.category_url)
        self.assertEqual(parsed, self.category_embed)

