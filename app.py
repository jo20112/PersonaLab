import streamlit as st
from transformers import pipeline

# تحميل نموذج تحليل النص بالعربي
@st.cache_resource  # لتخزين النموذج في الذاكرة المؤقتة
def load_model():
    return pipeline("text-generation", model="aubmindlab/aragpt2-medium")

personality_analyzer = load_model()

# قائمة الأسئلة بالعربي
questions_arabic = [
    "ما هو الشيء الذي تستمتع بفعله في وقت الفراغ؟",
    "كيف تتعامل مع المواقف الصعبة أو الضغوط؟",
    "ما هي الصفة التي تعتقد أن الآخرين يعتبرونها أفضل ما فيك؟",
    "هل تفضل العمل في فريق أم بشكل فردي؟",
    "ما هو أكبر حلم تريد تحقيقه في الحياة؟",
    "كيف تصف علاقتك مع الأصدقاء والعائلة؟",
    "ما هو الشيء الذي يجعلك تشعر بالإلهام؟",
    "هل تعتبر نفسك شخصًا منظمًا أم عفويًا؟",
    "ما هو أكثر شيء تقدره في الحياة؟",
    "كيف تتعامل مع التغييرات المفاجئة في حياتك؟"
]

# دالة لتحليل الإجابة بالعربي
def analyze_personality(answer):
    prompt = f"""
    قم بتحليل الإجابة التالية وصف الشخصية بشكل مفصل مع تقديم نصيحة في النهاية. تأكد من أن التحليل واضح ومنطقي:
    
    الإجابة: {answer}
    
    التحليل:
    """
    analysis = personality_analyzer(prompt, max_length=300, num_return_sequences=1, temperature=0.7)
    return analysis[0]['generated_text']

# واجهة المستخدم
st.title("تحليل الشخصية باستخدام الذكاء الاصطناعي")
st.write("أجب على الأسئلة التالية لتحليل شخصيتك:")

# تخزين الإجابات
answers = []

# عرض الأسئلة وجمع الإجابات
st.write("**الأسئلة:**")
for i, question in enumerate(questions_arabic):
    st.write(f"**السؤال {i+1}:** {question}")
    answer = st.text_input(f"الإجابة على السؤال {i+1}:", key=f"q{i}")
    answers.append(answer)

# زر لتحليل الإجابات
if st.button("حلل الإجابات"):
    if all(answers):  # التأكد من أن جميع الأسئلة قد تمت الإجابة عليها
        with st.spinner("جاري تحليل الإجابات..."):
            combined_answers = "\n".join(answers)  # جمع الإجابات في نص واحد
            analysis = analyze_personality(combined_answers)
        
        st.success("تم التحليل بنجاح!")
        st.write("**نتيجة التحليل:**")
        st.write(analysis)
    else:
        st.warning("من فضلك أجب على جميع الأسئلة قبل الضغط على زر التحليل.")