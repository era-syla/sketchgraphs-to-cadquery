import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00604, 0.00756).lineTo(0.00596, 0.00756).lineTo(0.00596, 0.00506).lineTo(-0.00604, 0.00506).lineTo(-0.00604, 0.00756).close()
solid=wp_sketch0.add(loop0).extrude(-0.018835141041897013)
