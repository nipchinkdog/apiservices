#! get comments
def TplComments(Comments):
    List = []
    for comment in Comments:
        #! arrange list posts
        List.append({
                'id' : comment.id,
                'account' : comment.accounts.username,
                'note' : comment.note,
                'date' : comment.date.strftime('%A, %b %d'),
                'datetime' : comment.datetime.strftime('%A, %b %d')
        })
    return List
