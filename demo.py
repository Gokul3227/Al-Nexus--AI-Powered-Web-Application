import google.generativeai as genai

genai.configure(api_key="AIzaSyB3KzgGSOTjph-xRqsOV-_fSKJPnqHPUyg")

models = genai.list_models()
for model in models:
    print(model.name)
