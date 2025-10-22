import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0635, 0.0762).lineTo(0.05715, 0.0762).lineTo(0.05715, 0.0508).lineTo(0.0635, 0.0508).lineTo(0.0635, 0.0762).close()
solid=wp_sketch0.add(loop0).extrude(0.07395047637616203)
