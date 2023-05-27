FROM python:3.8
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install git+https://github.com/openai/whisper.git
# RUN pip install -U openai-whisper
# RUN apt update && apt install ffmpeg -y
COPY app.py ./
# expose the port at which we'll run our app
EXPOSE 5050

# sleep to wait for sql server to boot then run our app
CMD python app.py