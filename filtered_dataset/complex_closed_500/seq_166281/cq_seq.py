import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.07208, 0.09665).lineTo(0.07958, 0.09665).lineTo(0.07958, 0.10415).lineTo(0.07208, 0.10415).lineTo(0.07062, 0.10415).lineTo(0.07062, 0.09665).lineTo(0.07208, 0.09665).close()
solid=wp_sketch0.add(loop0).extrude(-0.017347981814963293)
