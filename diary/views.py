import logging

from django.urls import reverse_lazy

from django.views import generic

from .forms import InquiryForm

from django.contrib import messages

logger = logging.getLogger(__name__)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Diary

from.forms import InquiryForm, DiaryCreateForm

from django.shortcuts import get_object_or_404

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True
    def test_func(self):
        #URLに埋め込まれた主キーから日記データ一件を取得できない場合は404エラー
        diary = get_object_or_404(Diary, pk=self.kwargs['pk'])
        #ログインユーザと日記の作成ユーザを比較、異なればraise_exception設定に従う
        return self.request.user == diary.user


class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary_list.html'

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries

class DiaryDetailView(LoginRequiredMixin, OnlyYouMixin, generic.DetailView):
    class DiaryCreateView(LoginRequiredMixin, generic.CreateView):
        model = Diary
        template_name ='diary_create.html'
        form_class = DiaryCreateForm
        success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        messagess.success(self.request, '日記を作成しました。')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"日記作成に失敗しました。")
        return super().form_invalid(form)

class DiaryUpdateView(LoginRequiredMixin, OnlyYouMixin, generic.UpdateView):
    class DiaryUpdateView(LoginRequiredMixin, generic.UpdateView):
        model = Diary
        template_name ='diary_update.html'
        form_class = DiaryCreateForm

        def get_success_url(self):
            return reverse_lazy('diary:diary_detail', kwargs={'pk': self.kwargs['pk']})

        def from_vaild(self, form):
            messages.success(self.request, '日記を更新しました。')
            return super().form_valid(form)

        def from_invaild(self, form):
            messages.error(self.request, '日記の更新に失敗しました。')
            return super().form_invalid(form)

class DiaryDeleteView(LoginRequiredMixin, OnlyYouMixin, generic.DeleteView):
    class DiaryDeleteView(LoginRequiredMixin, generic.DeleteView):
        model = Diary
        template_name = 'diary_delete.html'
        success_url = reverse_lazy('diary:diary_list')
        def delete(self, request, *args, **kwargs):
            messages.success(self.request, "日記を削除しました。")
            return super().delete(request, *args, **kwargs)
