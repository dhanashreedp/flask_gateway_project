# data_service/processor/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def process_text(request):
    text = request.data.get("text")
    if not text:
        return Response({"error": "No text provided for processing"}, status=400)
    processed_text = f"Data Service Processed: {text.upper()}" # Example processing
    return Response({"original_text": text, "processed_text": processed_text})