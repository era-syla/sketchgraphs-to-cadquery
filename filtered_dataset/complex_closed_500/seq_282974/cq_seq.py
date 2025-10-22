import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00062, 0.0127).lineTo(0.0184, 0.0127).lineTo(0.0184, 0.00762).lineTo(0.00062, 0.00762).lineTo(0.00062, 0.0127).close()
solid=wp_sketch0.add(loop0).extrude(-0.052881168872253165)
