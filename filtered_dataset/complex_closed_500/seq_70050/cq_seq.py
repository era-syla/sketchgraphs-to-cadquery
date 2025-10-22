import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01219, 0.00767).lineTo(0.008, 0.00767).lineTo(0.008, 0.00242).lineTo(0.01219, 0.00242).lineTo(0.01219, 0.00767).close()
solid=wp_sketch0.add(loop0).extrude(-0.004745226882759769)
