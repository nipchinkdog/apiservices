#! get pictures
def TplTags(Tags):
    List = []
    if Tags:
        Tags = Tags.split(',')
        for tags in Tags:
            List.append({
                    'tags' : '#'+tags,
            })
        return List
