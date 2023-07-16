# text_appender.py

class TextAppender:
    def append_text(self, file, processed_text):
        # Code to append the processed text to the original file
        # Replace this with the actual text appending code
        with open(file, "a") as f:
            f.write(processed_text)
