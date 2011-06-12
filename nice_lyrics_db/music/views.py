from flameforged.view_helpers import render_to

@render_to('music/home.html')
def home(request):
    return locals()
