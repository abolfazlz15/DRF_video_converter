# DRF_video_converter
Video to audio converter with django and DRF and moviepy 

1. Have Login and Register with OTP and JWT.
2. Compliance with the principles of clean coding.
3. use Celery as task queue and task schuler
4. use Rabbitmq as message broker 

## Run project
- In terminal: `git clone https://github.com/abolfazlz15/DRF_video_converter.git`
- cd `DRF_video_converter/` Where the requirements.txt is
- In terminal: `python -m venv venv`
- activate your venv: in windows `cd venv\scripts\activate` in linux: `venv/bin/activate`
- Run `pip install requirements.txt`
- cd `src/` where the manage.py is
- Run `python manage.py runserver`