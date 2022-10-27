from django.shortcuts import render

class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary_list.html'
    paginate_by = 2

    def get_queryset(selfself):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries
