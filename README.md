# Tag Creator

----

## Install

1. Local LLM - `pip install gpt4all`

```python
from gpt4all import GPT4All
model = GPT4All("ggml-model-gpt4all-falcon-q4_0.bin")
output = model.generate("The capital of France is ", max_tokens=3)
print(output)
```
