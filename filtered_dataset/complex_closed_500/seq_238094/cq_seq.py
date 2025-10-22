import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00618, 0.01235).lineTo(0.00217, 0.01235).lineTo(0.00217, 0.00835).lineTo(0.00618, 0.00835).lineTo(0.00618, 0.01235).close()
solid=wp_sketch0.add(loop0).extrude(0.010731938050229373)
