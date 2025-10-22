import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 0.22).lineTo(-0.02, 0.22).lineTo(-0.02, 0.0).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.6169100669437696)
