import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.015, 0.0015).lineTo(-0.027, 0.0015).lineTo(-0.03, -0.0).lineTo(-0.015, -0.0).lineTo(-0.015, 0.0015).close()
solid=wp_sketch0.add(loop0).extrude(-0.02418545814120488)
