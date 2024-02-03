#Aggregation and Composition
class Character:
    def __init__(self,char):
        self.char = char
    def __str__(self):
        return self.char

class Word:
    def __init__(self):
        self.chars = []
    def add_char(self,char):
        self.chars.append(Character(char))#Composition
    def __str__(self):
        return ''.join(str(char) for char in self.chars) 
    
class Paragraph:
    def __init__(self):
        self.words = []
    def add_words(self,word):
        self.words.append(word)
    def __str__(self):
        return ''.join(str(word) for word in self.words) 
    
class File:
    def __init__(self):
        self.paragraphs = []
    def add_paragraph(self,paragraph):
        self.paragraphs.append(paragraph)
    def __str__(self):
        return ''.join(str(paragraph) for paragraph in self.paragraphs) 

class Folder:
    def __init__(self):
        self.files = []
    def add_files(self,file):
        self.files.append(file)
    def __str__(self):
        return '\n\n'.join(str(file) for file in self.files) 
    
class User:
    def __init__(self):
        self.folder = [Folder(),Folder()]#Composition
    def __str__(self):
        return '\n\n\n'.join(str(folder) for folder in self.folders)