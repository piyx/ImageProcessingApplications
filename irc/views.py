import os
from pathlib import Path
from re import M
from django.shortcuts import render
from PIL import Image

# Create your views here.
from django.http import HttpResponse

from utils.imagetotext import imagetotext
from utils.denoise import denoise_image, restore_image
from utils.classification import classify_image, classify_image_better


def index(request):
    return render(request, 'irc/index.html', context={})


def image_to_text(request):
    input_image = request.FILES["image_to_text_image"]
    base_path = "irc/"
    relative_path = f"static/irc/uploads/{input_image.name}"
    image_store_path = f"{base_path}{relative_path}"
    image_copy = Image.open(input_image)
    image_copy.save(image_store_path)
    text_found = imagetotext(image_store_path)
    return render(request, 'irc/ImagetoText.html', 
                  context={'input_image': relative_path, 'output_text': text_found})


def image_classification(request):
    ischecked = len(request.POST.getlist("multilabelcheckbox"))
    input_image = request.FILES["image_classification_image"]
    base_path = "irc/"
    relative_path = f"static/irc/uploads/{input_image.name}"
    modelname = "model.h5" if not ischecked else "model_better.h5"
    model_path = f"irc/static/irc/{modelname}"
    image_store_path = f"{base_path}{relative_path}"
    image_copy = Image.open(input_image)
    image_copy.save(image_store_path)
    function = classify_image if not ischecked else classify_image_better
    classification = function(base_path, relative_path, model_path)
    return render(request, 'irc/ImageClassification.html', 
                  context={"input_image": relative_path, "output": classification, "ischecked": ischecked})


def image_restoration(request):
    ischecked = len(request.POST.getlist("restorationcheckbox"))
    input_image = request.FILES["image_restoration_image"]
    base_path = "irc/"
    relative_path = f"static/irc/uploads/{input_image.name}"
    image_store_path = f"{base_path}{relative_path}"


    image_copy = Image.open(input_image)
    image_copy.save(image_store_path)

    if ischecked:
        output_image = restore_image(base_path, relative_path)
    else:
        output_image = denoise_image(base_path, relative_path)
    
    context = {'input_image': relative_path, 'output_image': output_image}
    return render(request, 'irc/ImageRestoration.html', context=context)


