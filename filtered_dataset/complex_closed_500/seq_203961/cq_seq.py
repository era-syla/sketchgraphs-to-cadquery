import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00655, -0.00635).lineTo(0.00655, -0.00635).lineTo(0.00655, -0.00411).lineTo(-0.00655, -0.00411).lineTo(-0.00655, -0.00635).close()
solid=wp_sketch0.add(loop0).extrude(0.02109439122622123)
