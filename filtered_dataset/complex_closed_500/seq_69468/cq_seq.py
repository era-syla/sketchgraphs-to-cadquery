import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.04506, 0.06).lineTo(0.01811, 0.09).lineTo(-0.01494, 0.06).lineTo(0.04506, 0.06).close()
solid=wp_sketch0.add(loop0).extrude(0.12013627242021241)
