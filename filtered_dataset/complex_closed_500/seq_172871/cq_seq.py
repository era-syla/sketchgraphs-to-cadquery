import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.007, 0.0).lineTo(0.007, 0.02).lineTo(0.005, 0.02).lineTo(-0.0, 0.015).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.017635209164603233)
