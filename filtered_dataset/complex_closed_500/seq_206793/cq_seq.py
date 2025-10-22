import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00965, 0.0221).lineTo(0.06655, 0.0221).lineTo(0.06655, 0.00965).lineTo(0.00965, 0.00965).lineTo(0.00965, 0.0221).close()
solid=wp_sketch0.add(loop0).extrude(0.05223155502817624)
