import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.02189, 0.00623).lineTo(-0.02189, 0.00623).lineTo(-0.02189, -0.00623).lineTo(0.02189, -0.00623).lineTo(0.02189, 0.00623).close()
solid=wp_sketch0.add(loop0).extrude(-0.07984571019684791)
