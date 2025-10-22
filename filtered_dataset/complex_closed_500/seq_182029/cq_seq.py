import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.01509).lineTo(1.12, 0.01509).lineTo(1.12, 0.78009).lineTo(0.0, 0.78009).lineTo(0.0, 0.01509).close()
solid=wp_sketch0.add(loop0).extrude(-1.1369645647674318)
