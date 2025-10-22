import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00708, 0.04825).lineTo(0.06806, 0.04825).lineTo(0.06806, 0.01239).lineTo(0.00708, 0.01239).lineTo(0.00708, 0.04825).close()
solid=wp_sketch0.add(loop0).extrude(-0.036521117739073135)
