import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00952, 0.01905).lineTo(-0.07938, 0.01905).lineTo(-0.07938, 0.0).lineTo(0.00952, 0.0).lineTo(0.00952, 0.01905).close()
solid=wp_sketch0.add(loop0).extrude(-0.2659821096916902)
