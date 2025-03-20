from transformers import pipeline

# تحميل نموذج تحليل النص
personality_analyzer = pipeline("text-generation", model="gpt2")

# دالة لتحليل الإجابة
def analyze_personality(answer):
    prompt = f"Analyze the following answer and determine the personality traits:\n\n{answer}\n\nAnalysis:"
    analysis = personality_analyzer(prompt, max_length=100, num_return_sequences=1)
    return analysis[0]['generated_text']

# مثال على إجابة المستخدم
user_answer = "I enjoy spending time with friends and trying new activities."
analysis = analyze_personality(user_answer)
print("Personality Analysis:\n", analysis)