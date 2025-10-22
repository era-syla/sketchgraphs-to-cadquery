import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0245, -0.0145).lineTo(0.015, -0.0145).lineTo(0.015, -0.0215).lineTo(0.0245, -0.0215).lineTo(0.0245, -0.0145).close()
solid=wp_sketch0.add(loop0).extrude(-0.013818121457486031)
