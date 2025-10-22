import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.00559).lineTo(0.0762, 0.00559).lineTo(0.0762, 0.08179).lineTo(-0.0, 0.08179).lineTo(0.0, 0.00559).close()
solid=wp_sketch0.add(loop0).extrude(0.13863295217953592)
