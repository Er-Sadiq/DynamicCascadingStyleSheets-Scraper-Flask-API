from openai import OpenAI
import json

client = OpenAI(api_key='') # put your api key here or export it as system varible

def get_css_selectors(html_content):
    prompt = f"""
    Here is an HTML snippet from a product page:
    {html_content}
    Identify the CSS selectors for:
    1. Review Title
    2. Review Body
    3. Review Rating
    4. Reviewer Name
    Respond with JSON format containing these selectors.
    """

    print("Prompt for CSS selectors:", prompt) 

    try:
        response =  client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        
   
        print("Response from OpenAI:", response)

        css_selectors = response['choices'][0]['message']['content'].strip()

        # Attempt to parse the response as JSON
        try:
            css_selectors_json = json.loads(css_selectors)
            return css_selectors_json
        except json.JSONDecodeError as json_error:
            print(f"Error decoding JSON: {json_error}")
            print(f"Raw response (not valid JSON): {css_selectors}")
            return None

    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return None
