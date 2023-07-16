# file_finder.py

import os

class FileFinder:
    def find_files(self, directory):
        files = []
        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                if self.is_markdown_file(filename):
                    files.append(os.path.join(root, filename))
        return files
    
    def is_markdown_file(self, file):
        _, ext = os.path.splitext(file)
        return ext.lower() == ".md"
