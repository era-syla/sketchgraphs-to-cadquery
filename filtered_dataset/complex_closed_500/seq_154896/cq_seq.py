import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02857, 0.01308).lineTo(0.02143, 0.01308).lineTo(0.02143, 0.00428).lineTo(-0.02857, 0.00428).lineTo(-0.02857, 0.01308).close()
solid=wp_sketch0.add(loop0).extrude(0.030671129734841363)
