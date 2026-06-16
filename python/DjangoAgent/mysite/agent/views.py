# agent/views.py
from django.http import JsonResponse
from django.shortcuts import render


def ask_agent(request):
    # Get the query parameter
    question = request.GET.get("q", "")

    # Simple mock response logic
    if not question:
        answer = "Please ask a question."
    elif "hello" in question.lower():
        answer = "Hello! I am your mock AI agent."
    else:
        answer = f"I received your question: '{question}'. (This is a mock response.)"

    return JsonResponse({"answer": answer})

def chat_page(request):
    return render(request,"agent/chat.html")
