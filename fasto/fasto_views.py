from django.shortcuts import render

#COMMON = {'page_title_prefix': 'Fasto •'}

def index(request):
    context={
        #**COMMON,
        "page_title":"Dashboard"
    }
    return render(request,'fasto/index.html',context)


def index_2(request):
    context={
        "page_title":"Dashboard"
    }
    return render(request,'fasto/index-2.html',context)


def projects(request):
    context={
        "page_title":"Projects"
    }
    return render(request,'fasto/projects.html',context)


def contacts(request):
    context={
        "page_title":"Contacts"
    }
    return render(request,'fasto/contacts.html',context)


def kanban(request):
    context={
        "page_title":"Kanban"
    }
    return render(request,'fasto/kanban.html',context)


def calendar(request):
    context={
        "page_title":"Calendar"
    }
    return render(request,'fasto/calendar.html',context)


def messages(request):
    context={
        "page_title":"Messages"
    }
    return render(request,'fasto/messages.html',context)


def app_profile(request):
    context={
        "page_title":"App Profile"
    }
    return render(request,'fasto/apps/app-profile.html',context)


def post_details(request):
    context={
        "page_title":"Post Details"
    }
    return render(request,'fasto/apps/post-details.html',context)


def email_compose(request):
    context={
        "page_title":"Compose"
    }
    return render(request,'fasto/apps/email/email-compose.html',context)


def email_inbox(request):
    context={
        "page_title":"Inbox"
    }
    return render(request,'fasto/apps/email/email-inbox.html',context)


def email_read(request):
    context={
        "page_title":"Read"
    }
    return render(request,'fasto/apps/email/email-read.html',context)


def app_calender(request):
    context={
        "page_title":"Calendar"
    }
    return render(request,'fasto/apps/app-calender.html',context)


def ecom_product_grid(request):
    context={
        "page_title":"Product Grid"
    }
    return render(request,'fasto/apps/shop/ecom-product-grid.html',context)


def ecom_product_list(request):
    context={
        "page_title":"Product List"
    }
    return render(request,'fasto/apps/shop/ecom-product-list.html',context)


def ecom_product_detail(request):
    context={
        "page_title":"Product Detail"
    }
    return render(request,'fasto/apps/shop/ecom-product-detail.html',context)


def ecom_product_order(request):
    context={
        "page_title":"Product Order"
    }
    return render(request,'fasto/apps/shop/ecom-product-order.html',context)


def ecom_checkout(request):
    context={
        "page_title":"Checkout"
    }
    return render(request,'fasto/apps/shop/ecom-checkout.html',context)


def ecom_invoice(request):
    context={
        "page_title":"Invoice"
    }
    return render(request,'fasto/apps/shop/ecom-invoice.html',context)


def ecom_customers(request):
    context={
        "page_title":"Customers"
    }
    return render(request,'fasto/apps/shop/ecom-customers.html',context)



def chart_flot(request):
    context={
        "page_title":"Chart Flot"
    }
    return render(request,'fasto/charts/chart-flot.html',context)


def chart_morris(request):
    context={
        "page_title":"Chart Morris"
    }
    return render(request,'fasto/charts/chart-morris.html',context)


def chart_chartjs(request):
    context={
        "page_title":"Chart Chartjs"
    }
    return render(request,'fasto/charts/chart-chartjs.html',context)


def chart_chartist(request):
    context={
        "page_title":"Chart Chartist"
    }
    return render(request,'fasto/charts/chart-chartist.html',context)


def chart_sparkline(request):
    context={
        "page_title":"Chart Sparkline"
    }
    return render(request,'fasto/charts/chart-sparkline.html',context)


def chart_peity(request):
    context={
        "page_title":"Chart Peity"
    }
    return render(request,'fasto/charts/chart-peity.html',context)



def ui_accordion(request):
    context={
        "page_title":"Accordion"
    }
    return render(request,'fasto/bootstrap/ui-accordion.html',context)


def ui_alert(request):
    context={
        "page_title":"Alert"
    }
    return render(request,'fasto/bootstrap/ui-alert.html',context)


def ui_badge(request):
    context={
        "page_title":"Badge"
    }
    return render(request,'fasto/bootstrap/ui-badge.html',context)


def ui_button(request):
    context={
        "page_title":"Button"
    }
    return render(request,'fasto/bootstrap/ui-button.html',context)


def ui_modal(request):
    context={
        "page_title":"Modal"
    }
    return render(request,'fasto/bootstrap/ui-modal.html',context)


def ui_button_group(request):
    context={
        "page_title":"Button Group"
    }
    return render(request,'fasto/bootstrap/ui-button-group.html',context)


def ui_media_object(request):
    context={
        "page_title":"Media Object"
    }
    return render(request,'fasto/bootstrap/ui-media-object.html',context)


def ui_list_group(request):
    context={
        "page_title":"List Group"
    }
    return render(request,'fasto/bootstrap/ui-list-group.html',context)


def ui_card(request):
    context={
        "page_title":"Card"
    }
    return render(request,'fasto/bootstrap/ui-card.html',context)


def ui_carousel(request):
    context={
        "page_title":"Carousel"
    }
    return render(request,'fasto/bootstrap/ui-carousel.html',context)


def ui_dropdown(request):
    context={
        "page_title":"Dropdown"
    }
    return render(request,'fasto/bootstrap/ui-dropdown.html',context)


def ui_popover(request):
    context={
        "page_title":"Popover"
    }
    return render(request,'fasto/bootstrap/ui-popover.html',context)


def ui_progressbar(request):
    context={
        "page_title":"Progressbar"
    }
    return render(request,'fasto/bootstrap/ui-progressbar.html',context)


def ui_tab(request):
    context={
        "page_title":"Tab"
    }
    return render(request,'fasto/bootstrap/ui-tab.html',context)


def ui_typography(request):
    context={
        "page_title":"Typography"
    }
    return render(request,'fasto/bootstrap/ui-typography.html',context)


def ui_pagination(request):
    context={
        "page_title":"Pagination"
    }
    return render(request,'fasto/bootstrap/ui-pagination.html',context)


def ui_grid(request):
    context={
        "page_title":"Grid"
    }
    return render(request,'fasto/bootstrap/ui-grid.html',context)




def uc_select2(request):
    context={
        "page_title":"Select"
    }
    return render(request,'fasto/plugins/uc-select2.html',context)


def uc_nestable(request):
    context={
        "page_title":"Nestable"
    }
    return render(request,'fasto/plugins/uc-nestable.html',context)


def uc_noui_slider(request):
    context={
        "page_title":"UI Slider"
    }
    return render(request,'fasto/plugins/uc-noui-slider.html',context)


def uc_sweetalert(request):
    context={
        "page_title":"Sweet Alert"
    }
    return render(request,'fasto/plugins/uc-sweetalert.html',context)


def uc_toastr(request):
    context={
        "page_title":"Toastr"
    }
    return render(request,'fasto/plugins/uc-toastr.html',context)


def map_jqvmap(request):
    context={
        "page_title":"Jqvmap"
    }
    return render(request,'fasto/plugins/map-jqvmap.html',context)


def uc_lightgallery(request):
    context={
        "page_title":"LightGallery"
    }
    return render(request,'fasto/plugins/uc-lightgallery.html',context)


def widget_basic(request):
    context={
        "page_title":"Widget"
    }
    return render(request,'fasto/widget-basic.html',context)


def form_element(request):
    context={
        "page_title":"Form Element"
    }
    return render(request,'fasto/forms/form-element.html',context)


def form_wizard(request):
    context={
        "page_title":"Form Wizard"
    }
    return render(request,'fasto/forms/form-wizard.html',context)


def form_editor(request):
    context={
        "page_title":"CkEditor"
    }
    return render(request,'fasto/forms/form-editor.html',context)


def form_pickers(request):
    context={
        "page_title":"Pickers"
    }
    return render(request,'fasto/forms/form-pickers.html',context)


def form_validation(request):
    context={
        "page_title":"Form Validation"
    }
    return render(request,'fasto/forms/form-validation.html',context)


def table_bootstrap_basic(request):
    context={
        "page_title":"Table Bootstrap"
    }
    return render(request,'fasto/table/table-bootstrap-basic.html',context)


def table_datatable_basic(request):
    context={
        "page_title":"Table Datatable"
    }
    return render(request,'fasto/table/table-datatable-basic.html',context)






def page_register(request):
    return render(request,'fasto/pages/page-register.html')

def page_login(request):
    return render(request,'fasto/pages/page-login.html')

def page_forgot_password(request):
    return render(request,'fasto/pages/page-forgot-password.html')

def page_lock_screen(request):
    return render(request,'fasto/pages/page-lock-screen.html')

def page_empty(request):
    return render(request,'fasto/pages/page-empty.html')

def page_error_400(request):
    return render(request,'400.html')
    
def page_error_403(request):
    return render(request,'403.html')

def page_error_404(request):
    return render(request,'404.html')

def page_error_500(request):
    return render(request,'500.html')

def page_error_503(request):
    return render(request,'503.html')
    













