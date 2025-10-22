import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04151, 0.0).lineTo(0.04317, 0.0).lineTo(0.04317, 0.01702).lineTo(0.02366, 0.01702).lineTo(0.01598, 0.03279).lineTo(-0.04172, 0.03279).lineTo(-0.04151, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.19281432751516037)
