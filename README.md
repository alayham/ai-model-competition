# The AI Model Competetion Script
Be the judge of your AI Models, Ask them a question and rate their answers.+

Watch the video: https://www.youtube.com/watch?v=saI-iWK40_s

# Origin story
This script was originally created on video during the tenth episode of the first season of the devlab series. [See the video](https://www.youtube.com/watch?v=EX8VcKmCI9s) or [read the article](https://medium.com/@al-saleh/the-devlab-series-season-01-episode-10-a621b80d6d97)

# Requirements
- A running [Ollama server](https://ollama.ai)
- A python virtual invironment

# Install
In your python virtual environment, run 
```
pip install -r requirements.txt
```

# Usage
Edit `main.py` change the IP of the Ollama server, and the prompt, then run this command in your python virtual environment.
```
python main.py
```
# Current status
The script works in my devlab, I still did not get any feedback from other developers about it. please test it and let me know how it works.

# Future improvements
When I have some time, I would like to do some of the following:
- Add the processing time to the output. 
- Make the script more user friendly.
- Allow grading the answers, and saving the grades in some type of DB.
- Allow sharing the prompt and the grading to the community.

# License
MIT License
