from avatar.models import Avatar

def profile_pic(request):
    if request.user.is_authenticated:
        try:
           profile_obj = Avatar.objects.get(user = request.user)
           pic = profile_obj.imagen
           return {"picture":pic}
        except Avatar.DoesNotExist:
            pass
    return {}