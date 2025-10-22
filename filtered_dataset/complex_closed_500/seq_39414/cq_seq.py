import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.15443, 0.07638).lineTo(-0.15037, 0.07638).lineTo(-0.15037, 0.07892).lineTo(-0.15443, 0.07892).lineTo(-0.15443, 0.07638).close()
solid=wp_sketch0.add(loop0).extrude(-0.00013490236723469483)
