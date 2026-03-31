"""
llm_loader.py

Loads the LLM model and generates responses.
"""

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

print("Loading LLM model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float32
)

model.eval()

print("Model loaded successfully")


def generate_answer(prompt: str) -> str:
    """
    Generate answer using the LLM
    """

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        padding=True,
        truncation=True
    )

    with torch.no_grad():

        outputs = model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_new_tokens=120,
            temperature=0.3,
            top_p=0.9,
            repetition_penalty=1.2,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )

    decoded = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    # Remove prompt text from output
    response = decoded.replace(prompt, "").strip()

    # Stop if model starts repeating instructions
    if "Context:" in response:
        response = response.split("Context:")[0]

    return response