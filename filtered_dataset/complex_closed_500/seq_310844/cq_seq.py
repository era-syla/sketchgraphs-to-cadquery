import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.45, -0.55).lineTo(0.9, -0.55).lineTo(0.9, -1.0).lineTo(0.45, -1.0).lineTo(0.45, -0.55).close()
solid=wp_sketch0.add(loop0).extrude(-0.6618163114205461)
