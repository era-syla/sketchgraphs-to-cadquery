import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00635, 0.00254).lineTo(-0.00635, 0.00254).lineTo(-0.00635, -0.00254).lineTo(0.00635, -0.00254).lineTo(0.00635, 0.00254).close()
solid=wp_sketch0.add(loop0).extrude(-0.002328201564022435)
