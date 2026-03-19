# 🗺️ Python Concept Map for AI-Native Developers

This guide focuses on **What** and **When** to use specific Python tools. Use this to guide your AI-assisted development—let the AI handle the syntax, while you handle the architecture.

---

## 🛠️ 1. Project Infrastructure
| Concept | What it is | When to use it |
| :--- | :--- | :--- |
| **Virtual Env (venv)** | An isolated playground for your project's packages. | **Always.** Never install packages globally. |
| **Pip & Requirements** | Tools to install and track your project's dependencies. | When you need to share your project or deploy it. |
| **.env Files** | A safe place to store API keys and secrets. | **Always** for OpenAI/Gemini keys. Never commit this to Git! |

## 🧠 2. Modern Python Logic
| Concept | What it is | When to use it |
| :--- | :--- | :--- |
| **Async / Await** | Running multiple tasks at the same time without waiting. | For API calls, AI generation, and database queries. |
| **Type Hinting** | Adding labels (like `: str`) to your code. | Always. It helps AI understand your code better and prevents bugs. |
| **Decorators** | A way to wrap a function to add extra logic (like logging). | For "sideways" logic like auth checks or measuring time. |
| **Context Managers** | The `with` statement. Handles setup and cleanup safely. | For opening files, database connections, or AI sessions. |

## 🌐 3. Web & API (FastAPI Focus)
| Concept | What it is | When to use it |
| :--- | :--- | :--- |
| **Pydantic Models** | Rules for what your data SHOULD look like. | Whenever you receive or send JSON data in an API. |
| **Middleware** | Logic that runs on every single request (like CORS). | For security, logging, or rate limiting. |
| **ORM (SQLModel)** | Talking to a database using Python instead of SQL. | When you need to save chats, users, or settings permanently. |

## 🚀 4. AI & LLM Essentials
| Concept | What it is | When to use it |
| :--- | :--- | :--- |
| **Embeddings** | Turning text into lists of numbers (vectors). | For "searching" through documents or finding similar text. |
| **Vector Database**| A special database for storing and searching embeddings. | When your AI needs to "remember" thousands of documents. |
| **RAG** | Giving the AI a "book" to read before it answers a question. | When you want an AI to answer questions about YOUR data. |
| **Tooling / Agents** | Giving the AI "buttons" to click (like searching the web). | When your chatbot needs to DO things, not just talk. |

---

### **How to use this map:**
When you're stuck, don't ask AI for "code." Ask: *"I need to implement a **Context Manager** for my **Vector Database** connection. Can you show me how?"*
