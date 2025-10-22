import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(1.0, 0.0).lineTo(1.0, 0.5).lineTo(-0.0, 0.5).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-1.2927274465080418)
