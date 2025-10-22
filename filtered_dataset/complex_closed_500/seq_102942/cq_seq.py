import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.011, 0.0).lineTo(0.011, 0.0).lineTo(0.014, -0.006).lineTo(-0.014, -0.006).lineTo(-0.011, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.07476189232285393)
