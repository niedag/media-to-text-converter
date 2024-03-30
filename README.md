speech2text

The mp4 to mp3 converter is currently separate to the mp3 to text interface
1. First open up a venv and install all the required libraries
2. Add all mp4 files into the audio folder.
3. Run the command ```python mp4_converter.py```
4. Open the django server using  ```python manage.py runserver```
5. Navigate to the url /transcribe
6. Add the audio clip of your choosing and select Submit Audio File
7. Text will be added to a csv file at /validate/validate.csv

**Todo:**
- Take video media (mp4) convert to mp3 X
- New audio clips are created in the audio folder without overwritting current files in the directory X
- Run mp3 through GPT text inference X
- Take context from GPT response and insert it into a txt or csv file X
OR 
- Take the context from GPT output and run it through a NSFW filter

**Simple Validation process:**
- AFTER putting text through a filter, add it to a csv file and label it as either TRUE (Safe) or FALSE (Not safe)
- Take ~100 or sample texts that are pre-labeled as Safe or Unsafe and then compare it against the current model.
- Report the validation test as simply Num correct / total text

**Additional Tests**
- Check the validity of mp4 to mp3 AND mp3 to text

