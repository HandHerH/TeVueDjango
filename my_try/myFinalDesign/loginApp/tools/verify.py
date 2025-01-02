import re


class VerifyForm:
    regexes = {
        'phone': r'^1[3-9]\d{9}$',
    }

    @classmethod
    def verify(cls, filed, value):
        pattern = cls.regexes.get(filed)
        if not pattern:
            return False

        if re.match(pattern, value):
            return True
        return False
