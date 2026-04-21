from model.note import Note
class ParserNote:
    def __init__(self, notes_values):
        self.notes_values = notes_values
        self.liste_notes = []

            
    def parse(self):
        for matiere in self.notes_values.replace(" ", "").split('#'):
            name = self.get_name(matiere)
            devoirs, exam = self.get_notes(matiere)
            note = Note(name, devoirs, exam)
            self.liste_notes.append(note)
    
    def transform_to_float(self,note):
        try:
            return float(note)
        except:
            return None
        
    def get_notes(self, note):
            try:
                notes = note.strip(']').replace(",", ".").split('[')[1].split(':')
                exam = self.transform_to_float(notes[1]) if len(notes)>1 else None
                devoirs_str = notes[0].split('|') if len(notes)>=1 else [None]
                devoirs = [self.transform_to_float(note) for note in devoirs_str]
                return devoirs, exam 
            except:
                return [None], None

    def get_name(self, note):
        if 'math' in note.lower():
            return 'math'
        elif 'pc' in note.lower() or 'science' in note.lower():
            return 'pc'
        elif 'svt' in note.lower():
            return 'svt'
        elif 'fran' in note.lower():
            return 'fr'
        elif 'anglais' in note.lower():
            return 'ang'
        elif 'hg' in note.lower():
            return 'hg'
        else:
            return None
        
    

   