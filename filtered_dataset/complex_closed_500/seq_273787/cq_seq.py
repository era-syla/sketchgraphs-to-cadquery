import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.20322, 0.005).lineTo(-0.23567, 0.0219).lineTo(-0.20322, 0.0219).lineTo(-0.20322, 0.005).close()
solid=wp_sketch0.add(loop0).extrude(-0.05764756587334729)
