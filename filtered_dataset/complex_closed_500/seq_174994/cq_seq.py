import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0019).lineTo(0.01151, 0.0019).lineTo(0.01295, 0.0044).lineTo(0.0117, 0.007).lineTo(0.0, 0.007).lineTo(0.0, 0.0019).close()
solid=wp_sketch0.add(loop0).extrude(-0.011389902543698337)
