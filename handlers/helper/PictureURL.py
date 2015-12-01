def getPictureURL(picture):
    if picture == 'None':
        picture_url = '/images/avatar-template.png'
    else:
        picture_url = '/view_photo/' + picture
    return picture_url
