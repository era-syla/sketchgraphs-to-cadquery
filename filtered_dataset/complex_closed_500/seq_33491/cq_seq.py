import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0125, 0.021).lineTo(0.01425, 0.021).lineTo(0.01425, 0.0195).lineTo(0.0129, 0.0195).lineTo(0.0125, 0.021).close()
solid=wp_sketch0.add(loop0).extrude(0.0015132717390850846)
