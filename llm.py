from google import genai 
from config import settings



client = genai.Client(api_key =  settings.GEMINI_API_KEY)

def ask_query(query : str ):
    response = client.models.generate_content(
        model = "gemini-3-flash-preview" ,
        contents = query
    )

    return response.text 





