from django.shortcuts import render, redirect, get_object_or_404
from .models import Testimonial
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .forms import TestimonialForm
from django.contrib.auth.decorators import login_required


def testimonial_create(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            messages.success(request, "Testimonial added successfully!")
            return redirect('/testimonials')
    else:
        form = TestimonialForm()
    return render(request,
                  'testimonials/testimonial_create.html', {'form': form})


@login_required
def testimonial_edit(request, testimonial_id):
    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)

    # Check if the current user is the owner of the testimonial
    if testimonial.user != request.user:
        messages.error(request,
                       "You are not authorized to edit this testimonial.")
        return redirect('/testimonials')

    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, "Testimonial updated successfully!")
            return redirect('/testimonials')
    else:
        form = TestimonialForm(instance=testimonial)

    return render(request,
                  'testimonials/testimonial_edit.html',
                  {'form': form, 'testimonial': testimonial})


def testimonial_delete(request, testimonial_id):
    try:
        testimonial = Testimonial.objects.get(id=testimonial_id)

        # Check if the logged-in user is the owner of the testimonial
        if request.user == testimonial.user:
            testimonial.delete()
            messages.success(request, 'Testimonial deleted successfully.')
            return redirect('/testimonials')
        else:
            messages.error(request,
                           "You're not authorized to delete this testimonial.")
    except ObjectDoesNotExist:
        messages.error(request, 'Testimonial does not exist.')

    return redirect('testimonials:testimonial_list')


def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    return render(request,
                  'testimonials/testimonial_list.html',
                  {'testimonials': testimonials})
