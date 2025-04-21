elif level == "bottom":
    # The single midPlat directly above ground
    if hero_x < midPlat.left:
        hero_x = midPlat.left
    elif hero_x > midPlat.right - rect_width:
        hero_x = midPlat.right - rect_width

elif level == "lower":
    # Two side‑by‑side lower platforms
    if hero_x < lowerLeftPlat.left:
        hero_x = lowerLeftPlat.left
    elif lowerLeftPlat.right - rect_width < hero_x < lowerRightPlat.left:
        # in the gap—snap to nearest edge
        if (hero_x - (lowerLeftPlat.right - rect_width)
            < (lowerRightPlat.left - hero_x)):
            hero_x = lowerLeftPlat.right - rect_width
        else:
            hero_x = lowerRightPlat.left
    elif hero_x > lowerRightPlat.right - rect_width:
        hero_x = lowerRightPlat.right - rect_width

elif level == "mid":
    # The single topmidPlat above them
    if hero_x < topmidPlat.left:
        hero_x = topmidPlat.left
    elif hero_x > topmidPlat.right - rect_width:
        hero_x = topmidPlat.right - rect_width

elif level == "top":
    # Two platforms up top left/right
    if hero_x < topleftPlat.left:
        hero_x = topleftPlat.left
    elif topleftPlat.right - rect_width < hero_x < toprightPlat.left:
        if (hero_x - (topleftPlat.right - rect_width)
            < (toprightPlat.left - hero_x)):
            hero_x = topleftPlat.right - rect_width
        else:
            hero_x = toprightPlat.left
    elif hero_x > toprightPlat.right - rect_width:
        hero_x = toprightPlat.right - rect_width
