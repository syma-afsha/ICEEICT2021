from django.shortcuts import render
from pages.views import nav_items, footer, conf_logo, styles, all_speakers

# Create your views here.


def speakers(request):
    context = {
        "styles": styles(),
        "nav_items": nav_items(),
        "footer": footer(),
        "conf_logo": conf_logo(),
    }
    return render(request, "keynotespeaker.html", context)


def speaker(request, key):

    if key in all_speakers().keys():
        context = all_speakers()[key]
        context["id"] = key
        context["nav_items"] = nav_items()
        context["footer"] = footer()
        context["conf_logo"] = conf_logo()
        context["styles"] = styles()

        return render(request, "keynotespeaker1.html", context)
    else:
        context = {
            "styles": styles(),
            "nav_items": nav_items(),
            "footer": footer(),
            "conf_logo": conf_logo(),
        }
        return render(request, "does_not_exist.html", context)
