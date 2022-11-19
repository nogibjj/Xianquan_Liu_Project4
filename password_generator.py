from fastapi import FastAPI
import uvicorn
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"This is my project 4": "Password Generator"}


@app.get("/password/")
async def password():
    uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
    uppercaseLetter2=chr(random.randint(65,90))
    lowercaseletter1 =chr(random.randint(97,122))
    lowercaseletter2 =chr(random.randint(97,122))
    digit1 = chr(random.randint(48,57))
    digit2 = chr(random.randint(48,57))
    punctuationsign1 = chr(random.randint(33,152))
    punctuationsign2 = chr(random.randint(33,152))
    #Generate password using all the characters, in random order
    password = uppercaseLetter1 + uppercaseLetter2 +lowercaseletter1+lowercaseletter2+digit1+digit2+punctuationsign1+punctuationsign2
    temp_pass = list(password)
    random.shuffle(temp_pass)
    password = ''.join(temp_pass)
    return {"newpassword": f"{password}"}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')