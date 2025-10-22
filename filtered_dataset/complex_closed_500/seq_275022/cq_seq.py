import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, -0.15817).lineTo(-0.66522, -0.15817).lineTo(-0.66522, 1.26095).lineTo(0.0, 1.26095).lineTo(0.0, -0.15817).close()
solid=wp_sketch0.add(loop0).extrude(-1.176015238299756)
