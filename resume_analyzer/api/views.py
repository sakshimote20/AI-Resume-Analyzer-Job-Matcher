from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer

import fitz
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@api_view(['GET'])
def job_list(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

def job_page(request):
    return render(request, "api/jobs.html")

@csrf_exempt
@api_view(['POST'])
def upload_resume(request):

    file = request.FILES.get('resume')

    if not file:
        return Response({"error": "No file uploaded"})

    text = ""

    pdf = fitz.open(stream=file.read(), filetype="pdf")

    for page in pdf:
        text += page.get_text()

    name = extract_name(text)

    jobs = Job.objects.all()

    results = []

    for job in jobs:

        score = calculate_match(text, job.description)

        results.append({
            "title": job.title,
            "company": job.company,
            "score": score
        })
    results.sort(key=lambda x: x['score'], reverse=True)

    return Response({
        "name": name,
        "matches": results
    })
def extract_name(text):

    lines = text.split("\n")

    for line in lines:
        if len(line.split()) <= 3 and line.strip() != "":
            return line.strip()

    return "Name not found"

def calculate_match(resume_text, job_text):

    documents = [resume_text, job_text]

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(vectors[0], vectors[1])

    score = similarity[0][0] * 100

    return round(score,2)