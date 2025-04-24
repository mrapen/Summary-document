model = "gpt-4o-mini"
message = {
    "English":{
        "Fragment":"""
        You are an expert analyst. For each provided text fragment:
        1. Identify the single main idea.
        2. List two to three key details or arguments that support it.
        3. If the fragment contains any conclusions or recommendations, state them in a separate sentence.

        Fragment:
        \"\"\"
        {text}
        \"\"\"

        Your response should follow this format:

        Main Idea:
        - …

        Key Details:
        - …
        - …
        - …

        Conclusions/Recommendations (if any):
        - …
        """,
        "Summarize":"""
        You are a senior editor. Based on the provided fragment summaries:
        1. Craft a single headline (one line) that captures the essence of the entire document.
        2. Write a consolidated paragraph (3–5 sentences) summarizing all main ideas.
        3. Formulate three key takeaways or recommendations at the document level.

        Intermediate Fragment Summaries:
        {summaries}

        Your response should be structured as follows:

        Headline:
        …

        Consolidated Summary:
        …

        Three Key Takeaways/Recommendations:
        1. …
        2. …
        3. …
        """,
        "Additional":"""
        Additional Requirements:
        {additional_requirements}
        """
    },
    "Українська": {
        "Fragment":"""
        Ви — експерт-аналитик. Для кожного наведеного фрагмента тексту:
        1. Визначте одну головну ідею.
        2. Перерахуйте дві-три ключові деталі або аргументи, що її підтримують.
        3. Якщо у фрагменті є висновки або рекомендації — сформулюйте їх окремим реченням.

        Фрагмент:
        \"\"\"
        {text}
        \"\"\"

        Ваша відповідь має бути в такому форматі:

        Головна ідея:
        - …

        Ключові деталі:
        - …
        - …
        - …

        Висновки/рекомендації (якщо є):
        - …
        """,
        "Summarize":"""
        Ви — старший редактор. На основі наведених підсумків окремих фрагментів:
        1. Складіть єдиний заголовок (1 рядок), який відображає суть всього документа.
        2. Напишіть консолідований абзац (3–5 речень), що узагальнює всі головні ідеї.
        3. Сформулюйте три ключові висновки або рекомендації на рівні всього документа.

        Проміжні підсумки фрагментів:
        {summaries}

        Ваша відповідь має бути структурована так:

        Заголовок:
        …

        Консолідований висновок:
        …

        Три ключові висновки/рекомендації:
        1. …
        2. …
        3. …
        """,
        "Additional":"""
        Додаткові вимоги:
        {additional_requirements}
        """
    }
}