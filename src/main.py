from google import genai
import time

# ==========================================
# AI Home Lab Assistant
# ==========================================

print("=" * 50)
print("🚀 AI Home Lab Assistant")
print("=" * 50)

# Create a client (connects to Google Cloud Vertex AI)
client = genai.Client(vertexai=True)

print("✅ Connected to Vertex AI")
print("🤖 Model: Gemini 2.5 Flash")
print("💡 Type 'exit' to quit.\n")

# Give Gemini a role/personality
system_prompt = """
You are a senior Google Cloud Customer Engineer.

Your job is to:
- Teach cloud concepts clearly.
- Explain step-by-step.
- Keep answers concise but helpful.
- Assume the user is learning Google Cloud and AI engineering.
"""

conversation_count = 1

# ==========================================
# Main Chat Loop
# ==========================================

while True:

    print("-" * 50)
    print(f"Conversation #{conversation_count}")

    question = input("\n💬 You: ")

    # Exit the application
    if question.lower() == "exit":
        print("\n👋 Thanks for using AI Home Lab Assistant!")
        break

    # Combine the system prompt with the user's question
    prompt = f"""
{system_prompt}

User Question:
{question}
"""

    print("\n⏳ Thinking...")

    start = time.time()

    # Send the request to Gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    end = time.time()

    print("\n🤖 Gemini:\n")
    print(response.text)

    print("\n" + "-" * 50)
    print(f"⏱ Response Time: {end - start:.2f} seconds")

    conversation_count += 1

print("\nApplication Closed.")