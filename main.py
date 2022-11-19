from fastapi import FastAPI
from models import PreprocessingRequest # File with the Pydantic Model
from preprocessing import * # File with the preprocessing classes
import uvicorn

step_name_to_obj = {
    "replace_money":RegExReplaceMoney(),
    "replace_number_like":RegExReplaceNumberLike(),
    "replace_email":RegExReplaceEMail()
}

app = FastAPI()

@app.get("/")
async def root():
    return {"This is my project 4": "Prepocessing Text"}

@app.get("/preprocess/")
def preprocess(request: PreprocessingRequest):
    steps = request.steps
    text = str(request.text)
    preprocessed_text = ""+text
    
    # Apply preprocessing
    for step in steps:
        preprocessed_text = step_name_to_obj[step].preprocess(preprocessed_text)
    
    # Send back the preprocessed text
    response = { 
        "steps":steps,
        "text":text,
        "preprocessed_text":preprocessed_text
    }
    return response

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')