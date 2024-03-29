speech2text

Todo:
- Take video media (mp4) convert to mp3
- Run mp3 through GPT text inference
- Take context from GPT response and insert it into a txt or csv file
OR 
- Take the context from GPT output and run it through a NSFW filter

**Simple Validation process:**
- AFTER putting text through a filter, add it to a csv file and label it as either TRUE (Safe) or FALSE (Not safe)
- Take ~100 or sample texts that are pre-labeled as Safe or Unsafe and then compare it against the current model.
- Report the validation test as simply Num correct / total text
