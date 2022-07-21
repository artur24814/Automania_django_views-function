from .models import ReadedMesseges

def navbar_view_unread_messege(request):
    """
    context processor to check unread message and show it to user wherever user is in website,
    """
    unread_message = ReadedMesseges.objects.filter(owner=request.user.username).filter(read=False)
    return {'quantity_messege': len(unread_message)}
