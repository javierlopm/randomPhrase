import psycopg2
import random

class speechElement:

    def __init__(self,description,code,dictcount):
        self.description = description
        self.code        = code
        self.dictcount   = dictcount

    def getCount(self):
        return self.dictcount

    def getDescription(self):
        return self.description

    def getCode(self):
        return self.code

class dictionary:
    """docstring for dictionary"""
    def __init__(self):
        try:
            self.conn = psycopg2.connect("dbname='dictionary' user='librarian' host='localhost' password='safepass'")
            cur = self.conn.cursor()
            cur.execute("""SELECT * from speech_count""")
            self.speechParts = []

            for row in cur:
                self.speechParts.append( speechElement(row[0],row[1],row[2]))

            cur.close()

        except:
            print("Couldn't connect to db 'dictionary' with user 'librarian' and password 'safepass")
            exit(1)

    def getWordByDescription(self,speech_part):
        cur   = self.conn.cursor()
        found = False

        for sp in self.speechParts:
            if sp.getDescription() == speech_part:
                found         = True
                numberOfWords = sp.getCount()
                speechCode    = sp.getCode()
                break

        if not found:
            print("Coudln't find the speech part " + speech_part)
            return None

        import random
        randomrow = random.randrange(0,numberOfWords-1)

        cur.execute("""SELECT * from part_of_speech  
                            WHERE speech_part = %s """,(speechCode,))

        rows   = cur.fetchall()
        wordId = rows[randomrow][0]

        cur.execute("""SELECT * from dictionary  
                WHERE word_id = %s """,(wordId,))

        return cur.fetchone()[1]


    def getWordByCode(self,speechCode):
        cur   = self.conn.cursor()
        found = False

        for sp in self.speechParts:
            if sp.getCode() == speechCode:
                found         = True
                numberOfWords = sp.getCount()
                break

        if not found:
            print("Coudln't find the speech part " + speech_part)
            return None

        import random
        randomrow = random.randrange(0,numberOfWords-1)

        cur.execute("""SELECT * from part_of_speech  
                            WHERE speech_part = %s """,(speechCode,))

        rows   = cur.fetchall()
        wordId = rows[randomrow][0]

        cur.execute("""SELECT * from dictionary  
                WHERE word_id = %s """,(wordId,))

        return cur.fetchone()[1]
    
    def makePhraseFromCode(self,speechCodeList):
        finalphrase = ""

        for elem in speechCodeList:
            finalphrase += " " + self.getWordByCode(elem)

        return finalphrase + "."


