from django.urls import path 
from . import views, client_views,product_views,refund_views,coupon_views,Address_views
from . import Payment_views, Payment_invoice_views,package_views,order_item_views,profile_views
from . import order_views,payment_gateway_views,whatspp_module_views,sms_module_views
from . import email_module_views,contact_views, campaign_views, BalanceSheet_views

urlpatterns = [
    # global system url routes
    path('', views.index, name="index"),
    path('balanceSheet/', BalanceSheet_views.BalanceSheet, name='balanceSheet'),
    path('dailyReports/', views.dailyReports, name='dailyReports'),
    path('monthlyReports/', views.monthlyReports, name='monthlyReports'),
    path('yearlyReports/', views.yearlyReports, name='yearlyReports'),
    path('settings/', views.settings, name='settings'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    # urls routes for client create read update and delete
    path('client/', client_views.client_create, name='client_create'),
    path('client/<int:pk>/', client_views.client_detail, name='client_detail'),
    path('client/<int:pk>/', client_views.client_update, name='client_update'),
    path('client/<int:pk>/', client_views.client_delete, name='client_delete'),
    path('clients/', client_views.clients_detail, name='clients_detail'),
    path('clients_delete/', client_views.clients_delete, name='clients_delete'),
    
    # url routes for products
    path('product/', product_views.product_create, name='product_create'),
    path('product/<int:pk>/', product_views.product_detail, name='product_detail'),
    path('product/<int:pk>/', product_views.product_update, name='product_update'),
    path('product<int:pk>/', product_views.product_delete, name='product_delete'),
    path('products/', product_views.products_detail, name='products_detail'),
    path('products_delete/', product_views.products_delete, name='products_delete'),
    
    # url routes for refunds
    path('refund/', refund_views.Refund_create, name='Refund_create'),
    path('refund/<int:pk>/', refund_views.Refund_detail, name='Refund_detail'),
    path('refund/int:pk>/', refund_views.Refund_update, name='Refund_update'),
    path('refund/<int:pk>/', refund_views.Refund_delete, name='Refund_delete'),
    path('refunds/', refund_views.Refunds_detail, name='Refunds_detail'),
    path('Refunds_delete/', refund_views.Refunds_delete, name='Refunds_delete'),
    
    # url routes for coupons
    path('coupon/', coupon_views.coupon_create, name='coupon_create'),
    path('coupon/<int:pk>/', coupon_views.coupon_detail, name='coupon_detail'),
    path('coupon/<int:pk>/', coupon_views.coupon_update, name='coupon_update'),
    path('coupon/<int:pk>/', coupon_views.coupon_delete, name='coupon_delete'),
    path('coupons/', coupon_views.coupons_detail, name='coupons_detail'),
    path('coupons_delete/', coupon_views.coupons_delete, name='coupons_delete'),
    
    # url routes for address
    path('address/', Address_views.Address_create, name='Address_create'),
    path('address/<int:pk>/', Address_views.Address_detail, name='Address_detail'),
    path('address/<int:pk>/', Address_views.Address_update, name='Address_update'),
    path('address/<int:pk>/', Address_views.Address_delete, name='Address_delete'),
    path('addresss/', Address_views.Address_details, name='Address_details'),
    path('Addresss_delete/', Address_views.Addresss_delete, name='Addresss_delete'),
    
   # url routes for payment
    path('payment/', Payment_views.Payment_create, name='Payment_create'),
    path('payment/<int:pk>/', Payment_views.Payment_detail, name='Payment_detail'),
    path('payment/<int:pk>/', Payment_views.Payment_update, name='Payment_update'),
    path('payment/<int:pk>/', Payment_views.Payment_delete, name='Payment_delete'),
    path('payments/', Payment_views.Payments_detail, name='Payments_detail'),
    path('Payment_delete/', Payment_views.Payment_delete, name='Payments_delete'),
    
    # url routes for Payment invoice
    path('payment_invoice/', Payment_invoice_views.payment_invoice_create, name='payment_invoice_create'),
    path('payment_invoice/<int:pk>/', Payment_invoice_views.payment_invoice_detail, name='payment_invoice_detail'),
    path('payment_invoice/<int:pk>/', Payment_invoice_views.payment_invoice_update, name='payment_invoice_update'),
    path('payment_invoice/<int:pk>/', Payment_invoice_views.payment_invoice_delete, name='payment_invoice_delete'),
    path('payment_invoices/', Payment_invoice_views.payment_invoices_detail, name='payment_invoices_detail'),
    path('payment_invoice_delete/', Payment_invoice_views.payment_invoice_delete, name='payment_invoices_delete'),
    
    # url for packages
    path('package/', package_views.package_create, name='package_create'),
    path('package/<int:pk>/', package_views.package_detail, name='package_detail'),
    path('package/<int:pk>/', package_views.package_update, name='package_update'),
    path('package/<int:pk>/', package_views.package_delete, name='package_delete'),
    path('packages/', package_views.packages_detail, name='packages_detail'),
    path('packages_delete/', package_views.packages_delete, name='packages_delete'),
    
   # urls for order items
    path('order_item/', order_item_views.order_item_create, name='order_item_create'),
    path('order_item/<int:pk>/', order_item_views.order_item_detail, name='order_item_detail'),
    path('order_item/<int:pk>/', order_item_views.order_item_update, name='order_item_update'),
    path('order_item/<int:pk>/', order_item_views.order_item_delete, name='order_item_delete'),
    path('order_items/', order_item_views.order_items_detail, name='order_items_detail'),
    path('order_items_delete/', order_item_views.order_items_delete, name='order_items_delete'),
    
   # urls for orders
    path('order/', order_views.order_create, name='order_create'),
    path('order/<int:pk>/', order_views.order_detail, name='order_detail'),
    path('order/<int:pk>/', order_views.order_update, name='order_update'),
    path('order/<int:pk>/', order_views.order_delete, name='order_delete'),
    path('orders/', order_views.orders_detail, name='orders_detail'),
    path('orders_delete/', order_views.orders_delete, name='orders_delete'),
    
    # urls for payment gateways configuration
    path('payment_gateway/', payment_gateway_views.payment_gateway_create, name='payment_gateway_create'),
    path('payment_gateway/<int:pk>/', payment_gateway_views.payment_gateway_detail, name='payment_gateway_detail'),
    path('payment_gateway/<int:pk>/', payment_gateway_views.payment_gateway_update, name='payment_gateway_update'),
    path('payment_gateway/<int:pk>/', payment_gateway_views.payment_gateway_delete, name='payment_gateway_delete'),
    path('payment_gateways/', payment_gateway_views.payment_gateways_detail, name='payment_gateways_detail'),
    path('payment_gateways_delete/', payment_gateway_views.payment_gateways_delete, name='payment_gateways_delete'),
    
    # urls for whatspp module configuration
    path('whatspp_module/', whatspp_module_views.whatspp_module_create, name='whatspp_module_create'),
    path('whatspp_module/<int:pk>/', whatspp_module_views.whatspp_module_detail, name='whatspp_module_detail'),
    path('whatspp_module/<int:pk>/', whatspp_module_views.whatspp_module_update, name='whatspp_module_update'),
    path('whatspp_module/<int:pk>/', whatspp_module_views.whatspp_module_delete, name='whatspp_module_delete'),
    path('whatspp_modules/', whatspp_module_views.whatspp_modules_detail, name='whatspp_modules_detail'),
    path('whatspp_modules_delete/', whatspp_module_views.whatspp_modules_delete, name='whatspp_modules_delete'),
    
    # urls for sms module configuration
    path('sms_module/', sms_module_views.sms_module_create, name='sms_module_create'),
    path('sms_module/<int:pk>/', sms_module_views.sms_module_detail, name='sms_module_detail'),
    path('sms_module/<int:pk>/', sms_module_views.sms_module_update, name='sms_module_update'),
    path('sms_module/<int:pk>/', sms_module_views.sms_module_delete, name='sms_module_delete'),
    path('sms_modules/', sms_module_views.sms_modules_detail, name='sms_modules_detail'),
    path('sms_modules_delete/', sms_module_views.sms_modules_delete, name='sms_modules_delete'),
    
    # urls for email module configuration
    path('email_module/', email_module_views.email_module_create, name='email_module_create'),
    path('email_module/<int:pk>/', email_module_views.email_module_detail, name='email_module_detail'),
    path('email_module/<int:pk>/', email_module_views.email_module_update, name='email_module_update'),
    path('email_module/<int:pk>/', email_module_views.email_module_delete, name='email_module_delete'),
    path('email_modules/', email_module_views.email_modules_detail, name='email_modules_detail'),
    path('email_modules_delete/', email_module_views.email_modules_delete, name='email_modules_delete'),
    
    # urls for campaign configuration
    path('campaign/', campaign_views.campaign_create, name='campaign_create'),
    path('campaign/<int:pk>/', campaign_views.campaign_detail, name='campaign_detail'),
    path('campaign/<int:pk>/', campaign_views.campaign_update, name='campaign_update'),
    path('campaign/<int:pk>/', campaign_views.campaign_delete, name='campaign_delete'),
    path('campaigns/', campaign_views.campaigns_detail, name='campaigns_detail'),
    path('campaigns_delete/', campaign_views.campaigns_delete, name='campaigns_delete'),
    
   # urls for contact configuration
    path('contact/', contact_views.contact_create, name='contact_create'),
    path('contact/<int:pk>/', contact_views.contact_detail, name='contact_detail'),
    path('contact/<int:pk>/', contact_views.contact_update, name='contact_update'),
    path('contact/<int:pk>/', contact_views.contact_delete, name='contact_delete'),
    path('contacts/', contact_views.contacts_detail, name='contacts_detail'),
    path('contacts_delete/', contact_views.contacts_delete, name='contacts_delete'),
    
]