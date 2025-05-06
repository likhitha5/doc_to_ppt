PRESENTATION_TEMPLATE = """
You are given text content along with associated image file paths, organized by headings.

Your task is to create a presentation with the following structure:
1. Title slide
2. Agenda/Overview
3. Main content slides (5-7 slides)
4. Summary/Conclusion

Audience: {audience_type}

audience_type == general: Suitable for introductory, broad-topic presentations (e.g., "What is Artificial Intelligence?"). Make it look little informal, casual, fun, creative with cool quotes


audience_type == educational: Appropriate for school/university lectures (e.g., "Introduction to Computer Science").

audience_type == technical: Deep dive content for engineers or developers (e.g., "Building Scalable Web Applications").

audience_type == business: Business-oriented content (e.g., "Quarterly Financial Performance Report").

Make presentation according to the audience.

Additional instructions: {instructions}

Instructions: Use the provided headings to break the content into slides. For each main content slide, if images are associated with the heading, include exactly one relevant image using its file path. If no image is available, set "image": null.

Return the presentation in the following JSON format:
{{
    "slides": [
        {{
            "type": "title|content|summary",
            "title": "Slide title",
            "content": ["bullet point 1", "bullet point 2"],
            "notes": "speaker notes",
            "image": "saved_uploads/filename.png" or null
        }}
    ]
}}

Text:
{text}

Image associations by heading:
{heading_image_mapping}
"""
