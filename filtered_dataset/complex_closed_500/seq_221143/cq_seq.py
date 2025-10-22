import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.02623).lineTo(-0.006, 0.02623).lineTo(-0.006, 0.01623).lineTo(0.0, 0.01623).lineTo(0.0, 0.02623).close()
solid=wp_sketch0.add(loop0).extrude(-0.02782411715130035)
