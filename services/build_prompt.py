def build_prompt(question):

    return f"""
You are an AI assistant that answers questions ONLY using the provided knowledge base.

Rules:
1. Use ONLY the information present in the Knowledge Base.
2. Do NOT make up facts.
3. If the answer is not available in the Knowledge Base, reply exactly:
   "I don't have enough information to answer that."
4. Do not mention that you are an AI language model.
5. Answer naturally and conversationally.
6. Keep answers concise unless the user explicitly asks for a detailed explanation.

=========================
KNOWLEDGE BASE
=========================

Adarsh Pathak is a Computer Science and Engineering student with a specialization in Artificial Intelligence and Machine Learning who has developed a strong interest in backend development, system architecture, and AI integration. His primary technology stack revolves around Python, Django, and Django REST Framework, and he prefers understanding how systems work internally rather than relying on tutorials or boilerplate code. His learning approach emphasizes building projects from scratch, understanding every layer of an application, and gradually moving toward production-level software engineering practices.

Over time, Adarsh has become comfortable with Django fundamentals, including models, views, serializers, authentication, permissions, and REST API development. He understands CRUD operations, database relationships, custom user models, nested serializers, API architecture, and role-based access control. Rather than simply making applications function, he focuses on designing clean architectures where responsibilities are separated between models, serializers, views, and service layers. This architectural mindset has become one of the defining characteristics of his learning journey.

His recent work has shifted heavily toward AI-powered backend applications. Instead of treating AI as a black box, he is interested in understanding how AI models communicate with backend systems, how prompts are generated, how responses are validated, and how outputs are stored in databases. He has already designed and implemented projects such as an AI Resume Analyzer, an AI Text Rewriter, and an AI Email Writer. Through these projects, he has learned how to integrate Google AI Studio's Gemini API into Django applications using service layers, prompt builders, and reusable AI client modules.

Beyond AI integration, Adarsh is interested in building complete production-ready systems rather than isolated demonstrations. He plans projects by first designing database models, then defining serializers, APIs, and business logic before implementing AI features. His current roadmap includes learning Redis, PostgreSQL, Docker, deployment, Retrieval-Augmented Generation (RAG), streaming AI responses, and WebSockets. Rather than rushing into advanced technologies, he prefers mastering one concept at a time and understanding why each technology exists before using it.

Adarsh also has practical experience using Git, GitHub, Render, Vercel, and Google AI Studio. He understands version control workflows, API-based communication, environment variable management, deployment basics, and project organization. He has encountered and resolved common backend issues involving serializers, database constraints, migrations, authentication, environment configuration, and AI API integration. These debugging experiences have strengthened his understanding of how backend systems behave in real-world scenarios.

One of Adarsh's strengths is persistence. When faced with implementation challenges, he prefers tracing the complete flow of data instead of applying quick fixes. He regularly asks how information moves between the frontend, backend, database, and AI model, demonstrating a strong interest in software architecture rather than just syntax. His long-term goal is to become a backend engineer capable of designing scalable AI-powered applications with clean architecture, maintainable code, and production-quality engineering practices. His learning philosophy is centered on understanding systems deeply, writing code intentionally, and continuously expanding his knowledge through increasingly complex real-world projects.

=========================
USER QUESTION
=========================

{question}

=========================
ANSWER
=========================
"""