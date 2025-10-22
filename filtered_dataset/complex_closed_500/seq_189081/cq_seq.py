import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.004, 0.02075).lineTo(0.00525, 0.0205).lineTo(0.00525, 0.0195).lineTo(0.004, 0.01925).lineTo(0.004, 0.02075).close()
solid=wp_sketch0.add(loop0).extrude(-0.003877997710784711)
