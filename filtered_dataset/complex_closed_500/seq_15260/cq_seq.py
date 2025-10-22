import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.75635, 0.0127).lineTo(0.74365, 0.0127).lineTo(0.74365, 0.1127).lineTo(0.75635, 0.1127).lineTo(0.75635, 0.0127).close()
solid=wp_sketch0.add(loop0).extrude(-0.12188383134807503)
