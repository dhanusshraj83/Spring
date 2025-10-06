

import onnxruntime as ort
from transformers import AutoTokenizer
import numpy as np

class TinyLlamaONNX:
    def _init_(self, onnx_path: str, model_id: str):
        # Create ONNX inference session
        self.session = ort.InferenceSession(onnx_path, providers=["CPUExecutionProvider"])
        # Or for GPU: providers=["CUDAExecutionProvider"]
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)

    def predict(self, prompt: str, max_length: int = 64) -> str:
        # Tokenize
        inputs = self.tokenizer(prompt, return_tensors="np", padding=True, truncation=True)
        input_ids = inputs["input_ids"]
        attention_mask = inputs["attention_mask"]

        # Prepare ONNX inputs
        ort_inputs = {
            "input_ids": input_ids.astype(np.int64),
            "attention_mask": attention_mask.astype(np.int64),
        }

        # Run inference
        outputs = self.session.run(None, ort_inputs)  # returns list of outputs
        logits = outputs[0]  # shape (batch_size, seq_len, vocab_size)

        # For simplicity: pick the last token by argmax
        last_logits = logits[:, -1, :]
        next_token_id = np.argmax(last_logits, axis=-1)[0]

        # Decode token back to text
        decoded = self.tokenizer.decode(next_token_id, skip_special_tokens=True)
        return decoded