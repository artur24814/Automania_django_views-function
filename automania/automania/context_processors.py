from .models import ReadedMesseges

def navbar_view_unread_messege(request):
    unread_message = ReadedMesseges.objects.filter(owner=request.user.username).filter(read=False)
    return {'quantity_messege': len(unread_message)}
