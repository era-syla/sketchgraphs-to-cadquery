import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.15291, -0.02414).lineTo(-0.10202, -0.00951).lineTo(-0.1146, 0.03426).lineTo(-0.16515, 0.01057).lineTo(-0.15291, -0.02414).close()
solid=wp_sketch0.add(loop0).extrude(0.09637332599752194)
