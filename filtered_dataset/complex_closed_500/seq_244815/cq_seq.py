import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.004, 0.0064).lineTo(-0.004, 0.0064).lineTo(-0.004, -0.0036).lineTo(0.004, -0.0036).lineTo(0.004, 0.0064).close()
solid=wp_sketch0.add(loop0).extrude(-0.023591199874501183)
