from .models import Course, Lesson, User, Comment
from django.views.generic import ListView, DetailView, CreateView
from .forms import CourseAddForm, CommentForm
from django.shortcuts import render, redirect


class HomePage(ListView):
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница сайта'
        return ctx


def tarrifsPage(request):
    return render(request, 'courses/tarrifs.html', {'title': 'Тарифы на сайте'})


class CourseDetailPage(DetailView):
    model = Course
    template_name = 'courses/course-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CourseDetailPage, self).get_context_data(**kwargs)
        ctx['title'] = Course.objects.filter(slug=self.kwargs['slug']).first()
        ctx['lessons'] = Lesson.objects.filter(course=ctx['title']).order_by('number')
        return ctx


class LessonDetailPage(DetailView):
    model = Course
    template_name = 'courses/lessons-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(LessonDetailPage, self).get_context_data(**kwargs)

        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = list(Lesson.objects.filter(course=course).filter(slug=self.kwargs['lesson_slug']).values())

        comments = Comment.objects.filter(lesson=Lesson[0]['id']).all()
        ctx['comments'] = comments
        ctx['commForm'] = CommentForm()

        ctx['title'] = lesson[0]['title']
        ctx['desc'] = lesson[0]['description']
        ctx['video'] = lesson[0]['video_url'].split("=")[1]
        return ctx

    def post(self, request, *args, **kwargs):
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = Lesson.objects.filter(course=course).filter(slug=self.kwargs['lesson_slug']).first()

        post = request.POST.copy()
        post['user'] = request.user
        post['lesson'] = lesson
        request.POST = post

        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()

        url = self.kwargs['slug'] + '/' + self.kwargs['lesson_slug']

        return redirect('/course/' + url)


class CourseAdd(CreateView):
    form_class = CourseAddForm
    template_name = 'courses/course_form.html'
