import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.065, 0.94).lineTo(0.065, 0.94).lineTo(0.065, 0.92).lineTo(-0.065, 0.92).lineTo(-0.065, 0.94).close()
solid=wp_sketch0.add(loop0).extrude(-0.24519060630411738)
