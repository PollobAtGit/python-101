def findPoint(px, py, qx, qy):
    if px is not None and py is not None and qx is not None and qy is not None:
        return [qx + (qx - px), qy + (qy - py)]
