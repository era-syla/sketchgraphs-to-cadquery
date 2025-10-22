import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-1.2, 0.2).lineTo(1.2, 0.2).lineTo(1.2, -0.2).lineTo(-1.2, -0.2).lineTo(-1.2, 0.2).close()
solid=wp_sketch0.add(loop0).extrude(-2.7696316918248205)
