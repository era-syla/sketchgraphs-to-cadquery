import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.23, 0.0195).lineTo(0.23, 0.0195).lineTo(0.23, -0.0195).lineTo(-0.23, -0.0195).lineTo(-0.23, 0.0195).close()
solid=wp_sketch0.add(loop0).extrude(-1.0391295359755344)
