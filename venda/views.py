

class HomeView():
    # model = Letter
    template_name = "home.html"
    ordering = ["-letter_date"]
    paginate_by = 9
