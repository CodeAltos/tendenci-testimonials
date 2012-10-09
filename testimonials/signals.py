def init_signals():
    from django.db.models.signals import post_save
    from addons.testimonials.models import Testimonial
    from tendenci.apps.contributions.signals import save_contribution

    post_save.connect(save_contribution, sender=Testimonial, weak=False)