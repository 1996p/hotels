from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def show_hotel_rating(rating):
    if rating <= 1:
        result = f"""
            <div class="hotel-rate">
                <img src="/static/lagoona/images/Vector.svg" alt="Рейтинг отеля {rating} из 5" class="hotel-rate-star">
                <img src="/static/lagoona/images/empty_star.svg" alt="" class="hotel-rate-star">
                <img src="/static/lagoona/images/empty_star.svg" alt="" class="hotel-rate-star">
                <img src="/static/lagoona/images/empty_star.svg" alt="" class="hotel-rate-star">
                <img src="/static/lagoona/images/empty_star.svg" alt="" class="hotel-rate-star">
             </div>
        """
    elif rating == 2:
        result = f"""
            <div class="hotel-rate">
                <img src="/static/lagoona/images/Vector.svg" alt="Рейтинг отеля {rating} из 5" class="hotel-rate-star">
                <img src="/static/lagoona/images/Vector.svg" alt="" class="hotel-rate-star">
                <img src="/static/lagoona/images/empty_star.svg" alt="" class="hotel-rate-star">
                <img src="/static/lagoona/images/empty_star.svg" alt="" class="hotel-rate-star">
                <img src="/static/lagoona/images/empty_star.svg" alt="" class="hotel-rate-star">
             </div>
        """
    elif rating == 3:
        result = f"""
            <div class="hotel-rate">
                <img src="/static/lagoona/images/Vector.svg" alt="Рейтинг отеля {rating} из 5" class="hotel-rate-star">
                <img src="/static/lagoona/images/Vector.svg" alt="" class="hotel-rate-star">
                <img src="/static/lagoona/images/Vector.svg" alt="" class="hotel-rate-star">
                <img src="/static/lagoona/images/empty_star.svg" alt="" class="hotel-rate-star">
                <img src="/static/lagoona/images/empty_star.svg" alt="" class="hotel-rate-star">
             </div>
        """
    elif rating == 4:
        result = f"""
            <div class="hotel-rate">
                <img src="/static/lagoona/images/Vector.svg" alt="Рейтинг отеля {rating} из 5" class="hotel-rate-star">
                <img src="/static/lagoona/images/Vector.svg" alt="" class="hotel-rate-star">
                <img src="/static/lagoona/images/Vector.svg" alt="" class="hotel-rate-star">
                <img src="/static/lagoona/images/Vector.svg" alt="" class="hotel-rate-star">
                <img src="/static/lagoona/images/empty_star.svg" alt="" class="hotel-rate-star">
             </div>
        """
    elif rating >= 5:
        result = f"""
            <div class="hotel-rate">
                <img src="/static/lagoona/images/Vector.svg" alt="Рейтинг отеля {rating} из 5" class="hotel-rate-star">
                <img src="/static/lagoona/images/Vector.svg" alt="" class="hotel-rate-star">
                <img src="/static/lagoona/images/Vector.svg" alt="" class="hotel-rate-star">
                <img src="/static/lagoona/images/Vector.svg" alt="" class="hotel-rate-star">
                <img src="/static/lagoona/images/Vector.svg" alt="" class="hotel-rate-star">
             </div>
        """
    return mark_safe(result)