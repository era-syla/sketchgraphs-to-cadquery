import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.425, 0.15).lineTo(1.315, 0.15).lineTo(1.465, 0.1).lineTo(3.3, 0.1).lineTo(3.825, 0.25).lineTo(3.825, 0.0).lineTo(0.425, -0.0).lineTo(0.425, 0.15).close()
solid=wp_sketch0.add(loop0).extrude(7.144949820262047)
