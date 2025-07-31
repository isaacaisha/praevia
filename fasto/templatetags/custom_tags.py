from django import template
from django.urls import resolve
from django.urls.exceptions import Resolver404
from loguru import logger


register = template.Library()

#This the custom filter, name is getitems
def getdata(json_data, args):    
    func_name=''
    try:
        myfunc, myargs, mykwargs = resolve(args)
        if myfunc:
            logger.success("*"*50)
            print()
            logger.debug("Function Name:> {} ",myfunc.__name__,feature="f-strings")
            logger.debug("Module Name:> {} ",myfunc.__module__,feature="f-strings")
            logger.debug("URL_Path:> {} ",args,feature="f-strings")
            func_name=myfunc.__name__
            print()
            logger.success("*"*50)
    except Resolver404:
        logger.debug("something went wrong",feature="f-strings")
        pass

    return json_data.get(func_name)
    #"""
    #Given dz_array.pagelevel.fasto.fasto_views, pick out the list for the view handling `path`.
    #"""
    #if not json_data:
    #    logger.warning("getdata: dz_array missing or empty")
    #    return []

    #try:
    #    view_func, _, _ = resolve(path)
    #    key = view_func.__name__
    #except Resolver404:
    #    logger.debug(f"getdata: can't resolve {path}")
    #    return []

    #data = json_data.get(key)
    #if data is None:
    #    logger.warning(f"getdata: no assets configured for view {key}")
    #    return []

    #return data


register.filter('getdata', getdata)



# request.path	                  /home/
# request.get_full_path	         /home/?q=test
# request.build_absolute_uri	 http://127.0.0.1:8000/home/?q=test