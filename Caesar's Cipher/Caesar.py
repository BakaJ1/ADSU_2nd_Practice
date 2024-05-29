class caesar_alg:
    def __init__(self, text, caesar_coefficient):
        self.text = text.upper()
        self.coefru = caesar_coefficient % 33
        self.coefen = caesar_coefficient % 26
    def ENcrypt(self):
        result = ''
        for i in self.text:
            if i == ' ':
                result+= i
            elif ord(i) in range(65,91):
                if ord(i) + self.coefen > 90:
                    result+=chr(ord(i) + self.coefen - 26)
                else:
                    result+=chr(ord(i) + self.coefen)
            elif ord(i) in range(1040, 1072):
                if ord(i) + self.coefru > 1071:
                    result+=chr(ord(i) + self.coefru - 32)
                else:
                    result+=chr(ord(i) + self.coefru)
            else:
                return "Encryption error."
        return result
    def DEcrypt(self):
        result = ''
        for i in self.text:
            if i == ' ':
                result+= i
            elif ord(i) in range(65,91):
                if ord(i) - self.coefen < 65:
                    result+=chr(ord(i) - self.coefen + 26)
                else:
                    result+=chr(ord(i) - self.coefen)
            elif ord(i) in range(1040, 1072):
                if ord(i) - self.coefru < 1040:
                    result += chr(ord(i) - self.coefru + 32)
                else:
                    result += chr(ord(i) - self.coefru)
            else:
                return "Decryption error."
        return result