import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01614, 0.00374).lineTo(0.07291, 0.00374).lineTo(0.07291, -0.00264).lineTo(0.01614, -0.00264).lineTo(0.01614, 0.00374).close()
solid=wp_sketch0.add(loop0).extrude(0.05586712384671705)
