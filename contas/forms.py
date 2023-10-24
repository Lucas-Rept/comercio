from django import forms
from .models import Cliente, Item

class ClienteForm(forms.ModelForm):
    name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'Nome do Cliente *', 'class':'name-input', 'id':'name-input'}))
    telefone = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'(00) 00000-0000', 'class':'telefone-input', 'type':'tel', 'onkeyup':'handlePhone(event)', 'maxlength':15}))
    class Meta:
        model = Cliente
        fields = '__all__'
        
class ItemForm(forms.ModelForm):
    unitChoices = (('und', 'und'), ('m', 'm'), ('L', 'L'), ('kg','kg'))
    
    name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'Digite o nome do item'}))
    quantity = forms.FloatField(label="Quantidade", widget=forms.NumberInput(attrs={'placeholder':'1.5, 2, 2.5, 3, etc', 'step':'0.01', 'min':'0', 'onpaste':'return false', "class":"placeholderLeft"}))
    price = forms.FloatField(label="Unitário R$", widget=forms.NumberInput(attrs={'placeholder':'1,00', 'step':'0.01', 'min':'0', 'onpaste':'return false', 'class':'placeholderLeft'}))
    unit = forms.ChoiceField(label="Unidade", choices = unitChoices, widget=forms.Select(attrs={'class':'placeholderLeft'}))

    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['cliente']
