import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.2).lineTo(0.968, 0.2).lineTo(0.968, 0.212).lineTo(0.0, 0.212).lineTo(0.0, 0.2).close()
solid=wp_sketch0.add(loop0).extrude(-2.1488760452050015)
