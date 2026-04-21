from utils.parser_notes import ParserNote
from services.validator import Validateur
from model.etudiant import Etudiant
class FileReader:
    validator = Validateur()
    data = []
    students = []

    def readfile(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                self.data.append(line.rstrip('\n'))
            self.data = self.data[1:]    
        
    def create_students(self, sep):
        for line in self.data:
            col = line.split(sep)

            note = col[-1]
            if col[-1] and col[-1][0] == '#':
                note = col[-1][1:] 
                
            parser = ParserNote(note)
            parser.parse()
            # print(col[-1])
            student = Etudiant(col[0], col[1], col[2], col[3], col[4], col[5], parser.liste_notes)
            self.validator.validate_student(student)
            self.students.append(student)




