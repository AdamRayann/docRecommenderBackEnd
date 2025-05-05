import os

from openai import OpenAI


api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

medical_prompt = """
אנא נתח את הדוח הרפואי המצורף והערך את ההמלצות שניתנו לחולה בהתבסס על נתוניו הרפואיים.
המטלה שלך היא לבדוק:
• סיכונים אפשריים בשילוב התרופות שהומלצו.
• אינטראקציות מסוכנות במיוחד (למשל: סיכון לדימום, נזק לכליות, לחץ דם).
• האם בחירת התרופות מתאימה לפרופיל החולה ולרקע המחלות.
• האם קיימות חלופות בטוחות יותר.
• לתת המלצות מקצועיות לרופא להמשך טיפול בטוח וזהיר יותר.

הוראות לפלט המבוקש:
• כתוב את התשובה בעברית.
• פרט על סיכונים חשובים שיש לשים לב אליהם.
• תן המלצות חלופיות או זהירות בטיפול.
• הדגש נקודות קריטיות במיוחד (לדוגמה: דימום, כליות, לב).
• תיצור טבלה מסכמת לכל הסיכונים והמלצות בצורה שמוכנה לשימוש עבור תיק רפואי או דיון עם הצוות הרב-תחומי.
"""

def analyze_medical_text(text):
    try:
        full_prompt = f"{medical_prompt}\n\n---\n\n{text}"
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "אתה עוזר רפואי."},
                {"role": "user", "content": full_prompt}
            ],
            temperature=0.4,
            max_tokens=1500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"