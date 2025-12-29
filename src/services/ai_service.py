import os
from groq import Groq

def generate_analysis(data, system_prompt):
    try:
        # Create client inside the function
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": str(data)}
            ],
            temperature=0.4,
            max_tokens=1024
        )

        content = response.choices[0].message.content
        content = content.replace('\\n', '\n')
        
        return {
            "success": True,
            "content": content
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }