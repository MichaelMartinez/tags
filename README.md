# Tag Creator

----

## Install

1. Local LLM - `pip install gpt4all openai`
2. run `python main.py`
3. Select folder for markdown file discovery
4. call the API
5. WIP here...

---

## Example call to GPT4All API

```python
from gpt4all import GPT4All
model = GPT4All("ggml-model-gpt4all-falcon-q4_0.bin")
output = model.generate("The capital of France is ", max_tokens=3)
print(output)
```

----

TODO:

1. Parse and strip files for text to be sent to LLM
2. Send text to LLM for tagging
   1. Need very specific prompts here
3. Return the tags and let user decide if the tags will be appended or discarded
