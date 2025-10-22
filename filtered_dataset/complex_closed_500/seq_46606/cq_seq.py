import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, -0.00991).lineTo(0.00316, -0.00991).lineTo(0.00316, 0.0).lineTo(0.0, 0.0).lineTo(0.0, -0.00991).close()
solid=wp_sketch0.add(loop0).extrude(-0.010902566361286581)
