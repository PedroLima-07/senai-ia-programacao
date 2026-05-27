from openai import OpenAI

# Sua chave da NVIDIA
cliente = OpenAI(
    api_key="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",
    base_url="https://integrate.api.nvidia.com/v1"
)

emb = cliente.embeddings.create(
    model="nvidia/nv-embedqa-e5-v5",
    input="O que é inteligencia artificial",
    extra_body={
        "input_type":"query"
        }
    
)
print(emb.data[0].embedding)