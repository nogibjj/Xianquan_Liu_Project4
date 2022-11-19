import re

class BaseRegExPreprocessing:
    regex = r""
    replace_token = " <GENERIC_TOKEN> "

    def preprocess(self, text):
        return re.sub( self.regex, self.replace_token, text )
 
class RegExReplaceNumberLike(BaseRegExPreprocessing):
    regex = r"(:?\d+.)+"
    replace_token = " <NUMBER_LIKE> "

class RegExReplaceMoney(BaseRegExPreprocessing):
    regex = r'\w[$][ ]\d{1,3}(?:\.\d{3})*?,\d{2}'
    replace_token = " <MONEY> "

class RegExReplaceEMail(BaseRegExPreprocessing):
    regex = r"\w+\@\w+(?:\.\w+)+"
    replace_token = " <Email> "