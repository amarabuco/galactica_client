FROM python:3.9.16-slim-buster

WORKDIR /usr/src/app

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

RUN pip install streamlit
RUN pip install transformers accelerate

COPY . .

CMD [ "python", "./your-daemon-or-script.py" ]