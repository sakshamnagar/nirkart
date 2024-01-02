from django.forms import ModelForm
from myapp.models import Item,SubCategory
from django import forms

class CreateItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class': 'form-control m-1 font','required': 'required'}
        self.fields['category'].widget.attrs = {'class': 'form-control m-1 font','required': 'required'}
        self.fields['sub_category'].widget.attrs = {'class': 'form-control m-1 font','required': 'required'}
        self.fields['manufacturing_brand'].widget.attrs = {'class': 'form-control m-1 font','required': 'required'}
        self.fields['model_name'].widget.attrs = {'class': 'form-control m-1 font','required': 'required'}
        self.fields['color'].widget.attrs = {'class': 'form-control m-1 font','required': 'required'}
        self.fields['quantity'].widget.attrs = {'class': 'form-control m-1 font','required': 'required'}
        self.fields['price'].widget.attrs = {'class': 'form-control m-1 font','required': 'required'}
        self.fields['tags'].widget.attrs = {'class': 'form-control m-1 font','required': 'required'}
        self.fields['description'].widget.attrs = {'class': 'form-control m-1 font','rows':'5','required': 'required'}
        self.fields['image'].widget.attrs = {'class': 'form-control m-1 text-muted font','required': 'required'}
        self.fields['sub_category'].queryset = SubCategory.objects.none()
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['sub_category'].queryset = SubCategory.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['sub_category'].queryset = self.instance.category.subcategory.order_by('name')

    class Meta:
        model = Item
        fields = ('name','category','sub_category','manufacturing_brand','model_name','color','quantity','price','tags','description','image')


class UpdateItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class': 'form-control m-1','required': 'required'}
        self.fields['category'].widget.attrs = {'class': 'form-control m-1','required': 'required'}
        self.fields['sub_category'].widget.attrs = {'class': 'form-control m-1','required': 'required'}
        self.fields['manufacturing_brand'].widget.attrs = {'class': 'form-control m-1','required': 'required'}
        self.fields['model_name'].widget.attrs = {'class': 'form-control m-1','required': 'required'}
        self.fields['color'].widget.attrs = {'class': 'form-control m-1','required': 'required'}
        self.fields['quantity'].widget.attrs = {'class': 'form-control m-1','required': 'required'}
        self.fields['price'].widget.attrs = {'class': 'form-control m-1','required': 'required'}
        self.fields['tags'].widget.attrs = {'class': 'form-control m-1','required': 'required'}
        self.fields['description'].widget.attrs = {'class': 'form-control m-1','rows':'5','required': 'required'}
        self.fields['image'].widget.attrs = {'class': 'form-control m-4','required': 'required'}
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['sub_category'].queryset = SubCategory.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['sub_category'].queryset = self.instance.category.subcategory.order_by('name')
                #set up related name for sub caegory as 'subcategory'. Thats why used category.subcategory.order_by instead of category.sub_cattegory_set.order_by
    class Meta:
        model = Item
        fields = ('name','category','sub_category','manufacturing_brand','model_name','color','quantity','price','tags','description','image')

        

    