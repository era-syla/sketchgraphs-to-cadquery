import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.108, 0.0).lineTo(0.0, 0.0).lineTo(-0.0, 0.137).lineTo(-0.108, 0.137).lineTo(-0.108, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.297871791317204)
