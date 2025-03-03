import google.generativeai as genai

genai.configure(api_key="API KEY HERE TO CHECK THE LLM MODELS")

models = genai.list_models()
for model in models:
    print(model.name)
