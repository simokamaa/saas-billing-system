from django import forms
from . models import *

class clientForm(forms.ModelForm):
   #Metadata
   class Meta:
       model = Client
       fields = '__all__'
       
class router_hotspotForm(forms.ModelForm):
    class Meta:
        model = router_hotspot
        fields = '__all__'       

class routerForm(forms.ModelForm):
    class Meta:
        model = router
        fields = '__all__'
        
        

class packageForm(forms.ModelForm):
    #Metadata
    class Meta:
        model  = Packages
        fields = '__all__'
class payement_invoiceForm(forms.ModelForm):
    #Metadata
    class Meta:
        model = payment_invoice
        fields = '__all__'
class payment_gatewayForm(forms.ModelForm):
    #Metadata
    class Meta:
        model = payment_gateway
        fields = '__all__'
        
class sms_moduleForm(forms.ModelForm):
    class Meta:
        model = sms_module
        fields = '__all__'
        
class whatspp_moduleForm(forms.ModelForm):
    class Meta:
        model = whatspp_module
        fields = '__all__'
        
class email_moduleForm(forms.ModelForm):
    class Meta:
        model = email_module
        fields = '__all__'
        
class campaignForm(forms.ModelForm):
    class Meta:
        model = campaign
        fields = '__all__'
        
class contactsForm(forms.ModelForm):
    class Meta:
        model = contacts
        fields = '__all__'
        
class PackagesForm(forms.ModelForm):
    class Meta:
        model = Packages
        fields = '__all__'
        
class ProductItemForm(forms.ModelForm):
    class Meta:
        model = ProductItem
        fields = '__all__'
        
class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'
        
class  OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields ='__all__'
        
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        
class RefundForm(forms.ModelForm):
    class Meta:
        model = Refund
        fields = '__all__'
        
class productForm(forms.ModelForm):
    class Meta:
        model = product
        fields = '__all__'
        
        
class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = '__all__'
        
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        
        
class PackagesForm(forms.ModelForm):
    class Meta:
        model = Packages
        fields = '__all__'
        
        