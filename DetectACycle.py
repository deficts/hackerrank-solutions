def has_cycle(head):
    hare=head.next
    tortoise=head
    while(hare!=tortoise):
        if(hare==None or tortoise==None):
            return False
        hare.next
        tortoise.next.next
    return True
