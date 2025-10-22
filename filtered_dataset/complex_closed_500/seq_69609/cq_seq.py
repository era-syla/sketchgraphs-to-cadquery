import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00934, 0.0).lineTo(0.00734, 0.0).lineTo(0.00734, 0.005).lineTo(0.00934, 0.005).lineTo(0.00934, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.013579358081967021)
