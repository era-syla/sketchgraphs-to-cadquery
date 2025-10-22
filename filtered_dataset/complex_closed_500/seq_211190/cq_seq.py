import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.10738, 0.05882).lineTo(0.09262, 0.05882).lineTo(0.09262, -0.04668).lineTo(-0.10738, -0.04668).lineTo(-0.10738, 0.05882).close()
solid=wp_sketch0.add(loop0).extrude(0.5519763968238135)
