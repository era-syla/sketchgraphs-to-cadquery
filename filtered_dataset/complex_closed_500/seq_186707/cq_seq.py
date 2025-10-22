import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00918, 0.001).lineTo(0.00924, 0.001).lineTo(0.00924, -0.001).lineTo(-0.00918, -0.001).lineTo(-0.00918, 0.001).close()
solid=wp_sketch0.add(loop0).extrude(-0.0538177761941552)
