import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(15.0, 0.0).lineTo(15.0, 6.5).lineTo(-0.0, 6.5).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-42.24394467088178)
