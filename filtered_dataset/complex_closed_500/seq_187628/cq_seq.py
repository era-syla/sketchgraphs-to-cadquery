import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02, 0.0074).lineTo(0.02, 0.0074).lineTo(0.02, -0.0074).lineTo(-0.02, -0.0074).lineTo(-0.02, 0.0074).close()
solid=wp_sketch0.add(loop0).extrude(-0.03933485245544322)
