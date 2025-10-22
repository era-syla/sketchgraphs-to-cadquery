import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.003).lineTo(0.004, 0.003).lineTo(0.004, 0.012).lineTo(-0.0, 0.012).lineTo(0.0, 0.003).close()
solid=wp_sketch0.add(loop0).extrude(-0.0077078635709726465)
