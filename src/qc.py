import base64
from openai import OpenAI
import os

class QualityControl:
   
    def __init__(self, image_path, threshold):
      self.image_path = image_path
      self.threshold = threshold
      self.extract_keywords_from_image()
      

    def extract_keywords_from_image(self):
        """Retrieves keywords from an image using GPT.

        Args:
            None
        Returns:
            The keywords found in the transcription.
        """
        with open(self.image_path, "rb") as image_file:
            image_data = image_file.read()

        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

        response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
            "role": "user",
            "content": [
                {"type": "text", "text": """
                What’s in this image? Output 10 keywords and only the keywords, nothing else. Comma and space seperated (i.e. hi, x, y...)
                Each keyword is only one word. Use only concrete nouns (no abstract nouns)
                """},
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64.b64encode(image_data).decode()}"
                },
                },
            ],
            }
        ],
        max_tokens=300,
        )

        # Parse the response to get keywords
        keywords = response.choices[0].message.content.split(', ')
        
        self.keywords = keywords

    def count_keywords_in_transcription(self, transcription):
        """Counts the number of keywords present in a transcription.

        Args:
            transcription: The text of the transcription.

        Returns:
            The number of keywords found in the transcription.
        """

        keyword_count = 0
        for keyword in self.keywords:
            if keyword.lower() in transcription.lower(): keyword_count += 1
        return keyword_count
    
    def fits_quality_control(self, transcription):
        """Checks if the transcription qualifies for the respective image.

        Args:
            transcription: The text of the transcription.

        Returns:
            True if it qualifies and False if it doesn't.
        """
        if len(transcription.split(' ')) < self.threshold:
            return False
        if self.count_keywords_in_transcription(transcription) < 2:
            return False
        return True