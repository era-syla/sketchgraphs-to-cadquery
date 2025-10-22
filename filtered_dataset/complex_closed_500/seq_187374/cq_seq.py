import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.635, 0.0).lineTo(0.635, -0.04993).lineTo(0.0, -0.04993).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(1.4033786436243774)
