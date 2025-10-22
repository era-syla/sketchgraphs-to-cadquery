import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00585, -0.0047).lineTo(0.00785, -0.0047).lineTo(0.00785, -0.01666).lineTo(-0.00585, -0.01666).lineTo(-0.00585, -0.0047).close()
solid=wp_sketch0.add(loop0).extrude(-0.020357941235270068)
