from django import forms

class CriptografiaForm(forms.Form):
    mensagem = forms.CharField(
        label='Mensagem',
        max_length=1000,
        widget=forms.TextInput(attrs={'placeholder': 'Digite sua mensagem aqui'})
    )
    chave = forms.CharField(
        label='Chave',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Digite a chave aqui'})
    )
    acao = forms.ChoiceField(
        label='Ação',
        choices=[('criptografar', 'Criptografar'), ('descriptografar', 'Descriptografar')],
        widget=forms.Select()
    )
