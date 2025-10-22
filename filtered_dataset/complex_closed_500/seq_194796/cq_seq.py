import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0, 0.08179).lineTo(0.0762, 0.08179).lineTo(0.0762, 0.00559).lineTo(0.0, 0.00559).lineTo(0.0, 0.08179).close()
solid=wp_sketch0.add(loop0).extrude(-0.1678618278366847)
