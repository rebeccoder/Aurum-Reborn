from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic import CreateView
from .forms import CreatorsForm
from .models import Creator


class Creators(generic.ListView):
    """
    A view to return the list of creators.
    """

    model = Creator
    context_object_name = "creators"
    template_name = "creators/creators.html"


class CreateCreator(UserPassesTestMixin,
                    SuccessMessageMixin, generic.CreateView):
    """
    A view to display the creator form.
    To add new creators. Restricted to superusers only.
    """

    model = Creator
    form_class = CreatorsForm
    success_message = "Successfully added creator!"
    success_url = reverse_lazy("creators")

    def test_func(self):
        """
        Check if the user is a superuser.
        """
        return self.request.user.is_superuser

    def handle_no_permission(self):
        """
        If the user is not a superuser, display a toast message.
        """
        messages.error(self.request,
                       "You need proper authorization to do that.")
        return redirect("home")

    def form_invalid(self, form):
        """
        Show toast error message if the form is invalid.
        """
        messages.error(
            self.request,
            "Oops, something went wrong! Please double-check the form."
        )
        return super().form_invalid(form)


class UpdateCreator(UserPassesTestMixin,
                    SuccessMessageMixin, generic.UpdateView):
    """
    A view to display the creator form.
    To update creators. Restricted to superusers only.
    """

    model = Creator
    form_class = CreatorsForm
    success_message = "Successfully updated creator!"
    success_url = reverse_lazy("creators")

    def test_func(self):
        """
        Check if the user is a superuser.
        """
        return self.request.user.is_superuser

    def handle_no_permission(self):
        """
        If the user is not a superuser, display a toast message.
        """
        messages.error(self.request,
                       "You need proper authorization to do that.")
        return redirect("home")


class CreatorDeleteView(UserPassesTestMixin,
                        SuccessMessageMixin, generic.DeleteView):
    """
    A view to delete a creator. Restricted to superusers only.
    """

    model = Creator
    success_url = reverse_lazy('creators')
    success_message = "Creator successfully deleted."

    def test_func(self):
        """
        Check if the user is a superuser.
        """
        return self.request.user.is_superuser

    def handle_no_permission(self):
        """
        If the user is not a superuser, display a toast message.
        """
        messages.error(self.request,
                       "You need proper authorization to do that.")
        return redirect("home")

    def delete(self, request, *args, **kwargs):
        """
        Handle the delete operation.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        messages.success(self.request, self.success_message)
        self.object.delete()
        return redirect("creators")


class CreatorsFormView(CreateView):
    model = Creator
    form_class = CreatorsForm
    template_name = 'creators/creator_form.html'
    success_url = '/creators/'
