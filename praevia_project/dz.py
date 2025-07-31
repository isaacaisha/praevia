#Static Folder Name
folder_name = "fasto" 

dz_array = {
        "public":{
            "favicon":f"{folder_name}/images/favicon.png",
            "description":"Fasto - Django Saas Admin Dashboard Template",
            "og_title":"Fasto - Django Saas Admin Dashboard Template",
            "og_description":"Fasto - Django Saas Admin Dashboard Template",
            "og_image":"https://fasto.dexignzone.com/django/social-image.png",
            "title":"Fasto - Django Saas Admin Dashboard Template",
        },
        "global":{
            "css":[
                    f"{folder_name}/vendor/bootstrap-select/dist/css/bootstrap-select.min.css",
                    f"{folder_name}/css/style.css"
                ],

            "js":{
                "top":[
                    f"{folder_name}/vendor/global/global.min.js",
                    f"{folder_name}/vendor/bootstrap-select/dist/js/bootstrap-select.min.js",
                ],
                "bottom":[
                    f"{folder_name}/js/custom.min.js",
                    f"{folder_name}/js/deznav-init.js",
                ]
            },

        },
        "pagelevel":{
            "fasto":{#AppName
                "fasto_views":{
                    "css":{
                        "index": [
						    f"{folder_name}/vendor/chartist/css/chartist.min.css",
                        ],
                        "index_2": [
                            f"{folder_name}/vendor/chartist/css/chartist.min.css",
                        ],
                        "projects": [
                        ],
                        "contacts": [
                        ],
                        "kanban": [
                        ],
                        "calendar": [
                            f"{folder_name}/vendor/fullcalendar/css/main.min.css",
                        ],
                        "messages": [
                        ],
                        "app_profile": [
                            f"{folder_name}/vendor/lightgallery/css/lightgallery.min.css",
                        ],
                        "post_details": [
                            f"{folder_name}/vendor/lightgallery/css/lightgallery.min.css",
                        ],
                        "app_calender": [
                            f"{folder_name}/vendor/fullcalendar/css/main.min.css",
                        ],
                        "chart_chartist": [
                            f"{folder_name}/vendor/chartist/css/chartist.min.css",
                        ],
                        "chart_chartjs": [
                        ],
                        "chart_flot": [
                        ],
                        "chart_morris": [
                        ],
                        "chart_peity": [
                        ],
                        "chart_sparkline": [
                        ],
                        "ecom_checkout": [
                        ],
                        "ecom_customers": [
                        ],
                        "ecom_invoice": [
                        ],
                        "ecom_product_detail": [
                            f"{folder_name}/vendor/star-rating/star-rating-svg.css",
                            f"{folder_name}/vendor/owl-carousel/owl.carousel.css",
                        ],
                        "ecom_product_grid": [
                        ],
                        "ecom_product_list": [
                            f"{folder_name}/vendor/star-rating/star-rating-svg.css",
                        ],
                        "ecom_product_order": [
                        ],
                        "email_compose": [
                            f"{folder_name}/vendor/dropzone/dist/dropzone.css",
                        ],
                        "email_inbox": [
                        ],
                        "email_read": [
                        ],
                        "form_editor": [
                        ],
                        "form_element": [
                        ],
                        "form_pickers": [
                            f"{folder_name}/vendor/bootstrap-daterangepicker/daterangepicker.css",
                            f"{folder_name}/vendor/clockpicker/css/bootstrap-clockpicker.min.css",
                            f"{folder_name}/vendor/jquery-asColorPicker/css/asColorPicker.min.css",
                            f"{folder_name}/vendor/bootstrap-material-datetimepicker/css/bootstrap-material-datetimepicker.css",
                            f"{folder_name}/vendor/pickadate/themes/default.css",
                            f"{folder_name}/vendor/pickadate/themes/default.date.css",
                        ],
                        "form_validation": [
                        ],
                        "form_wizard": [
                            f"{folder_name}/vendor/jquery-smartwizard/dist/css/smart_wizard.min.css",
                        ],
                        "map_jqvmap": [
                            f"{folder_name}/vendor/jqvmap/css/jqvmap.min.css",
                        ],
                        "table_bootstrap_basic": [
                        ],
                        "table_datatable_basic": [
                            f"{folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                        ],
                        "uc_lightgallery": [
                            f"{folder_name}/vendor/lightgallery/css/lightgallery.min.css",
                        ],
                        "uc_nestable": [
                            f"{folder_name}/vendor/nestable2/css/jquery.nestable.min.css",
                        ],
                        "uc_noui_slider": [
                            f"{folder_name}/vendor/nouislider/nouislider.min.css",
                        ],
                        "uc_select2": [
                            f"{folder_name}/vendor/select2/css/select2.min.css",
                        ],
                        "uc_sweetalert": [
                            f"{folder_name}/vendor/sweetalert2/dist/sweetalert2.min.css",
                        ],
                        "uc_toastr": [
                            f"{folder_name}/vendor/toastr/css/toastr.min.css",
                        ],
                        "ui_accordion": [
                        ],
                        "ui_alert": [
                        ],
                        "ui_badge": [
                        ],
                        "ui_button": [
                        ],
                        "ui_button_group": [
                        ],
                        "ui_card": [
                        ],
                        "ui_carousel": [
                        ],
                        "ui_dropdown": [
                        ],
                        "ui_grid": [
                        ],
                        "ui_list_group": [
                        ],
                        "ui_media_object": [
                        ],
                        "ui_modal": [
                        ],
                        "ui_pagination": [
                        ],
                        "ui_popover": [
                        ],
                        "ui_progressbar": [
                        ],
                        "ui_tab": [
                        ],
                        "ui_typography": [
                        ],
                        "widget_basic": [
                            f"{folder_name}/vendor/chartist/css/chartist.min.css",
                        ],
                        "page_empty": [
                        ],
                    },
                    "js":{
                        "index": [
                            f"{folder_name}/vendor/chart.js/Chart.bundle.min.js",
                            f"{folder_name}/vendor/peity/jquery.peity.min.js",
                            f"{folder_name}/vendor/apexchart/apexchart.js",
                            f"{folder_name}/js/dashboard/dashboard-1.js",
                        ],
                        "index_2": [
                            f"{folder_name}/vendor/chart.js/Chart.bundle.min.js",
                            f"{folder_name}/vendor/peity/jquery.peity.min.js",
                            f"{folder_name}/vendor/apexchart/apexchart.js",
                            f"{folder_name}/js/dashboard/dashboard-1.js",
                        ],
                        "projects": [
                        ],
                        "contacts": [
                            f"{folder_name}/js/dashboard/contact.js",
                        ],
                        "kanban": [
                            f"{folder_name}/vendor/draggable/draggable.js",
                        ],
                        "calendar": [
                            f"{folder_name}/vendor/moment/moment.min.js",
                            f"{folder_name}/vendor/fullcalendar/js/main.min.js",
                            f"{folder_name}/js/dashboard/calendar.js",
                        ],
                        "messages": [
                        ],
                        "app_calender": [
                            f"{folder_name}/vendor/moment/moment.min.js",
                            f"{folder_name}/vendor/fullcalendar/js/main.min.js",
                        ],
                        "app_profile": [
                            f"{folder_name}/vendor/lightgallery/js/lightgallery-all.min.js",
                        ],
                        "post_details": [
                            f"{folder_name}/vendor/lightgallery/js/lightgallery-all.min.js",
                        ],
                        "chart_chartist": [
                            f"{folder_name}/vendor/chart.js/Chart.bundle.min.js",
                            f"{folder_name}/vendor/chartist/js/chartist.min.js",
                            f"{folder_name}/vendor/chartist-plugin-tooltips/js/chartist-plugin-tooltip.min.js",
                            f"{folder_name}/js/plugins-init/chartist-init.js",
                        ],
                        "chart_chartjs": [
                            f"{folder_name}/vendor/chart.js/Chart.bundle.min.js",
                            f"{folder_name}/js/plugins-init/chartjs-init.js",
                        ],
                        "chart_flot": [
                            f"{folder_name}/vendor/chart.js/Chart.bundle.min.js",
                            f"{folder_name}/vendor/flot/jquery.flot.js",
                            f"{folder_name}/vendor/flot/jquery.flot.pie.js",
                            f"{folder_name}/vendor/flot/jquery.flot.resize.js",
                            f"{folder_name}/vendor/flot-spline/jquery.flot.spline.min.js",
                            f"{folder_name}/js/plugins-init/flot-init.js",
                        ],
                        "chart_morris": [
                            f"{folder_name}/vendor/chart.js/Chart.bundle.min.js",
                            f"{folder_name}/vendor/raphael/raphael.min.js",
                            f"{folder_name}/vendor/morris/morris.min.js",
                            f"{folder_name}/js/plugins-init/morris-init.js",
                        ],
                        "chart_peity": [
                            f"{folder_name}/vendor/chart.js/Chart.bundle.min.js",
                            f"{folder_name}/vendor/peity/jquery.peity.min.js",
                            f"{folder_name}/js/plugins-init/piety-init.js",

                        ],
                        "chart_sparkline": [
                            f"{folder_name}/vendor/chart.js/Chart.bundle.min.js",
                            f"{folder_name}/vendor/jquery-sparkline/jquery.sparkline.min.js",
                            f"{folder_name}/js/plugins-init/sparkline-init.js",
                            f"{folder_name}/vendor/svganimation/vivus.min.js",
                            f"{folder_name}/vendor/svganimation/svg.animation.js",
                        ],
                        "ecom_checkout": [
                        ],
                        "ecom_customers": [
                            f"{folder_name}/vendor/highlightjs/highlight.pack.min.js",
                        ],
                        "ecom_invoice": [
                        ],
                        "ecom_product_detail": [
                            f"{folder_name}/vendor/owl-carousel/owl.carousel.js",
                            f"{folder_name}/vendor/star-rating/jquery.star-rating-svg.js",
                        ],
                        "ecom_product_grid": [
                        ],
                        "ecom_product_list": [
                            f"{folder_name}/vendor/star-rating/jquery.star-rating-svg.js",
                        ],
                        "ecom_product_order": [
                        ],
                        "email_compose": [
                            f"{folder_name}/vendor/dropzone/dist/dropzone.js",
                        ],
                        "email_inbox": [
                        ],
                        "email_read": [
                        ],
                        "form_editor": [
                            f"{folder_name}/vendor/ckeditor/ckeditor.js",
                        ],
                        "form_element": [
                        ],
                        "form_pickers": [
                            f"{folder_name}/vendor/moment/moment.min.js",
                            f"{folder_name}/vendor/bootstrap-daterangepicker/daterangepicker.js",
                            f"{folder_name}/vendor/clockpicker/js/bootstrap-clockpicker.min.js",
                            f"{folder_name}/vendor/jquery-asColor/jquery-asColor.min.js",
                            f"{folder_name}/vendor/jquery-asGradient/jquery-asGradient.min.js",
                            f"{folder_name}/vendor/jquery-asColorPicker/js/jquery-asColorPicker.min.js",
                            f"{folder_name}/vendor/bootstrap-material-datetimepicker/js/bootstrap-material-datetimepicker.js",
                            f"{folder_name}/vendor/pickadate/picker.js",
                            f"{folder_name}/vendor/pickadate/picker.time.js",
                            f"{folder_name}/vendor/pickadate/picker.date.js",
                            f"{folder_name}/js/plugins-init/bs-daterange-picker-init.js",
                            f"{folder_name}/js/plugins-init/clock-picker-init.js",
                            f"{folder_name}/js/plugins-init/jquery-asColorPicker.init.js",
                            f"{folder_name}/js/plugins-init/material-date-picker-init.js",
                            f"{folder_name}/js/plugins-init/pickadate-init.js",
                        ],
                        "form_validation": [
                            f"{folder_name}/vendor/jquery-validation/jquery.validate.min.js",
                            f"{folder_name}/js/plugins-init/jquery.validate-init.js",
                        ],
                        "form_wizard": [
                            f"{folder_name}/vendor/jquery-steps/build/jquery.steps.min.js",
                            f"{folder_name}/vendor/jquery-validation/jquery.validate.min.js",
                            f"{folder_name}/vendor/bootstrap-touchspin/js/jquery.bootstrap-touchspin.min.js",
                            f"{folder_name}/js/plugins-init/jquery.validate-init.js",
                            f"{folder_name}/vendor/jquery-smartwizard/dist/js/jquery.smartWizard.js",
                        ],
                        "map_jqvmap": [
                            f"{folder_name}/vendor/jqvmap/js/jquery.vmap.min.js",
                            f"{folder_name}/vendor/jqvmap/js/jquery.vmap.world.js",
                            f"{folder_name}/vendor/jqvmap/js/jquery.vmap.usa.js",
                            f"{folder_name}/js/plugins-init/jqvmap-init.js",
                        ],
                        "page_error_400": [
                        ],
                        "page_error_403": [
                        ],
                        "page_error_404": [
                        ],
                        "page_error_500": [
                        ],
                        "page_error_503": [
                        ],
                        "page_forgot_password": [
                        ],
                        "page_lock_screen": [
                        ],
                        "page_login": [
                        ],
                        "page_register": [
                        ],
                        "page_empty": [
                        ],
                        "table_bootstrap_basic": [
                        ],
                        "table_datatable_basic": [
                            f"{folder_name}/vendor/datatables/js/jquery.dataTables.min.js",
                            f"{folder_name}/js/plugins-init/datatables.init.js",
                        ],
                        "uc_lightgallery": [
                            f"{folder_name}/vendor/lightgallery/js/lightgallery-all.min.js",
                        ],
                        "uc_nestable": [
                            f"{folder_name}/vendor/nestable2/js/jquery.nestable.min.js",
                            f"{folder_name}/js/plugins-init/nestable-init.js",
                        ],
                        "uc_noui_slider": [
                            f"{folder_name}/vendor/nouislider/nouislider.min.js",
                            f"{folder_name}/vendor/wnumb/wNumb.js",
                            f"{folder_name}/js/plugins-init/nouislider-init.js",
                        ],
                        "uc_select2": [
                            f"{folder_name}/vendor/select2/js/select2.full.min.js",
                            f"{folder_name}/js/plugins-init/select2-init.js",
                        ],
                        "uc_sweetalert": [
                            f"{folder_name}/vendor/sweetalert2/dist/sweetalert2.min.js",
                            f"{folder_name}/js/plugins-init/sweetalert.init.js",
                        ],
                        "uc_toastr": [
                            f"{folder_name}/vendor/toastr/js/toastr.min.js",
                            f"{folder_name}/js/plugins-init/toastr-init.js",
                        ],
                        "ui_accordion": [
                        ],
                        "ui_alert": [
                        ],
                        "ui_badge": [
                        ],
                        "ui_button": [
                        ],
                        "ui_button_group": [
                        ],
                        "ui_media_object": [
                        ],
                        "ui_card": [
                        ],
                        "ui_carousel": [
                        ],
                        "ui_dropdown": [
                        ],
                        "ui_grid": [
                        ],
                        "ui_list_group": [
                        ],
                        "ui_modal": [
                        ],
                        "ui_pagination": [
                        ],
                        "ui_popover": [
                        ],
                        "ui_progressbar": [
                        ],
                        "ui_tab": [
                        ],
                        "typography": [
                        ],
                        "widget_basic": [
                            f"{folder_name}/vendor/chart.js/Chart.bundle.min.js",
                            f"{folder_name}/vendor/apexchart/apexchart.js",
                            f"{folder_name}/vendor/chartist/js/chartist.min.js",
                            f"{folder_name}/vendor/chartist-plugin-tooltips/js/chartist-plugin-tooltip.min.js",
                            f"{folder_name}/vendor/flot/jquery.flot.js",
                            f"{folder_name}/vendor/flot/jquery.flot.pie.js",
                            f"{folder_name}/vendor/flot/jquery.flot.resize.js",
                            f"{folder_name}/vendor/flot-spline/jquery.flot.spline.min.js",
                            f"{folder_name}/vendor/jquery-sparkline/jquery.sparkline.min.js",
                            f"{folder_name}/js/plugins-init/sparkline-init.js",
                            f"{folder_name}/vendor/peity/jquery.peity.min.js",
                            f"{folder_name}/js/plugins-init/piety-init.js",
                            f"{folder_name}/js/plugins-init/widgets-script-init.js",
                        ],


                    },
                }
            }
        }


}