import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.004, 0.0162).lineTo(0.004, 0.0).lineTo(0.008, 0.0).lineTo(0.008, 0.0073).lineTo(0.00675, 0.0073).lineTo(0.00675, 0.0149).lineTo(0.008, 0.0149).lineTo(0.008, 0.0162).lineTo(0.004, 0.0162).close()
solid=wp_sketch0.add(loop0).extrude(-0.045760241796412866)
