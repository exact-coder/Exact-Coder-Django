from django import forms
from ckeditor.widgets import CKEditorWidget
from article.models import Article,ArticleCategory,Tags

class WriteArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['article_main_title','article_sub_title','article_banner_img','article_description','categories','tags']
        # labels ={'article_main_title':'Article Main Title *','article_sub_title':'Article Sub-Title','article_banner_img':'Article Banner Image *','article_description':'Article Description *','categories': 'Select Categories  ','tags': 'Select Tags  '}
        widgets = {
            'article_main_title': forms.TextInput(attrs={'class':'form-control m-3 text-light placeholder-glow','placeholder':'Article Title'}),
            'article_sub_title': forms.TextInput(attrs={'class':'form-control m-3 text-light','placeholder':'Article Sub-Title'}),
            'article_banner_img': forms.FileInput(attrs={'class':'form-control m-3 text-light'}),
            'article_description': forms.TextInput(attrs={'class':'form-control m-3 text-light','id':'content','placeholder':'Describe your Articles'}),
            # 'categories': forms.TextInput(attrs={'class':'form-control'}),
            # 'tags':  forms.ChoiceWidget(attrs={'class':'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categories'].widget.attrs.update({
            'class': 'form-control m-3 text-light',
        })
        self.fields['tags'].widget.attrs.update({
            'class': 'form-control m-3 text-light',
        })
        self.fields['categories'].queryset = ArticleCategory.objects.all()
        
        self.fields['tags'].queryset = Tags.objects.all()
    